#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 21:50
# @Author  : FanTuan
# @File    : gameEntity.py
from gameobjects.vector2 import *
import pygame
from statemachine import StateMachine


class GameEntity(object):
    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0.
        self.brain = StateMachine()
        self.id = 0

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x - w / 2, y - h / 2))

    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0 and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalised()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += travel_distance * heading


class Ant(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "ant", image)
        exploring_state = AntSateExploring(self)
        seeking_state = AntStateSeeking(self)
        delivering_state = AntStateDelivering(self)
        hunting_state = AntStateHunting(self)
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        self.carry_image = None

    def carry(self, image):
        self.carry_image = image

    def drop(self, surface):
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))
            self.carry_image = None

    def render(self, surface):
        GameEntity.render(self.surface)
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))


class World(object):
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
        self.backgroud = pygame.surface.Surface((640, 480)).convert()
        self.backgroud.fill((255, 255, 255))

    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def process(self, time_passed):
        time_passed_second = time_passed / 1000.0
        for entity in self.entities.itervalues():
            entity.process(time_passed_second)

    def render(self, surface):
        surface.blit(self.backgroud, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)

    def get_close_entity(self, name, location, range=100.):
        location = Vector2(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:
                    return entity
        return None

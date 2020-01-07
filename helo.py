#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 14:32
# @Author  : FanTuan
# @File    : helo.py

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

pygame.init()

background_image_filename = 'images/sushiplate.jpg'
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
mouse_image_filename = 'images/fugu.png'
sprite_image_filename = 'images/fugu.png'
# font=pygame.font.Font('fonts/prstart.ttf',16)
# logo=font.render("fantuan",False,(0,0,0))
# pygame.image.save(logo,"logo.png")
pygame.display.set_caption("Helo")


clock = pygame.time.Clock()
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

# 鼠标控制+AD旋转
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# AD旋转
sprite_pos = Vector2(200, 350)   # 初始位置
sprite_speed = 300.     # 每秒前进的像素数（速度）
sprite_rotation = 0.      # 初始角度
sprite_rotation_speed = 360. # 每秒转动的角度数（转速）

# WASD
# sprite_pos = Vector2(200, 150)
# sprite_speed=300


# 游荡
position = Vector2(100.0, 100.0)
heading = Vector2()

# 撞墙
x_sprite, y_sprite = 100, 100
speed_x, speed_y = 250, 100

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                exit()
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption("Window resized to " + str(event.size))

    # 改变大小后填充窗口，先画背景
    screen_width, screen_height = SCREEN_SIZE
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    # 按键元组
    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    # 按时间绘画
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0


    '''AD旋转/WS鼠标点击移动'''
    rotation_direction = 0.
    movement_direction = 0.

    # 鼠标控制旋转
    rotation_direction = pygame.mouse.get_rel()[0] / 5.0

    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    if pressed_keys[K_UP]or pressed_mouse[0]:
        movement_direction = -1.
    if pressed_keys[K_DOWN]or pressed_mouse[2]:
        movement_direction = +1.
    rotation_spritre = pygame.transform.rotate(sprite, sprite_rotation)
    width, hight = rotation_spritre.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x - width / 2, sprite_pos.y - screen_height / 2)
    screen.blit(rotation_spritre, sprite_draw_pos)

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
    heading_x = sin(sprite_rotation * pi / 180)
    heading_y = cos(sprite_rotation * pi / 180)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction
    sprite_pos += heading * sprite_speed * time_passed_seconds

    '''WASD移动版'''
    # key_direction = Vector2(0, 0)
    # if pressed_keys[K_LEFT]:
    #     key_direction.x = -1
    # elif pressed_keys[K_RIGHT]:
    #     key_direction.x = +1
    # if pressed_keys[K_UP]:
    #     key_direction.y = -1
    # elif pressed_keys[K_DOWN]:
    #     key_direction.y = +1
    # key_direction.normalise()
    # screen.blit(sprite, sprite_pos)
    # sprite_pos += key_direction * sprite_speed * time_passed_seconds



    '''指针周围游荡'''
    # screen.blit(mouse_cursor, position)
    # destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*mouse_cursor.get_size()) / 2
    # vector_to_mouse = Vector2.from_points(position, destination)
    # vector_to_mouse.normalise()
    # heading = heading + (vector_to_mouse * .6)
    # position += heading * time_passed_seconds

    '''碰撞反弹'''
    # screen.blit(sprite, (x_sprite, y_sprite))
    # x_sprite += time_passed_seconds * speed_x
    # y_sprite += time_passed_seconds * speed_y
    # if x_sprite > 640 - sprite.get_width():
    #     speed_x = -speed_x
    #     x = 640 - sprite.get_width()
    # elif x_sprite < 0:
    #     speed_x = -speed_x
    #     x = 0
    # if y_sprite > 480 - sprite.get_height():
    #     speed_y = -speed_y
    #     y_sprite = 480 - sprite.get_height()
    # elif y_sprite < 0:
    #     speed_y = -speed_y
    #     y = 0

    '''鼠标指针版'''
    # x, y = pygame.mouse.get_pos()
    # x -= mouse_cursor.get_width() / 2
    # y -= mouse_cursor.get_height() / 2
    # screen.blit(mouse_cursor, (x, y))

    pygame.display.update()

if __name__ == '__main__':
    pass

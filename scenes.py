import sys
import os
import math
import random
import matplotlib.pyplot as plt
import numpy as np 
sys.path.append("./src/")
from geometry import * 
from hitable import * 
from shape import * 
from camera import * 
from material import * 
from texture import * 

#define scenes here
# TODO: make scenes.py a parser with a text scenefile input

def create_scene():
    hit_object_list = []
    small_balls = []
    
    # Light
    light = diffuse_light(constant_texture(vec3(3, 2.55, 2.55)))
    hit_object_list.append(xz_rect(123, 423, 147, 412, 750, light))
    
    # Floor
    floor_img = plt.imread("./texture_maps/woodenFloor.png")
    floor_img = np.swapaxes(floor_img, 0, 1)
    nx, ny, _ = floor_img.shape
    mat_floor = lambertian(image_texture(floor_img, nx, ny))
    hit_object_list.append(rotate_y(box(vec3(-500, -200, -100), vec3(1500, 100, 500), mat_floor), -15))
    
    # Mirror
    hit_object_list.append(rotate_z(box(vec3(-10, 95, -80), vec3(-8, 360, 80), metal(vec3(0.9, 0.9, 0.9), 0)), 10))
    #hit_object_list.append(rotate_z(box(vec3(-5, 90, -80), vec3(-3, 360, 80), metal(vec3(0.9, 0.9, 0.9), 0)), 10))
    
    # Box
    box_img = plt.imread("./texture_maps/pinkWood.png")
    box_img = np.swapaxes(box_img, 0, 1)
    nx, ny, _ = box_img.shape
    mat_box = lambertian(image_texture(box_img, nx, ny))
    hit_object_list.append(box(vec3(-215, 100, -100),vec3(-85, 400, 100), mat_box))
    
    # Glass sphere
    hit_object_list.append(sphere(vec3(425, 325, 250), 125, dielectric(1.5)))
    # rotate and translate the candies in the glass sphere
    
    # Small spheres
    ns = 200
    candy_img = plt.imread("./texture_maps/candy.png")
    candy_img = np.swapaxes(candy_img, 0, 1)
    nx, ny, _ = candy_img.shape
    mat_candy = lambertian(image_texture(candy_img, nx, ny))
    #mat_candy = lambertian(constant_texture(vec3(1.0, 0.8, 0.8)))
    for j in range(ns):
        choose_mat = random.random()
        center = vec3(165*(random.random()+0.01), 165, 165*(random.random()+0.01))
        if (choose_mat < 0.4): # diffuse with candy texture
            small_balls.append(sphere(center, 10, mat_candy))
        elif (choose_mat < 0.8): # metal
            small_balls.append(sphere(center, 10, metal(vec3(1.0, 0.6, 0.8), 10.0)))
        else: # Glass
            small_balls.append(sphere(center, 10, dielectric(1.5)))
                
    hit_object_list.append(translate(rotate_y(bvh_node(small_balls, 0.0, 1.0), -30), vec3(200, -55, -130)))
    #rotate and translate and bvh node test end 
    
    return hit_object_list
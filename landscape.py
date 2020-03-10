import pygame
import pygame
from pygame.locals import *
import pygame.gfxdraw
import math
from random import randrange, choice
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (105, 105, 105)
blue = (0, 0, 175)
blue2 = (0, 131, 195)
red2 = (225, 6, 0)
red = (170, 0, 0)
green = (0, 170, 0)
green2 = (27, 171, 11)
orange = (200, 50, 0)
brown = (139, 69, 19)
purple = (124, 70, 145)
gold_yellow = (255, 223, 0)
lake = (158, 206, 204)
# bright game colors
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_black = (1, 1, 1)
bright_grey = (211, 211, 211)
bright_blue = (0, 0, 255)
bright_orange = (200, 100, 0)
light_sky_blue = (135, 206, 250)
saddleBrown = (139, 69, 19)
sky_color = (135, 206, 235)

image = pygame.image.load('rock.jpg')
imagex = 360
imagey = 260


class Landscape:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height

        self.objects = []
        self.createObjects()

        return

    def createObjects(self):
        sky = Main(sky_color, self.mWidth, self.mHeight)

        self.objects.append(sky)
        return

    def draw(self, surface):
        for object in self.objects:
            object.draw(surface)

        return


class Birds:
    def __init__(self, color, width, height, x, y):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, surface):

        pygame.draw.arc(surface, black, ((self.width, self.height),
                                         (25, 25)), 0, math.pi/1, 1)
        pygame.draw.arc(surface, black, ((self.width + 25, self.height),
                                         (25, 25)), 0, math.pi/1, 1)


class Cloud:
    def __init__(self, color, width, height, x, y):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = self.width, self.height, self.x, self.y

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)


class Mountain:
    def __init__(self, color, filler,  x, y):
        self.x = x
        self.y = y
        self.color = color
        self.width = 60
        self.height = 60
        self.thick = 5
        self.filler = filler
        self.rect = self.filler, self.x, self.y

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.rect)
        pygame.draw.polygon(surface, self.color, self.rect)
        pygame.draw.polygon(surface, self.color, self.rect)
        pygame.draw.polygon(surface, self.color, self.rect)


class Sun:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.rect = self.x, self.y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect, self.radius)


class Waterfall:
    def __init__(self, color, p1, p2):
        self.color = color
        self.x = p1
        self.y = p2
        self.rect = self.x, self.y

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.x, self.y, 30)


class Main:
    def __init__(self, color, width, height):
        self.scolor = color
        self.mWidth = width
        self.mHeight = height
        self.x = 0
        self.y = 0
        self.rect = (self.x, self.y, self.mWidth, self.mHeight)

        self.cloudcolors = [
            (239, 238, 237), (224, 223, 221)]
        self.clouds = []
        self.mountains = []
        self.getMountain()
        self.getClouds()
        self.getBirds()
        self.getSun()
        self.getWaterfall()

    def getClouds(self):
        num_of_clouds = randrange(3, 7)
        for num in range(num_of_clouds):
            color = choice(self.cloudcolors)
            x = randrange(10, self.mWidth - 10)
            y = randrange(5, int(self.mHeight / 5))
            width = randrange(100, 200)
            height = randrange(60, 70)
            newcloud = Cloud(color, x, y, width, height)
            self.clouds.append(newcloud)

    def getBirds(self):
        num_of_birds = randrange(3, 7)
        for num in range(num_of_birds):
            color = black
            x = randrange(10, self.mWidth - 10)
            y = randrange(5, int(self.mHeight / 5))
            width = randrange(100, 200)
            height = randrange(60, 70)

            newbird = Birds(color, x, y, width, height)
            self.clouds.append(newbird)

    def getMountain(self):
        num_of_mountain = 4
        fill = [(0, 600), (0, 600), (900, 600), (400, 800)]
        xs = [(1, 250), (300, 250), (650, 250), (900, 250)]
        ys = [(400, 600), (800, 800), (200, 900), (900, 900)]
        for num in range(num_of_mountain):
            color = brown
            x = xs[num]
            y = ys[num]
            filler = fill[num]
            mountain = Mountain(color, filler, x, y)
            self.mountains.append(mountain)

    def getSun(self):

        color = gold_yellow
        x = 490
        y = 400
        radius = 100

        sun = Sun(color, x, y, radius)
        self.clouds.append(sun)

    def getWaterfall(self):
        color = lake
        p1 = (496, 450)
        p2 = (496, 700)

        waterfall = Waterfall(color, p1, p2)
        self.mountains.append(waterfall)

    def draw(self, surface):
        pygame.draw.rect(surface, self.scolor, self.rect)
        for cloud in self.clouds:
            cloud.draw(surface)
        for mountain in self.mountains:
            mountain.draw(surface)

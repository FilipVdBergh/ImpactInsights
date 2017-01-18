import pygame
from pygame.locals import *

class pygame_impactplot:
    def __init__(self, screen_width, screen_height):

        self.screen_height = screen_height
        self.screen_width = screen_width
        self.fullscreen = False
        self.lane_padding_percentage = 0.25
        self.space_between_lanes = 0.05
        self.title_font = "arial"
        self.title_font_color = (0, 0, 0)
        self.title_font_size = 24
        self.lane_font  = "cambria"
        self.lane_font_color = (0, 0, 0)
        self.lane_font_size = 14
        self.lane_color = (255, 255, 255)
        self.box_title_font = "arial"
        self.box_title_font_color = (0, 0, 0)
        self.box_title_font_size = 18
        self.box_color = (50, 50, 50)
        self.box_text_font = "arial"
        self.box_text_font_color = (255,255,255)
        self.box_text_font_size = 12
        self.box_width_padding_percentage = 0.10
        self.box_height_padding_percentage = 0.10
        self.bg_color = (255, 255, 255)
        self.bg_picture = None

        pygame.init()


    def plot(self, canvas):
        self.lane_width = self.screen_width
        self.lane_height = self.screen_height / (len(canvas.layer) + (len(canvas.layer) - 1) * self.lane_padding_percentage )

        screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        for y, l in enumerate(canvas.layer.values()):
            lane_surface = pygame.surface.Surface((self.lane_width, self.lane_height))
            lane_surface.fill(self.lane_color)
            f = pygame.font.SysFont(self.lane_font, self.lane_font_size)
            lane_text_surface = f.render(canvas.layernames[y], True, self.lane_font_color)
            screen.blit(lane_surface, (0, y*(self.lane_height*(1+self.lane_padding_percentage))))
            screen.blit(lane_text_surface, (0, y*(self.lane_height*(1+self.lane_padding_percentage))))

            for x, b in enumerate(l):
                box_width = self.lane_width/len(l)
                box_surface = pygame.surface.Surface((box_width, self.lane_height * (1 - self.box_height_padding_percentage)))
                box_surface.fill(self.box_color)
                screen.blit(box_surface, (self.box_width_padding_percentage*box_width + (x / len(l)) * self.lane_width * (1 + self.box_width_padding_percentage),
                                          y*(self.lane_height*(1+self.lane_padding_percentage))+(self.box_height_padding_percentage*self.lane_height)))

        pygame.display.update()


class text_impactplot:
    def __init__(self):
        pass

    def plot(self, canvas):
        print(canvas.title.upper())
        print("These are the %s boxes to be drawn on the canvas:" % canvas.count_boxes())
        for l in canvas.layer:
            print("  Level", l, canvas.layernames[l])
            for b in canvas.layer[l]:
                print("    %s (Id %s)" % (b.title, b.id))
        print("These are the %s relationships to be drawn on the canvas:" % canvas.count_relationships())
        for r in canvas.relationships:
            print("    %s <connects to> %s" % (r.from_box.title, r.to_box.title))


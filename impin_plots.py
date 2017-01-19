import pygame
from pygame.locals import *

class pygame_impactplot:
    def __init__(self, screen_width, screen_height):

        self.screen_height = screen_height
        self.screen_width = screen_width
        self.fullscreen = False
        self.lane_padding_percentage = 0.25
        self.title_font = "arial"
        self.title_font_color = (0, 0, 0)
        self.title_font_size = 24
        self.lane_font  = "cambria"
        self.lane_font_color = (0, 0, 0)
        self.lane_font_size = 14
        self.lane_color = (255, 255, 255)
        self.box_title_font = "arial"
        self.box_title_font_color = (255, 255, 255)
        self.box_title_font_size = 16
        self.box_color = (50, 50, 50)
        self.box_text_font = "arial"
        self.box_text_font_color = (255,255,255)
        self.box_text_font_size = 12
        self.box_width_padding_percentage = 0.10
        self.box_height_padding_percentage = 0.20
        self.bg_color = (255, 255, 255)
        self.bg_picture = None

        pygame.init()


    def plot(self, canvas):
        self.lane_width = self.screen_width
        self.lane_height = self.screen_height / (len(canvas.layer) + (len(canvas.layer) - 1) * self.lane_padding_percentage )

        screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        maximum_number_of_boxes_per_layer = 0
        for l in canvas.layer.values():
            maximum_number_of_boxes_per_layer = max(maximum_number_of_boxes_per_layer, len(l))


        for y, l in enumerate(canvas.layer.values()):
            lane_surface = pygame.surface.Surface((self.lane_width, self.lane_height))
            lane_surface.fill(self.lane_color)
            f = pygame.font.SysFont(self.lane_font, self.lane_font_size)
            lane_text_surface = f.render(canvas.layernames[y], True, self.lane_font_color)
            lane_y = y*(self.lane_height*(1+self.lane_padding_percentage))
            screen.blit(lane_surface, (0, lane_y))
            screen.blit(lane_text_surface, (0, lane_y))

            for x, b in enumerate(l):
                box_width = (self.lane_width) / (maximum_number_of_boxes_per_layer + (self.box_width_padding_percentage * maximum_number_of_boxes_per_layer) + self.box_width_padding_percentage)
                box_surface = pygame.surface.Surface((box_width, self.lane_height * (1 - self.box_height_padding_percentage)))
                box_surface.fill(self.box_color)
                f = pygame.font.SysFont(self.box_title_font, self.box_title_font_size)
                box_text_surface = f.render(b.title, True, self.box_title_font_color)
                box_x = (self.lane_width - len(l)*box_width - (len(l)+1) * self.box_width_padding_percentage * box_width)/2 + self.box_width_padding_percentage * box_width + x * box_width * (1 + self.box_width_padding_percentage)
                #box_y = y * (self.lane_height*(1+self.lane_padding_percentage))+(self.box_height_padding_percentage*self.lane_height)
                box_y = lane_y + self.lane_height * (self.box_height_padding_percentage/2)
                screen.blit(box_surface, (box_x, box_y))
                screen.blit(box_text_surface, (box_x + box_width/2 - box_text_surface.get_width()/2, box_y))



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


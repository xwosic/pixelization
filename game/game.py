import pygame
from game.screen import Screen
from game.objects.pixel import Pixel
from game.groups.rects import RectGroup
from game.objects.bacteria import Bacteria


class Game:
    def __init__(self):
        # screen
        self.screen: Screen = None
        # time
        self.clock = pygame.time.Clock()
        self.FPS = 10
        # states
        self.running = False
        # everything is rect
        self.rects = RectGroup()

    def on_init(self):
        pygame.init()
        self.screen = Screen(tittle='pixelution', width=1200, height=600)
        self.running = True

        for i in range(20):
            Bacteria(None, self, 15 * i, 100)
        
        b1 = Bacteria(None, self, 600, 300)
        b2 = Bacteria(b1.dna, self, 600, 300)
        b3 = Bacteria(b2.dna, self, 600, 300)
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False               

        elif event.type == pygame.MOUSEBUTTONUP:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def handle_events(self):
        for event in pygame.event.get():
            self.on_event(event)

    def update(self):
        self.screen.screen.fill(self.screen.background_color)
        self.rects.update(self)
        pygame.display.update()

    def exit(self):
        self.running = False

    def clean_up(self):
        # save progress
        # to do
        # close game
        pygame.quit()

    def execute(self):
        if not self.running:
            self.on_init()

        while self.running:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.update()

        self.clean_up()

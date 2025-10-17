import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pygame
from engine.window import Window
from engine.scene import Scene
from engine.sprite import Sprite

class MyScene(Scene):
    def __init__(self):
        super().__init__()
        self.player = Sprite(100, 100)
        self.sprites.append(self.player)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= 200 * dt
        if keys[pygame.K_RIGHT]:
            self.player.x += 200 * dt
        if keys[pygame.K_UP]:
            self.player.y -= 200 * dt
        if keys[pygame.K_DOWN]:
            self.player.y += 200 * dt

        super().update(dt)

if __name__ == "__main__":
    window = Window()
    scene = MyScene()
    window.run(scene)

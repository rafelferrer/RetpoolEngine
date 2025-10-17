import pygame

class Window:
    def __init__(self, width=800, height=600, title="Retpool Engine"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self, scene):
        while self.running:
            dt = self.clock.tick(60) / 1000  # Delta time en segundos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                scene.handle_event(event)

            scene.update(dt)
            self.screen.fill((0, 0, 0))
            scene.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

import pygame

class Sprite:
    def __init__(self, x, y, images=None, frame_time=0.1):
        """
        images: lista de rutas de imágenes para animación
        frame_time: tiempo por frame en segundos
        """
        self.x = x
        self.y = y
        self.images = [pygame.image.load(img).convert_alpha() for img in images] if images else []
        self.frame_time = frame_time
        self.current_frame = 0
        self.timer = 0
        self.rect = self.images[0].get_rect(topleft=(x, y)) if self.images else pygame.Rect(x, y, 50, 50)

    def update(self, dt):
        if self.images:
            self.timer += dt
            if self.timer >= self.frame_time:
                self.timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.images)
        # Actualiza rect posición
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.images:
            screen.blit(self.images[self.current_frame], (self.x, self.y))
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)

class Scene:
    def __init__(self, name=""):
        self.name = name
        self.sprites = []
        self.next_scene = None  # Permite cambiar de pantalla

    def handle_event(self, event):
        for sprite in self.sprites:
            if hasattr(sprite, 'handle_event'):
                sprite.handle_event(event)

    def update(self, dt):
        for sprite in self.sprites:
            if hasattr(sprite, 'update'):
                sprite.update(dt)

    def draw(self, screen):
        for sprite in self.sprites:
            if hasattr(sprite, 'draw'):
                sprite.draw(screen)

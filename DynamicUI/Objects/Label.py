from .. import Element, Renderer, InputHandler
from pygame import Font, Event, Surface, SRCALPHA


class LabelInputHandler(InputHandler):
    def handle_event(self, event: Event, element: Element) -> None:
        pass


class LabelRenderer(Renderer):
    def __init__(self, text: str, font: Font = Font(None, 24), text_color = (20, 20, 20),
                 anchor: str = "midleft", background_color = None) -> None:
        super().__init__(background_color=background_color)
        self.text = text
        self.text_color = text_color
        self.font = font
        self.anchor = anchor


    def measure_content(self, element: Element) -> tuple[float, float]:
        text_surface = self.font.render(self.text, True, self.text_color)
        return text_surface.get_size()

    def render(self, element: Element) -> Surface:
        """surface = super().render(element)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(element.rect.width // 2, element.rect.height // 2))
        surface.blit(text_surface, text_rect)
        return surface"""
        # Create surface with background
        surface = Surface((element.rect.width, element.rect.height), SRCALPHA)
        surface.fill(self.background_color) if self.background_color else surface.fill((0, 0, 0, 0))
        # Render text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        if self.anchor == "center":
            text_rect.center = (element.rect.width // 2, element.rect.height // 2)
        elif self.anchor == "topleft":
            text_rect.topleft = (0, 0)
        elif self.anchor == "topright":
            text_rect.topright = (element.rect.width, 0)
        elif self.anchor == "bottomleft":
            text_rect.bottomleft = (0, element.rect.height)
        elif self.anchor == "bottomright":
            text_rect.bottomright = (element.rect.width, element.rect.height)
        elif self.anchor == "midtop":
            text_rect.midtop = (element.rect.width // 2, 0)
        elif self.anchor == "midbottom":
            text_rect.midbottom = (element.rect.width // 2, element.rect.height)
        elif self.anchor == "midleft":
            text_rect.midleft = (0, element.rect.height // 2)
        elif self.anchor == "midright":
            text_rect.midright = (element.rect.width, element.rect.height // 2)

        # Blit text onto surface
        surface.blit(text_surface, text_rect)
        return surface


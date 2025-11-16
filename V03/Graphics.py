# Graphics.py
from .Element import Element
from pygame import Surface
import pygame
import random

class Graphics:
    def __init__(self, background_color = None):
        self.surface: Surface|None = None
        self._cached_for: Element|None = None
        self.background_color = background_color

    def draw(self, element: Element) -> Surface:
        # default draw returns a small transparent surface instead of an opaque black
        return Surface((10, 10), pygame.SRCALPHA)

    def render(self, element: 'Element') -> Surface:
        # only reuse cached surface when it was created for this exact element
        if self.surface and self._cached_for is element:
            return self.surface

        # helper to ensure integer positive sizes for Surface creation
        def _make_surface_for(el: 'Element') -> Surface:
            # prefer explicit el.size, then el.min_size, then fallback to (1,1)
            w = 1
            h = 1
            if getattr(el, 'size', None):
                try:
                    w, h = int(el.size[0]), int(el.size[1])
                except Exception:
                    pass
            if (w <= 0 or h <= 0) and getattr(el, 'min_size', None):
                try:
                    w = max(1, int(el.min_size[0]))
                    h = max(1, int(el.min_size[1]))
                except Exception:
                    pass
            w = max(1, w)
            h = max(1, h)
            return Surface((w, h), pygame.SRCALPHA)

        # recursive renderer that composes an element's surface using its own
        # draw (if any) and its children's rendered surfaces.
        def _render_element(el: 'Element') -> Surface:
            # create base surface for this element
            surf = _make_surface_for(el)

            # fill background if a background color was provided
            bg = None
            if getattr(el, 'graphics', None):
                bg = el.graphics.background_color
            if bg is not None:
                surf.fill(bg)

            # draw this element's own content
            if getattr(el, 'graphics', None):
                # use the Graphics.draw implementation to get content to blit
                content = el.graphics.draw(el)
                # ensure content fits into surf
                surf.blit(content, (0, 0))

            # render children and blit them at their local positions
            for child in el.children:
                # get child's surface. If child has a graphics object, prefer it
                if getattr(child, 'graphics', None):
                    # ensure child size is sane before rendering
                    if not getattr(child, 'size', None) or child.size[0] <= 0 or child.size[1] <= 0:
                        if getattr(child, 'min_size', None):
                            child.size = (int(child.min_size[0]), int(child.min_size[1]))
                        else:
                            child.size = (1, 1)
                    # clear child's cached surface so we always re-render for current state
                    child.graphics.surface = None
                    if hasattr(child.graphics, '_cached_for'):
                        child.graphics._cached_for = None
                    child_surf = child.graphics.render(child)
                else:
                    # no graphics object on the child: compose a surface from its subtree
                    child_surf = _render_element(child)

                # ensure we have integer local coords
                cx, cy = int(child.x), int(child.y)
                surf.blit(child_surf, (cx, cy))

            return surf

        # render this element (and its subtree) and cache the result on this Graphics
        composed = _render_element(element)
        self.surface = composed
        self._cached_for = element
        return self.surface

    def invalidate(self, element: Element) -> Element:
        # clear this graphics' cache for the given element
        if getattr(self, 'surface', None):
            self.surface = None
            self._cached_for = None

        # bubble invalidation up so parent caches are cleared too
        if element.parent:
            if element.parent.graphics:
                element.parent.graphics.invalidate(element.parent)
        return element

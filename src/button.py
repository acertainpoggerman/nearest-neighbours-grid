import pygame
from misc.constants import *
from misc.utils import *

from typing import Optional

class Button():
    def __init__(
        self, 
        location: tuple[int, int], width: int, height: int, 
        image_url: str, onclick,
        color: Optional[pygame.Color] = None, 
        hover_color: Optional[pygame.Color] = None,
        padding: int = 4, border_radius: int = 4
    ) -> None:
        
        self.width = width
        self.height = height
        self.location = location
        
        self.onclick = onclick
        
        self.hovered = False
        
        self.color = color
        self.hover_color = hover_color
        
        self.bounds = pygame.Rect(location[0], location[1], self.width, self.height)
        self.image = pygame.image.load(image_url).convert_alpha()
        
        self.padding = padding
        self.border_radius = border_radius
        
        self.image = pygame.transform.scale(self.image, (self.width - self.padding*2, self.height - padding*2))
       
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.bounds.collidepoint(pos): self.onclick()
            
    
    def set_color(self, color: Optional[pygame.Color] = None) -> None:
        self.color = color
        
    def update(self, pos: tuple[int, int]) -> None:
        if self.bounds.collidepoint(pos): self.hovered = True
        else: self.hovered = False
    
    
    def render(self, screen) -> None:
        
        offset = get_centered_start(
            (self.width, self.height),
            (self.image.get_width(), self.image.get_height())
        )
        
        if self.hovered and self.hover_color != None:
            pygame.draw.rect(
                screen, self.hover_color, self.bounds, 0,
                self.border_radius
            )
            
        if self.color != None:
            pygame.draw.rect(
                screen, self.color, self.bounds, 0,
                self.border_radius
            )
            
            
        screen.blit(self.image, offset_tuple(self.location, offset))
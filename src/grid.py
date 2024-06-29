import pygame

# You are probably going to use [numpy] and [random]

from os import path, pardir

from misc.constants import *
from misc.utils import *

from button import Button


class Grid():
    """ A class that represents a square grid
    """
    def __init__(self, screen: pygame.Surface, boxes_per_axis: int, randomized_point_count: int = 5, width: int = 800) -> None:

        self.gridline_color: Color = GRAY25
        self.bounds_color: Color = WHITE
        self.dot_color: Color = WHITE
        self.link_color: Color = GREEN
        self.text_color: Color = GRAY50
        
        self.points: list[Point] = []
        self.nearest_points: tuple[Point, Point] = (None, None)
        
        self.can_click = False
        self.randomized_point_count = randomized_point_count
        
        self.screen = screen
        self.size = width, width
        self.boxes_per_axis = boxes_per_axis
        
        start = get_centered_start(self.screen.get_size(), self.size)
        self.bounds = pygame.Rect(*start, *self.size)
        
        button_size: int = 50
        assets_path = path.abspath(path.join(__file__, f"{pardir}/{pardir}/assets/"))
        
        self.font = pygame.font.Font(f"{assets_path}/fonts/OpenSans-Regular.ttf", 20)
        
        # Buttons < Start>
        self.refresh_button = Button(
            (
                self.start[0] + get_centered_start(self.size, (50, 50))[0],
                self.start[1] + self.height + 25
            ), 
            button_size, button_size,
            f"{assets_path}/restart-icon.png", 
            self.refresh_grid,
            
            hover_color=GRAY25, border_radius=8
        )
        
        self.link_button = Button(
            (
                self.refresh_button.location[0] - 8 - button_size,
                self.start[1] + self.height + 25
            ), 
            button_size, button_size,
            f"{assets_path}/link-icon.png",
            self.link_nearest_points,
            
            hover_color=RED_ALT1, border_radius=8, padding=8
        )
        
        self.toggle_button = Button(
            (
                self.refresh_button.location[0] + self.refresh_button.width + 8,
                self.start[1] + self.height + 25
            ),
            button_size, button_size,
            f"{assets_path}/pointer-icon.png",
            self.toggle_grid_clicking,
            
            hover_color=GRAY25, border_radius=8, padding=8
        )
        # Buttons < End >
        
    
    @property
    def start(self) -> Point:
        return get_centered_start(self.screen.get_size(), self.size)
        
    @property
    def width(self) -> int: return self.size[0]
    @property
    def height(self) -> int: return self.size[1]
    @property
    def box_size(self) -> int: return self.width // self.boxes_per_axis
    
    @property
    def intersections_per_axis(self) -> int: 
        """ The number of intersections per axis, excluding intersections on the boundary. """
        return self.boxes_per_axis - 1
    @property
    def num_intersections(self) -> int: 
        """ The number of intersections in the entire grid, excluding intersections on the boundary """
        return self.intersections_per_axis ** 2
    
    
    
    def handle_event(self, event: pygame.event.Event) -> None:
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.bounds.collidepoint(pos) and self.can_click: 
                self.toggle_point(offset_tuple(pos, scale_tuple(self.start, -1)))
                self.validate_points()
                return
            
        self.link_button.handle_event(event)
        self.refresh_button.handle_event(event)
        self.toggle_button.handle_event(event)
    
    def update(self, pos: tuple[int, int]) -> None:
         self.refresh_button.update(pos)
         self.toggle_button.update(pos)
         self.link_button.update(pos)
         
    
    def render(self) -> None:
        
        # Rendering top text (Number of Points)
        text = self.font.render(f"Number of Points: {len(self.points)}", True, WHITE)
        text_rect = text.get_rect()
        text_rect.bottomleft = offset_tuple(self.start, (0, -10))
        self.screen.blit(text, text_rect)
        
        # Rendering the buttons
        self.refresh_button.render(self.screen)
        self.toggle_button.render(self.screen)
        self.link_button.render(self.screen)
        
        # Rendering the grid lines
        for x in range(1, self.boxes_per_axis):
            pygame.draw.line(
                self.screen, self.gridline_color, 
                (self.start[0] + x * self.box_size, self.start[1]), 
                (self.start[0] + x * self.box_size, self.start[1] + self.height),
            )
            
        for y in range(1, self.boxes_per_axis):
            pygame.draw.line(
                self.screen, self.gridline_color, 
                (self.start[0], self.start[1] + y * self.box_size), 
                (self.start[0] + self.width, self.start[1] + y * self.box_size),
            )
        
        
        # Render the line connecting the two nearest points
        if not None in self.nearest_points:
            nearest_points_screen_space = self.to_screen_space(self.nearest_points[0]), self.to_screen_space(self.nearest_points[1])
            pygame.draw.line(
                    self.screen, self.link_color, 
                    *nearest_points_screen_space, 4
                )
        
        # Render Points on the Grid (Will convert the points from grid-space to screen-space)
        for point in self.points:
            point_screen_space = self.start[0] + self.box_size * point[0], self.start[1] + self.box_size * point[1]
            pygame.draw.circle(self.screen, self.dot_color, point_screen_space, 10)
        
        # Rendering the boundary square. This should always be last in the rendering
        pygame.draw.rect(self.screen, self.bounds_color, self.bounds, 4)
    
 
 
    def clear_points(self) -> None:
        """ Clears all points in the grid """
        self.points = []
        self.nearest_points = (None, None)
    
    def refresh_grid(self) -> None:
        """ Performs an action based on the already
        
        Will execute clear_points() if the grid is in click mode (Indicated by the toggle button being blue)
        but will also perform randomize_points() if the grid is not in click mode.
        
        """
        
        if self.can_click: self.clear_points()
        else: 
            self.clear_points
            result = self.randomize_points(self.randomized_point_count)
            if len(set(result)) < len(result): 
                raise Exception("You got overlapping points :D")
            self.points = [*result]
            self.validate_points()
        
    def toggle_grid_clicking(self) -> None:
        """ Changes whether the grid can be clicked on to add/remove points. """
            
        self.can_click = not self.can_click
        
        # Changing the color of the toggle button
        if self.can_click: self.toggle_button.set_color(BLUE_ALT1)
        else: self.toggle_button.set_color()
    
    def link_nearest_points(self) -> None:
        self.nearest_points = self.find_nearest_points()
        if not (self.nearest_points[0], self.nearest_points[1]) == (None, None):
            if not (self.nearest_points[0] in self.points or self.nearest_points[1] in self.points):
                raise Exception("You are giving the grid wrong coordinates")
        
    def validate_points(self) -> None:
        for point in self.points:
            if point[0] <= 0 or point[1] <= 0 or point[0] > self.intersections_per_axis or point[1] > self.intersections_per_axis:
                raise Exception("You got points on or outside the grid boundary")
    
    def to_screen_space(self, point) -> tuple[int, int]:
        return offset_tuple(self.start, (point[0]*self.box_size, point[1]*self.box_size))
        


# ---- CHALLENGE SECTION ------------------------------------------------------------------------------------------------- 
     
    def randomize_points(self, n: int) -> list[Point]:
        """ Creates a random list of non-overlapping points
        
        The resulting list of points [(x, y), ... ] should be in grid-space as opposed
        to screen-space (i.e. points on the grid).
        
        Parameters
        ----------
        n : int
            The number of points to create. If n exceeds the number of intersections on the grid, an Exception will be thrown.
            
        Returns
        -------
        The list of points. If the points return have points with the same coordinate, the program will crash :D
        
        """
        
        if n > self.num_intersections: raise Exception("Number of points to randomize exceeds capacity of grid.")
        
        # TODO: Start Here. You are free to remove anything below this method
        
        points: list[Point] = []
        return points
    
    
    def toggle_point(self, pos: tuple[int, int]) -> None:
        """ Adds or removes a point to an intersection on the grid (Thank you Fere for suggesting this (^-^) )
        
        Should snap the point to the grid intersection closest to the mouse cursor, as well as save the point
        to the self.points attribute. If a point already exists at the target position, remove that point instead. Should
        not add points on the boundary of the grid (e.g. (0, 0))
        
        Parameters
        ----------
        pos: tuple[int, int]
            The mouse position in screen-space, but relative to the grid, so at the top-left of the grid, pos will be
            (0, 0) and at the bottom-right, pos will be (width, height) of the grid.
        
        """
        
        # TODO: Start Here. You are free to remove anything below in this method. You can test how pos
        #       works by clicking the grid (in click mode) and seeing the output from the print statement
        
        print(f"Clicked point {pos}")        
        ...
    
    
    
    def find_nearest_points(self) -> tuple[int, int]:
        """ Finds the nearest pair of points in self.points
        
        The algorithm should find the two points closest points, and return their coordinates in the form ((x1, y1), (x2, y2)). If it
        works as intended, clicking the link button in the GUI should create a line that connects the 2 closest points.
        
        Ideally should work in O(nlogn) time, rather than O(n²) time.
        
        Returns
        -------
        The coordinates of the 2 nearest points in self.points, Or (None, None) if there are less than 2 points on the grid
        
        """
        
        # TODO: Start Here. You are free to remove anything below in this method
        
        points: tuple[Point, Point] = (None, None)
        return points
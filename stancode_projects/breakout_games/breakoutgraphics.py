"""
File: breakoutgraphics.py
Name: Sean Liu
---------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program will construct the layout of the breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved

import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width-self.ball.width)/2, y=(window_height-self.ball.height)/2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_ball)
        # Draw bricks
        n = 0
        n1 = 0
        for row in range(brick_rows):
            if n == brick_cols:
                n = 0
                n1 += 1
            for col in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.window.add(self.brick)
                self.brick.x += n1*(brick_spacing+brick_width)
                self.brick.y += brick_offset + n*(brick_spacing+brick_height)
                self.brick.filled = True
                if n < 2:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif n < 4:
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif n < 6:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif n < 8:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                else:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                n += 1
        # For user-end to end the game when all bricks are knocked off.
        self.brick_num = brick_cols*brick_rows

    def move_paddle(self, mouse):
        """
        This function will allow the midpoint of the paddle to
        chase the mouse's location.
        """
        if self.paddle.width//2 <= mouse.x <= self.window.width-self.paddle.width//2:
            self.paddle.x = mouse.x - self.paddle.width//2
        if mouse.x < 0:
            self.paddle.x = 0
        if mouse.x > self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    def start_ball(self, click):
        """
        This function will let the mouseclick to activate
        the ball.
        """
        if self.__dx == 0 and self.__dy == 0:
            if 0 < click.x < self.window.width:
                self.__dy = INITIAL_Y_SPEED
                self.__dx = random.randint(0, MAX_X_SPEED)
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def return_ball(self):
        """
        This method will re-allocate the ball back to
        the starting point.
        """
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.__dx = 0
        self.__dy = 0

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx *= -1

    def set_dy(self):
        self.__dy *= -1

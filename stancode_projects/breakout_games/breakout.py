"""
File: breakout.py
Name: Sean Liu
---------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program will allow the user to play
the breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# Global variable
brick_knocked = 0


def main():
    graphics = BreakoutGraphics()
    death = 0
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            graphics.set_dx()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        if graphics.ball.y > graphics.window.height:
            graphics.return_ball()
            death += 1
            if death == NUM_LIVES:
                break
        # These are the four collision points of the ball.
        collision1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        collision2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        collision3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        collision4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,
                                                   graphics.ball.y+graphics.ball.height)
        global brick_knocked
        if collision1 is not None:
            if collision1 is not graphics.paddle:
                graphics.window.remove(collision1)
                brick_knocked += 1
                graphics.set_dy()
            # To avoid the ball being trapped in the paddle.
            elif dy > 0:
                graphics.set_dy()
        elif collision2 is not None:
            if collision2 is not graphics.paddle:
                graphics.window.remove(collision2)
                brick_knocked += 1
                graphics.set_dy()
            elif dy > 0:
                graphics.set_dy()
        elif collision3 is not None:
            if collision3 is not graphics.paddle:
                graphics.window.remove(collision3)
                brick_knocked += 1
                graphics.set_dy()
            elif dy > 0:
                graphics.set_dy()
        elif collision4 is not None:
            if collision4 is not graphics.paddle:
                graphics.window.remove(collision4)
                brick_knocked += 1
                graphics.set_dy()
            elif dy > 0:
                graphics.set_dy()
        if brick_knocked == graphics.brick_num:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

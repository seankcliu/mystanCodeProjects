"""
File: breakout_extension.py
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
from campy.graphics.gobjects import GOval, GRect, GLabel
from breakoutgraphics_extension import BreakoutGraphics

# Constant
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# Global variable
brick_knocked = 0
scores = 0


def main():
    global brick_knocked
    global scores
    graphics = BreakoutGraphics()
    death = 0
    scoreboard = GLabel(f'Score: {scores}')
    scoreboard.font = '-30'
    scoreboard.color = 'seagreen'
    graphics.window.add(scoreboard, x=0, y=scoreboard.height)
    lives_left = GLabel(f'Lives: {NUM_LIVES-death}')
    lives_left.font = '-20'
    lives_left.color = 'crimson'
    graphics.window.add(lives_left, x=10, y=graphics.window.height)
    sign = GRect(300, 40)
    sign.filled = True
    sign.color = 'seagreen'
    sign.fill_color = 'seagreen'
    sign_double = GLabel('Score Doubled!!!')
    sign_double.font = '-40'
    sign_double.color = 'white'
    sign_bigger = GLabel('Bigger paddle!!!')
    sign_bigger.font = '-40'
    sign_bigger.color = 'white'

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
            lives_left.text = f'Lives: {NUM_LIVES-death}'
            if death == NUM_LIVES:
                break
        # These are the four collision points of the ball.
        collision1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        collision2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        collision3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        collision4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,
                                                   graphics.ball.y+graphics.ball.height)
        if collision1 is not None:
            if collision1 is not graphics.paddle:
                if collision1 is not scoreboard:
                    if collision1 is not lives_left:
                        graphics.window.remove(collision1)
                        brick_knocked += 1
                        if collision1 is graphics.brickred1:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision1 is graphics.brickred2:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision1 is graphics.brickred3:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision1 is graphics.brickblue1:
                            scores += 1
                            graphics.bigger_paddle()
                            paddle_bigger(graphics, sign, sign_bigger)
                        else:
                            scores += 1
                        scoreboard.text = f'Score: {scores}'
                        graphics.set_dy()
            if collision1 is graphics.paddle and dy > 0:
                graphics.set_dy()
        elif collision2 is not None:
            if collision2 is not graphics.paddle:
                if collision2 is not scoreboard:
                    if collision2 is not lives_left:
                        graphics.window.remove(collision2)
                        brick_knocked += 1
                        if collision2 is graphics.brickred1:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision2 is graphics.brickred2:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision2 is graphics.brickred3:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision2 is graphics.brickblue1:
                            scores += 1
                            graphics.bigger_paddle()
                            paddle_bigger(graphics, sign, sign_bigger)
                        else:
                            scores += 1
                        scoreboard.text = f'Score: {scores}'
                        graphics.set_dy()
            if collision2 is graphics.paddle and dy > 0:
                graphics.set_dy()
        elif collision3 is not None:
            if collision3 is not graphics.paddle:
                if collision3 is not scoreboard:
                    if collision3 is not lives_left:
                        graphics.window.remove(collision3)
                        brick_knocked += 1
                        if collision3 is graphics.brickred1:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision3 is graphics.brickred2:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision3 is graphics.brickred3:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision3 is graphics.brickblue1:
                            scores += 1
                            graphics.bigger_paddle()
                            paddle_bigger(graphics, sign, sign_bigger)
                        else:
                            scores += 1
                        scoreboard.text = f'Score: {scores}'
                        graphics.set_dy()
            if collision3 is graphics.paddle and dy > 0:
                graphics.set_dy()
        elif collision4 is not None:
            if collision4 is not graphics.paddle:
                if collision4 is not scoreboard:
                    if collision4 is not lives_left:
                        graphics.window.remove(collision4)
                        brick_knocked += 1
                        if collision4 is graphics.brickred1:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision4 is graphics.brickred2:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision4 is graphics.brickred3:
                            scores *= 2
                            double_score(graphics, sign, sign_double)
                        elif collision4 is graphics.brickblue1:
                            scores += 1
                            graphics.bigger_paddle()
                            paddle_bigger(graphics, sign, sign_bigger)
                        else:
                            scores += 1
                        scoreboard.text = f'Score: {scores}'
                        graphics.set_dy()
            if collision4 is graphics.paddle and dy > 0:
                graphics.set_dy()
        if brick_knocked == graphics.brick_num:
            break
        pause(FRAME_RATE)


def double_score(graphics, sign, sign_double):
    """
    :param graphics: BreakoutGraphics
    :param sign: GRect
    :param sign_double: GLabel

    This function pops a message on the top-right corner
    of the window.
    """
    graphics.window.add(sign, x=graphics.window.width - sign.width, y=0)
    graphics.window.add(sign_double, x=150, y=sign_double.height)
    pause(100)
    graphics.window.remove(sign)
    graphics.window.remove(sign_double)
    pause(100)
    graphics.window.add(sign, x=graphics.window.width - sign.width, y=0)
    graphics.window.add(sign_double, x=150, y=sign_double.height)
    pause(100)
    graphics.window.remove(sign)
    graphics.window.remove(sign_double)


def paddle_bigger(graphics, sign, sign_bigger):
    """
    :param graphics: BreakoutGraphics
    :param sign: GRect
    :param sign_bigger: GLabel

    This function pops a message on the top-right corner
    of the window.
    """
    graphics.window.add(sign, x=graphics.window.width - sign.width, y=0)
    graphics.window.add(sign_bigger, x=150, y=sign_bigger.height)
    pause(100)
    graphics.window.remove(sign)
    graphics.window.remove(sign_bigger)
    pause(100)
    graphics.window.add(sign, x=graphics.window.width - sign.width, y=0)
    graphics.window.add(sign_bigger, x=150, y=sign_bigger.height)
    pause(100)
    graphics.window.remove(sign)
    graphics.window.remove(sign_bigger)


if __name__ == '__main__':
    main()

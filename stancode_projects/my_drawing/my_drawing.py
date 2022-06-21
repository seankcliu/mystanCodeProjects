"""
File: my_drawing.py
Name: Sean Liu
----------------------
This program will show the coder's drawing
which is produced through the campy package.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Evil Genius

    This is Stewie Griffin from the TV series Family Guy. He is
    a well-spoken baby, whom I'm trying to be in the Python language.
    """
    window = GWindow(1000, 800)

    # The background is put in first.
    background1 = GPolygon()
    background1.add_vertex((0, 800))
    background1.add_vertex((0, 360))
    background1.add_vertex((1000, 600))
    background1.add_vertex((1000, 800))
    background1.filled = True
    background1.color = 'sage'
    background1.fill_color = 'sage'
    window.add(background1)
    background2 = GPolygon()
    background2.add_vertex((0, 360))
    background2.add_vertex((0, 0))
    background2.add_vertex((1000, 0))
    background2.add_vertex((1000, 600))
    background2.filled = True
    background2.color = 'cadetblue'
    background2.fill_color = 'cadetblue'
    window.add(background2)
    label1 = GLabel('SC101', x=60, y=100)
    label1.color = 'white'
    label1.font = 'Verdana-100-bold-italic'
    window.add(label1)
    label2 = GLabel('SC101', x=160, y=300)
    label2.color = 'silver'
    label2.font = 'Verdana-100-bold-italic'
    window.add(label2)
    label3 = GLabel('SC101', x=60, y=500)
    label3.color = 'white'
    label3.font = 'Verdana-100-bold-italic'
    window.add(label3)
    label4 = GLabel('SC101', x=160, y=700)
    label4.color = 'silver'
    label4.font = 'Verdana-100-bold-italic'
    window.add(label4)
    label5 = GLabel('SC101', x=500, y=100)
    label5.color = 'silver'
    label5.font = 'Verdana-100-bold-italic'
    window.add(label5)
    label6 = GLabel('SC101', x=600, y=300)
    label6.color = 'white'
    label6.font = 'Verdana-100-bold-italic'
    window.add(label6)
    label7 = GLabel('SC101', x=500, y=500)
    label7.color = 'silver'
    label7.font = 'Verdana-100-bold-italic'
    window.add(label7)
    label8 = GLabel('SC101', x=600, y=700)
    label8.color = 'white'
    label8.font = 'Verdana-100-bold-italic'
    window.add(label8)

    # Stewie's body will be added next.
    body = GOval(500, 500)
    body.filled = True
    body.color = 'gold'
    body.fill_color = 'gold'
    window.add(body, x=250, y=600)
    belt1 = GRect(40, 150, x=400, y=650)
    belt1.filled = True
    belt1.color = 'firebrick'
    belt1.fill_color = 'firebrick'
    window.add(belt1)
    belt2 = GRect(40, 160, x=560, y=640)
    belt2.filled = True
    belt2.color = 'firebrick'
    belt2.fill_color = 'firebrick'
    window.add(belt2)
    overall = GPolygon()
    overall.add_vertex((350, 800))
    overall.add_vertex((400, 750))
    overall.add_vertex((600, 750))
    overall.add_vertex((650, 800))
    overall.filled = True
    overall.color = 'firebrick'
    overall.fill_color = 'firebrick'
    window.add(overall)
    arm1 = GArc(120, 220, 300, 60)
    window.add(arm1, x=330, y=710)
    arm2 = GArc(120, 220, 180, 60)
    window.add(arm2, x=640, y=710)
    button1 = GOval(50, 50, x=395, y=730)
    button1.filled = True
    button1.fill_color = 'yellow'
    window.add(button1)
    button2 = GOval(50, 50, x=555, y=730)
    button2.filled = True
    button2.fill_color = 'yellow'
    window.add(button2)

    # Stewie's head is up next.
    head_top = GArc(700, 1100, 10, 160)
    head_top.filled = True
    head_top.color = 'antiquewhite'
    head_top.fill_color = 'antiquewhite'
    window.add(head_top, x=150, y=200)
    head_btm = GArc(700, 1100, 190, 160)
    head_btm.filled = True
    head_btm.color = 'antiquewhite'
    head_btm.fill_color = 'antiquewhite'
    window.add(head_btm, x=150, y=110)
    ear1 = GOval(50, 50)
    ear1.filled = True
    ear1.color = 'antiquewhite'
    ear1.fill_color = 'antiquewhite'
    window.add(ear1, x=120, y=400)
    ear2 = GOval(50, 50)
    ear2.filled = True
    ear2.color = 'antiquewhite'
    ear2.fill_color = 'antiquewhite'
    window.add(ear2, x=818, y=400)
    ear_line1 = GArc(220, 120, 0, 50)
    window.add(ear_line1, x=108, y=410)
    ear_line2 = GArc(220, 120, 130, 50)
    window.add(ear_line2, x=835, y=410)
    hair1 = GLine(223, 360, 193, 340)
    window.add(hair1)
    hair2 = GLine(260, 320, 230, 300)
    window.add(hair2)
    hair3 = GLine(310, 280, 280, 260)
    window.add(hair3)
    hair4 = GLine(360, 265, 340, 228)
    window.add(hair4)
    hair5 = GLine(420, 245, 410, 208)
    window.add(hair5)
    hair6 = GLine(485, 240, 480, 200)
    window.add(hair6)
    hair7 = GLine(560, 240, 555, 203)
    window.add(hair7)
    hair8 = GLine(630, 255, 625, 220)
    window.add(hair8)
    hair9 = GLine(700, 285, 695, 250)
    window.add(hair9)
    hair10 = GLine(740, 315, 750, 290)
    window.add(hair10)
    hair11 = GLine(780, 358, 790, 333)
    window.add(hair11)
    brow1 = GLine(415, 300, 325, 295)
    window.add(brow1)
    brow2 = GLine(720, 320, 620, 310)
    window.add(brow2)
    eye1 = GOval(120, 120, x=300, y=330)
    eye1.filled = True
    eye1.fill_color = 'white'
    window.add(eye1)
    eye_white1 = GArc(120, 220, 0, 180)
    eye_white1.filled = True
    eye_white1.fill_color = 'antiquewhite'
    window.add(eye_white1, x=300, y=330)
    eye2 = GOval(120, 120, x=600, y=340)
    eye2.filled = True
    eye2.fill_color = 'white'
    window.add(eye2)
    eye_white2 = GArc(120, 220, 0, 180)
    eye_white2.filled = True
    eye_white2.fill_color = 'antiquewhite'
    window.add(eye_white2, x=600, y=340)
    eye_black1 = GOval(15, 15)
    eye_black1.filled = True
    window.add(eye_black1, x=300, y=390)
    eye_black2 = GOval(15, 15)
    eye_black2.filled = True
    window.add(eye_black2, x=601, y=400)
    nose_top = GLine(510, 410, 530, 440)
    window.add(nose_top)
    nose_bottom = GLine(530, 440, 515, 450)
    window.add(nose_bottom)
    smile = GArc(220, 120, 200, 100)
    window.add(smile, x=430, y=460)
    smile_tip = GLine(549, 496, 541, 476)
    window.add(smile_tip)


if __name__ == '__main__':
    main()

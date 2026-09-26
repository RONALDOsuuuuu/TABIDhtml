from turtle import *
class face:
    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.nooseSize = 'small'
    def setSize(self, redius):
        self.size =redius
    def draw(self):
            self.goHome()
            pensize(3)
            speed(0)
            self.drawOutline()
            self.drawEye(135)
            self.drawEye(45)
            self.drawMouth()
            self.drawNose()
            pensize
    def goHome(self):
            penup()
            goto(self.record)
            setheading(0)
    def drawOutline(self):
            penup
            forward(self.size)
            left(90)
            pendown()
            circle(self.size)
            self.goHome()
    def drawEye(self):
            penup()
            left(turn)
            forward(self.size/2)
            pendown()
            dot(self.size/10)
            self.goHome()
    def drawMouth(self):
            penup()
            right(135)
            forward(self.size/1.7,90)
            self.goHome()
    def drawNose(self):
            if self.noseSize == 'large' :
                dot(self.size/2, "grey")
            elif self.noseSize == 'small' :
                dot(self.size/6, "grey")
            else :
                dot(self.size/4, "grey")
                self.goHome()
f1= face(0, 0)
f1.draw()
showturtle()
done
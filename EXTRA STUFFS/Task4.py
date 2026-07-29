import turtle
import math
import colorsys

class HeartAnimator:
    def __init__(self, num_lines: int = 180, scale: int = 15):
        self.num_lines = num_lines
        self.scale = scale
        
        self.screen = turtle.Screen()
        self.screen.bgcolor("#050505")
        self.screen.title("Clockwise Animated Heart")
        self.screen.setup(width=800, height=800)
        
        # tracer(1) ensures the animation plays frame-by-frame 
        # instead of rendering instantly.
        self.screen.tracer(1) 
        
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0) # 0 is the fastest drawing animation speed
        self.pen.pensize(1.2)

    def _get_heart_coordinates(self, angle: float) -> tuple[float, float]:
        x = 16 * (math.sin(angle) ** 3)
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        
        return x * self.scale, y * self.scale

    def draw_star(self, size: int):
        for _ in range(5):
            self.pen.forward(size)
            self.pen.backward(size)
            self.pen.right(72)

    def animate(self):
        # The loop runs from 0 to 2*PI. 
        # The math naturally draws the shape in a clockwise direction.
        for i in range(self.num_lines):
            angle = i * (math.pi * 2) / self.num_lines
            x, y = self._get_heart_coordinates(angle)
            
            # Calculates a smooth color gradient based on the current line
            hue = i / self.num_lines
            color = colorsys.hsv_to_rgb(hue, 0.85, 1.0)
            
            self.pen.penup()
            self.pen.goto(0, 30) # The center origin point for the strings
            self.pen.pendown()
            
            self.pen.color(color)
            self.pen.goto(x, y)
            
            self.draw_star(4)
            
        turtle.done()

if __name__ == "__main__":
    app = HeartAnimator()
    app.animate()
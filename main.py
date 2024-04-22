import tkinter as tk
import math

class TankGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()
        self.tank1 = self.draw_tank(100, 100, 0, 'blue')
        self.tank2 = self.draw_tank(500, 300, 0, 'red')
        self.setup_bindings()

    def draw_tank(self, x, y, angle, color):
        tank_body = self.canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill=color)
        turret_length = 20
        turret_end_x = x + turret_length * math.cos(angle)
        turret_end_y = y + turret_length * math.sin(angle)
        tank_turret = self.canvas.create_line(x, y, turret_end_x, turret_end_y, width=3, fill='black')
        return {'body': tank_body, 'turret': tank_turret, 'x': x, 'y': y, 'angle': angle}

    def move_tank(self, tank, dx, dy):
        self.canvas.move(tank['body'], dx, dy)
        self.canvas.move(tank['turret'], dx, dy)
        tank['x'] += dx
        tank['y'] += dy

    def rotate_tank(self, tank, da):
        tank['angle'] += da
        turret_length = 20
        turret_end_x = tank['x'] + turret_length * math.cos(tank['angle'])
        turret_end_y = tank['y'] + turret_length * math.sin(tank['angle'])
        self.canvas.coords(tank['turret'], tank['x'], tank['y'], turret_end_x, turret_end_y)

    def setup_bindings(self):
        self.root.bind("<KeyPress-w>", lambda e: self.move_tank(self.tank1, 0, -10))
        self.root.bind("<KeyPress-s>", lambda e: self.move_tank(self.tank1, 0, 10))
        self.root.bind("<KeyPress-a>", lambda e: self.rotate_tank(self.tank1, -0.1))
        self.root.bind("<KeyPress-d>", lambda e: self.rotate_tank(self.tank1, 0.1))

if __name__ == "__main__":
    root = tk.Tk()
    game = TankGame(root)
    root.mainloop()

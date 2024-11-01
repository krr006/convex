#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)

tk = TkDrawer()
tk.clean()
tr = Void()
print("Задайте координаты вершин треугольника")
for i in range(3):
    tr = tr.add(R2Point())
    tk.clean()
    tr.draw(tk)


f = Void()
print("\nЗадайте координаты вершин выпуклой оболочки")
try:
    ex = True
    while True:
        if (isinstance(f, Void | Point)):
            f = f.add(R2Point())
            tk.clean()
            f.draw(tk)
            tr.draw(tk)
        elif (isinstance(f, Segment)):
            print(f"Количество ребер, лежащих в треугольнике - {f.num(tr)}")
            tk.clean()
            tr.draw(tk)
            f.draw(tk)
            f = f.add(R2Point())
        else:
            if ex:
                f.three(tr)
                ex = False
            tk.clean()
            tr.draw(tk)
            f.draw(tk)
            print(f"S = {f.area()}, P = {f.perimeter()}\n")
            print(f"Количество ребер, лежащих в треугольнике равно {f.count}")
            f = f.add(R2Point(), tr)


except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()

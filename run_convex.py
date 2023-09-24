#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void, Point, Segment

tr = Void()
print("Задайте координаты вершин треугольника")
for i in range(3):
    tr = tr.add(R2Point())

print("\nЗадайте координаты вершин выпуклой оболочки")
f = Void()
try:
    ex = True
    while True:
        if (isinstance(f, Void | Point)):
            f = f.add(R2Point())
        elif (isinstance(f, Segment)):
            print(f"Количество ребер, лежащих в треугольнике - {f.num(tr)}")
            f = f.add(R2Point())
        else:
            if ex:
                f.three(tr)
                ex = False
            print(f"S = {f.area()}, P = {f.perimeter()}\n")
            print(f"Количество ребер, лежащих в треугольнике равно {f.count}")
            f = f.add(R2Point(), tr)
except (EOFError, KeyboardInterrupt):
    print("\nStop")

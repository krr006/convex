#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

tr = Void()
print("Задайте координаты вершин треугольника")
for i in range(3):
    tr = tr.add(R2Point())

print("\nЗадайте координаты вершин выпуклой оболочки")
f = Void()
try:
    с = 0
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print()
        с += 1
        if c >= 3:
            print(f"Количество ребер внутри треугольника равно {f.num(tr)}")
except (EOFError, KeyboardInterrupt):
    print("\nStop")

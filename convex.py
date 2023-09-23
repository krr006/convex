from deq import Deq
from r2point import R2Point
from vector import Vector


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def num(self, triangle):
        vertex1 = triangle.points.array[0]
        vertex2 = triangle.points.array[1]
        vertex3 = triangle.points.array[2]
        vec1 = Vector(vertex1, self.p)
        vec2 = Vector(vertex2, self.p)
        vec3 = Vector(vertex3, self.p)
        ex1 = vec1.dot(Vector(vertex1, vertex2))
        ex2 = vec2.dot(Vector(vertex2, vertex3))
        ex3 = vec3.dot(Vector(vertex3, vertex1))
        vec4 = Vector(vertex1, self.q)
        vec5 = Vector(vertex2, self.q)
        vec6 = Vector(vertex3, self.q)
        ex4 = vec4.dot(Vector(vertex1, vertex2))
        ex5 = vec5.dot(Vector(vertex2, vertex3))
        ex6 = vec6.dot(Vector(vertex3, vertex1))
        if (((ex1 >= 0 and ex2 >= 0 and ex3 >= 0) or
            (ex1 <= 0 and ex2 <= 0 and ex3 <= 0)) and
            ((ex4 >= 0 and ex5 >= 0 and ex6 >= 0) or
                (ex4 <= 0 and ex5 <= 0 and ex6 <= 0))):
            return 1
        return 0

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        # self.vertices = []
        self.count = 0
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t, triangle):
        # vertex1 = triangle.points.array[0]
        # vertex2 = triangle.points.array[1]
        # vertex3 = triangle.points.array[2]
        # # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                # vec1 = Vector(vertex1, p)
                # vec2 = Vector(vertex2, p)
                # vec3 = Vector(vertex3, p)
                # ex1 = vec1.dot(Vector(vertex1, vertex2))
                # ex2 = vec2.dot(Vector(vertex2, vertex3))
                # ex3 = vec3.dot(Vector(vertex3, vertex1))
                # vec4 = Vector(vertex1, self.points.first())
                # vec5 = Vector(vertex2, self.points.first())
                # vec6 = Vector(vertex3, self.points.first())
                # ex6 = vec6.dot(Vector(vertex3, vertex1))
                # ex4 = vec4.dot(Vector(vertex1, vertex2))
                # ex5 = vec5.dot(Vector(vertex2, vertex3))
                # if (((ex1 >= 0 and ex2 >= 0 and ex3 >= 0) or
                #     (ex1 <= 0 and ex2 <= 0 and ex3 <= 0)) and
                #     ((ex4 >= 0 and ex5 >= 0 and ex6 >= 0) or
                #         (ex4 <= 0 and ex5 <= 0 and ex6 <= 0))):
                #     self.count -= 1
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()

            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                # vec1 = Vector(vertex1, p)
                # vec2 = Vector(vertex2, p)
                # vec3 = Vector(vertex3, p)
                # ex1 = vec1.dot(Vector(vertex1, vertex2))
                # ex2 = vec2.dot(Vector(vertex2, vertex3))
                # ex3 = vec3.dot(Vector(vertex3, vertex1))
                # vec4 = Vector(vertex1, self.points.first())
                # vec5 = Vector(vertex2, self.points.first())
                # vec6 = Vector(vertex3, self.points.first())
                # ex6 = vec6.dot(Vector(vertex3, vertex1))
                # ex4 = vec4.dot(Vector(vertex1, vertex2))
                # ex5 = vec5.dot(Vector(vertex2, vertex3))
                # if (((ex1 >= 0 and ex2 >= 0 and ex3 >= 0) or
                #     (ex1 <= 0 and ex2 <= 0 and ex3 <= 0)) and
                #     ((ex4 >= 0 and ex5 >= 0 and ex6 >= 0) or
                #         (ex4 <= 0 and ex5 <= 0 and ex6 <= 0))):
                #     self.count -= 1
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            # vec1 = Vector(vertex1, t)
            # vec2 = Vector(vertex2, t)
            # vec3 = Vector(vertex3, t)
            # ex1 = vec1.dot(Vector(vertex1, vertex2))
            # ex2 = vec2.dot(Vector(vertex2, vertex3))
            # ex3 = vec3.dot(Vector(vertex3, vertex1))
            # vec4 = Vector(vertex1, self.points.first())
            # vec5 = Vector(vertex2, self.points.first())
            # vec6 = Vector(vertex3, self.points.first())
            # ex4 = vec4.dot(Vector(vertex1, vertex2))
            # ex5 = vec5.dot(Vector(vertex2, vertex3))
            # ex6 = vec6.dot(Vector(vertex3, vertex1))
            # if (((ex1 >= 0 and ex2 >= 0 and ex3 >= 0) or
            #     (ex1 <= 0 and ex2 <= 0 and ex3 <= 0)) and
            #     ((ex4 >= 0 and ex5 >= 0 and ex6 >= 0) or
            #         (ex4 <= 0 and ex5 <= 0 and ex6 <= 0))):
            #     self.count += 1
            # ex1 = vec1.dot(Vector(vertex1, vertex2))
            # ex2 = vec2.dot(Vector(vertex2, vertex3))
            # ex3 = vec3.dot(Vector(vertex3, vertex1))
            # vec4 = Vector(vertex1, self.points.last())
            # vec5 = Vector(vertex2, self.points.last())
            # vec6 = Vector(vertex3, self.points.last())
            # ex4 = vec4.dot(Vector(vertex1, vertex2))
            # ex5 = vec5.dot(Vector(vertex2, vertex3))
            # ex6 = vec6.dot(Vector(vertex3, vertex1))
            # if (((ex1 >= 0 and ex2 >= 0 and ex3 >= 0) or
            #     (ex1 <= 0 and ex2 <= 0 and ex3 <= 0)) and
            #     ((ex4 >= 0 and ex5 >= 0 and ex6 >= 0) or
            #         (ex4 <= 0 and ex5 <= 0 and ex6 <= 0))):
            #     self.count += 1
            self.points.push_first(t)
            # self.vertices.append(t)
        print(f"Количество ребер внутри треугольника равно {self.count}")
        return self

    def num(self, triangle):
        count = 0
        vertex1 = triangle.points.array[0]
        vertex2 = triangle.points.array[1]
        vertex3 = triangle.points.array[2]
        # Перебираем вершины выпуклой оболочки
        for i in range(self.points.size()):
            p1 = self.points.array[i]
            p2 = self.points.array[(i + 1) % self.points.size()]
            vec1 = Vector(vertex1, p1)
            vec2 = Vector(vertex2, p1)
            vec3 = Vector(vertex3, p1)
            ex1 = vec1.dot(Vector(vertex1, vertex2))
            ex2 = vec2.dot(Vector(vertex2, vertex3))
            ex3 = vec3.dot(Vector(vertex3, vertex1))
            vec4 = Vector(vertex1, p2)
            vec5 = Vector(vertex2, p2)
            vec6 = Vector(vertex3, p2)
            ex4 = vec4.dot(Vector(vertex1, vertex2))
            ex5 = vec5.dot(Vector(vertex2, vertex3))
            ex6 = vec6.dot(Vector(vertex3, vertex1))
            if (((ex1 >= 0 and ex2 >= 0 and ex3 >= 0) or
                (ex1 <= 0 and ex2 <= 0 and ex3 <= 0)) and
                ((ex4 >= 0 and ex5 >= 0 and ex6 >= 0) or
                    (ex4 <= 0 and ex5 <= 0 and ex6 <= 0))):
                count += 1

        return count


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)

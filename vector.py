class Vector:
    def __init__(self, beg, end):
        self.x = end.x - beg.x
        self.y = end.y - beg.y

    def dot(self, other):
        return self.x*other.y - other.x*self.y

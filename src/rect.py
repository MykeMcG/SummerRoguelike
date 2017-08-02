class Rect:
    # A rectangle used to represent rooms on the map
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersect(self, other):
        # Returns true if self intersects with other
        return (self.x1 <= other.x2 and self.x2 >= other.x1 
                and self.y1 <= other.y2 and self.y2 >= other.y1)

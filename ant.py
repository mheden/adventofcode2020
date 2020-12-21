from collections import namedtuple
import math


class Ant:
    """
                  N (90°)
                  ^ +y
                  |
                  |
    W (180°) <----+----> E (0°)
     -x           |    +x
                  |
                  v -y
                  S (0°)
    """

    def __init__(self, x, y, heading=0):
        self.heading = heading
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.path = [(self.x, self.y, self.heading)]

    def forward(self, dist):
        self.x += round(dist * math.cos(2 * math.pi * self.heading / 360.0))
        self.y += round(dist * math.sin(2 * math.pi * self.heading / 360.0))
        self.path.append((self.x, self.y, self.heading))

    def backward(self, dist):
        self.x -= round(dist * math.cos(2 * math.pi * self.heading / 360.0))
        self.y -= round(dist * math.sin(2 * math.pi * self.heading / 360.0))
        self.path.append((self.x, self.y, self.heading))

    def turn(self, degrees):
        self.heading = (self.heading + degrees) % 360

    def north(self, dist):
        self.y += dist
        self.path.append((self.x, self.y, self.heading))

    def south(self, dist):
        self.y -= dist
        self.path.append((self.x, self.y, self.heading))

    def east(self, dist):
        self.x += dist
        self.path.append((self.x, self.y, self.heading))

    def west(self, dist):
        self.x -= dist
        self.path.append((self.x, self.y, self.heading))

    def pos(self):
        return (self.x, self.y)

    def dist(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        return (360 * math.atan2(self.y, self.x) / (2 * math.pi) + 360) % 360

    def __str__(self):
        return "Ant(%d, %d, %d)" % (self.x, self.y, self.heading)


if __name__ == "__main__":
    ant = Ant(0, 0, heading=0)

    # movement
    ant.forward(10)
    assert ant.x == 10
    assert ant.y == 0
    assert ant.heading == 0
    ant.north(20)
    assert ant.x == 10
    assert ant.y == 20
    assert ant.heading == 0
    ant.backward(20)
    assert ant.x == -10
    assert ant.y == 20
    assert ant.heading == 0
    ant.turn(90)
    assert ant.x == -10
    assert ant.y == 20
    assert ant.heading == 90
    ant.forward(10)
    assert ant.x == -10
    assert ant.y == 30
    assert ant.heading == 90
    ant.backward(5)
    assert ant.x == -10
    assert ant.y == 25
    assert ant.heading == 90
    ant.turn(180)
    assert ant.x == -10
    assert ant.y == 25
    assert ant.heading == 270
    ant.forward(25)
    assert ant.x == -10
    assert ant.y == 0
    assert ant.heading == 270
    ant.east(10)
    assert ant.x == 0
    assert ant.y == 0
    assert ant.heading == 270
    assert ant.path == [
        (0, 0, 0),
        (10, 0, 0),
        (10, 20, 0),
        (-10, 20, 0),
        (-10, 30, 90),
        (-10, 25, 90),
        (-10, 0, 270),
        (0, 0, 270),
    ]
    ant.move(10, 10)
    assert ant.x == 10
    assert ant.y == 10
    assert ant.heading == 270
    ant.forward(10)
    assert ant.path == [(10, 10, 270), (10, 0, 270)]

    # angle
    ant.x = 5
    ant.y = 5
    assert ant.angle() == 45
    ant.x = -5
    ant.y = 5
    assert ant.angle() == 135
    ant.x = -5
    ant.y = -5
    assert ant.angle() == 225
    ant.x = 5
    ant.y = -5
    assert ant.angle() == 315

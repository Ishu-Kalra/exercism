# Globals for the bearings
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4
left = [WEST, SOUTH, EAST, NORTH]
right = [EAST, SOUTH, WEST, NORTH]

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_left(self):
        for direction in range(0, 4):
            if left[direction] == self.bearing:
                if direction != 3:
                    self.bearing = left[direction + 1]
                    break
                else:
                    self.bearing = left[0]
        return self.bearing

    def turn_right(self):
        for direction in range(0, 4):
            if right[direction] == self.bearing:
                if direction != 3:
                    self.bearing = right[direction + 1]
                    break
                else:
                    self.bearing = right[0]
        return self.bearing

    def advance(self):
        x,y = self.coordinates
        #print(str(x) + " and " + str(y))
        if self.bearing == NORTH:
            y += 1
        if self.bearing == SOUTH:
            y -= 1
        if self.bearing == EAST:
            x += 1
        if self.bearing == WEST:
            x -= 1
        self.coordinates = (x, y)

    def simulate(self, string):
        for char in string:
            if char.upper() == 'R':
                self.turn_right()
            if char.upper() == 'L':
                self.turn_left()
            if char.upper() == 'A':
                self.advance()

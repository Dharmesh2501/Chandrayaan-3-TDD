class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.position = (x, y, z)
        self.direction = direction

    def move_forward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y + 1, z)
        elif self.direction == 'S':
            self.position = (x, y - 1, z)
        elif self.direction == 'E':
            self.position = (x + 1, y, z)
        elif self.direction == 'W':
            self.position = (x - 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z + 1)
        elif self.direction == 'Down':
            self.position = (x, y, z - 1)

    def move_backward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y - 1, z)
        elif self.direction == 'S':
            self.position = (x, y + 1, z)
        elif self.direction == 'E':
            self.position = (x - 1, y, z)
        elif self.direction == 'W':
            self.position = (x + 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z - 1)
        elif self.direction == 'Down':
            self.position = (x, y, z + 1)



    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            
          


# Example usage
starting_position = (0, 0, 0)
initial_direction = 'N'
commands = ["f", "r"]
chandrayaan_3 = Spacecraft(*starting_position, initial_direction)
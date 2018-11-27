class Car:
    def __init__(self, current_position):
        self.current_position = current_position
        self.path = [current_position]

    def move(self,new_position):
        self.path.append(new_position)
        self.current_position = new_position


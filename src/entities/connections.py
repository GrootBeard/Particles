from entities.particles import Entity

class Connection(Entity):

    def __init__(self):
        self.p1 = None
        self.p2 = None

    def connect(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def disconnect(self):
        self.p1 = None
        self.p2 = None

    def update(self):
        pass


class Spring(Connection):

    def __init__(self, constant, rest_length, p1, p2):
        super().__init__()
        self.spring_constant = constant
        self.rest_length = rest_length
        self.connect(p1, p2)

    def update(self):
        dist_vec = self.p1.position - self.p2.position
        stretch = dist_vec.len() - self.rest_length
        # print("stretch: {0}".format(stretch))
        self.p1.apply_force(-dist_vec.unit() * stretch * self.spring_constant)
        self.p2.apply_force(dist_vec.unit() * stretch * self.spring_constant)

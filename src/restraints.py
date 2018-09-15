class Spring(object):

    def __init__(self, constant, rest_length, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.spring_constant = constant
        self.rest_length = rest_length

    def update(self):
        dist_vec = self.p1.position - self.p2.position
        stretch = dist_vec.len() - self.rest_length
        self.p1.apply_force(-dist_vec.norm() * stretch * self.spring_constant)
        self.p2.apply_force(dist_vec.norm() * stretch * self.spring_constant)
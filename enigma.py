class Enigma:

    def __init__(self, n_rotors, order, rotor, pairs, initial_position):
        self.n_rotors = n_rotors
        if n_rotors == 0:
            raise AssertionError
        self.order = order
        if not isinstance(self.order, list) or len(order) != n_rotors:
            raise AssertionError
        for i in range(len(order)):
            self.order[i] -= 1
        self.rotor = rotor
        if not isinstance(self.rotor, list) or len(rotor) != n_rotors:
            raise AssertionError
        self.next = dict()
        self.build_next(pairs)
        self.move_to_initial_position(initial_position)
        self.first_rotation = 0

    def rotate(self, idx):
        self.rotor[idx] = self.rotor[idx][-1] + self.rotor[idx][:-1]

    def move_to_initial_position(self, initial_position):
        for idx in range(len(initial_position)):
            pos = self.rotor[self.order[idx]].find(initial_position[idx])
            for i in range(25 - pos):
                self.rotate(self.order[idx])

    def build_next(self, pairs):
        for e in pairs:
            self.next[e[0]] = e[1]
            self.next[e[1]] = e[0]

    def transform(self, key, rotor_id, left=True):
        if left:
            return self.rotor[self.order[rotor_id]][ord(key) - ord('A')]
        return chr(self.rotor[self.order[rotor_id]].find(key) + ord('A'))

    @staticmethod
    def reflect(key):
        key = ord(key) - ord('A')
        key = (key + 1) % 26
        key = key + ord('A')
        return chr(key)

    def rotate_all(self):
        pot = [1]
        for i in range(self.n_rotors - 1):
            pot += [pot[i] * 26]
        self.first_rotation += 1
        for i in range(self.n_rotors):
            if self.first_rotation % pot[i] == 0:
                self.rotate(self.order[i])

    def press(self, key):
        if key in self.next:
            key = self.next[key]
        for i in range(self.n_rotors):
            key = self.transform(key, i)
        key = self.reflect(key)
        for i in reversed(range(self.n_rotors)):
            key = self.transform(key, i, left=False)
        if key in self.next:
            key = self.next[key]
        self.rotate_all()
        return key

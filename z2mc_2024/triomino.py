from core.traversal import predicate_finder


class TriominoPiece:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f'TriominoPiece({self.x}, {self.y}, {self.z})'
    def __eq__(self, other):
        if isinstance(other, TriominoPiece):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False
    def __hash__(self):
        return hash((self.x, self.y, self.z))

class TriominoGenerator:
    def __init__(self, max):
        self.max = max

    def roots(self):
        return [TriominoPiece(0, 0, 0)]

    def neighbors(self, source):
        x = source.x
        y = source.y
        z = source.z
        neighbors = []
        nx = (x + 1) % self.max
        if nx <= y :
            neighbors.append(TriominoPiece(nx, y, z))
        ny = (y + 1) % self.max
        if x <= ny <= z:
            neighbors.append(TriominoPiece(x, ny, z))
        nz = (z + 1) % self.max
        if nz >= y :
            neighbors.append(TriominoPiece(x, y, nz))
        return neighbors

if __name__ == '__main__':
    t = TriominoGenerator(6)
    x, pieces = predicate_finder(t, lambda n: False)
    print('# piece = ', len(pieces))
    print(*pieces, sep='\n')
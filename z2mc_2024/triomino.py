from core.traversal import predicate_finder


class TriominoPiece:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def create(x, y, z, rotation = 0):
        return RotatedTriominoPiece(TriominoPiece(x, y, z), rotation)

    def point(self, idx):
        if idx == 0: return self.x
        if idx == 1: return self.y
        if idx == 2: return self.z
        return None
    def edge(self, idx):
        if idx == 0: return self.x, self.y
        if idx == 1: return self.y, self.z
        if idx == 2: return self.z, self.x
        return None

    def __repr__(self):
        return f'TriominoPiece({self.x}, {self.y}, {self.z})'
    def __eq__(self, other):
        if isinstance(other, TriominoPiece):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False
    def __hash__(self):
        return hash((self.x, self.y, self.z))


class RotatedTriominoPiece:
    def __init__(self, piece, rotation):
        self.piece = piece
        if piece.x == piece.y == piece.z:
            self.rotation = 0
        else:
            self.rotation = rotation # 0 = 0°, 1 = 120°, 2 = 240°

    def point(self, idx):
        if self.rotation == 0: return self.piece.point(idx)
        if self.rotation == 1: return self.piece.point((idx+1) % 3)
        if self.rotation == 2: return self.piece.point((idx+2) % 3)
        return None

    def edge(self, idx):
        if self.rotation == 0: return self.piece.edge(idx)
        if self.rotation == 1: return self.piece.edge((idx+1) % 3)
        if self.rotation == 2: return self.piece.edge((idx+2) % 3)
        return None

    def rotate(self):
        if self.piece.x == self.piece.y == self.piece.z:
            return
        self.rotation = (self.rotation + 1) % 3

    def __repr__(self):
        return f'RotatedTriominoPiece({self.piece}, {self.rotation})'
    def __eq__(self, other):
        if isinstance(other, RotatedTriominoPiece):
            return self.piece == other.piece and self.rotation == other.rotation
        return False
    def __hash__(self):
        return hash((self.piece, self.rotation))

class TriominoPosition:
    def __init__(self, ax, ay, az, piece):
        self.ax = ax
        self.ay = ay
        self.az = az
        self.piece = piece

    @staticmethod
    def empty():
        return TriominoPosition((None, -1), (None, -1), (None, -1), None)

    def axis(self, idx):
        if idx == 0: return self.ax
        if idx == 1: return self.ay
        if idx == 2: return self.az
        return None

    def check_axis(self, axis):
        (rp, p), (re, e) = self.axis(axis)
        if rp is not None and rp.piece.point(p) != self.piece.point(axis):
            return False
        if re is not None and re.piece.edge(e) != self.piece.edge((axis + 1) % 3):
            return False
        return True

    def check(self):
        if self.piece is not None:
            return (    not ( self.ax[0] is None and self.ay[0] is None and self.az[0] is None )
                    and self.check_axis(0)
                    and self.check_axis(1)
                    and self.check_axis(2))
        return True

    def set_piece(self, piece):
        if self.piece is not None or piece is None:
            return
        self.piece = piece


    def __eq__(self, other):
        if not isinstance(other, TriominoPosition):
            return False
        return (self.piece == other.piece) and (self.ax == other.ax) and (self.ay == other.ay) and (self.az == other.az)

    def __hash__(self):
        return hash((self.piece, self.ax, self.ay, self.az))

    def __repr__(self):
        return f'TriominoPosition({self.piece} ax:{self.ax} ay:{self.ay} az:{self.az})'

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

class TriominoConfiguration:
    def __init__(self):
        self.empty_positions = [TriominoPosition.empty()]
        self.positions = []
        self.hand = [TriominoPiece(0, 0, 0)]
        self.well = [TriominoPiece(0, 0, 1)]

    def __repr__(self):
        return (f' '
                f'-empty-positions: {self.empty_positions} \n '
                f'-positions: {self.positions} \n '
                f'-hand: {self.hand} \n '
                f'-well: {self.well}')

class Triomino:

    def initial(self):
        return []
    def actions(self, c):
        return []
    def execute(self, a, c):
        return []

if __name__ == '__main__':
    t = TriominoGenerator(6)
    xx, pieces = predicate_finder(t, lambda n: False)
    print('# piece = ', len(pieces))
    print(*pieces, sep='\n')
    p = TriominoPosition.empty()
    print( p.check())

    p.piece = RotatedTriominoPiece(TriominoPiece(0, 0, 0), 0)
    print( p.check() )

    rpx = RotatedTriominoPiece(TriominoPiece(0, 0, 0), 1)
    print (f'rotation {rpx.rotation}')

    c = TriominoConfiguration()
    print (c)

    c.empty_positions[0].set_piece(p.piece)
    print(c)

    print (-1 % 3)


import numpy as np

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'{self.x, self.y}'


def convexHull(coordinates, ver2=True):
    points = []
    for x, y in coordinates:
        points.append(Point(x, y))

    p = min(points, key=lambda p: p.x)
    convexHullVertices = []

    while True:
        convexHullVertices.append(p)
        pIdx = points.index(p)
        try:
            q = points[pIdx + 1]
        except:
            q = points[pIdx - 1]

        for r in points:
            if r == p or r == q:
                continue
            pqrVal = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
            prqVal = (r.y - p.y) * (q.x - r.x) - (q.y - r.y) * (r.x - p.x)
            dr = np.sqrt((p.x - r.x)**2 + (p.y - r.y)**2)
            dq = np.sqrt((p.x - q.x)**2 + (p.y - q.y)**2)
            if pqrVal < 0 or (pqrVal == 0 and dr > dq and ver2):  # gdy lewoskrętne
                q = r
        p = q
        if p == min(points, key=lambda p: p.x):
            break

    return convexHullVertices


def main():
    print('Wyniki dla wersji pierwszej:')
    coords1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    convexHullVertices = convexHull(coords1, ver2=False)
    print(convexHullVertices)

    coords2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    convexHullVertices = convexHull(coords2, ver2=False)
    print(convexHullVertices)

    coords3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    convexHullVertices = convexHull(coords3, ver2=False)
    print(convexHullVertices)

    print('\nWyniki dla wersji drugiej:')
    convexHullVertices = convexHull(coords1)
    print(convexHullVertices)

    convexHullVertices = convexHull(coords2)
    print(convexHullVertices)

    convexHullVertices = convexHull(coords3)
    print(convexHullVertices)



if __name__ == '__main__':
    main()
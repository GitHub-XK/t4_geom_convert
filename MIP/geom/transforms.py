# Return dictionary describing transformations
from collections import OrderedDict
from math import cos, radians


def to_cos(a):
    return cos(radians(a))


def normalize_transform(name, dtype, params):
    """
    return complete list of paramters for the tr card.
    """
    name = int(name)
    pl = list(map(float, params.split()))
    if len(pl) == 3:
        # no rotational matrix is given. Use the identical one
        dtype = dtype.replace('*', '')
        pl = pl + [1, 0, 0, 0, 1, 0, 0, 0, 1]
    if dtype[0] == '*':
        pl[3:] = list(map(to_cos, pl[3:]))
    return name, pl


def get_transforms(input, lim=None):
    """
    input is an instance of mpi.MIP class.
    """
    d = OrderedDict()
    n = 0
    for c in input.cards(blocks='d', skipcomments=True):
        name, dtype, params = c.parts()
        if dtype.lower() in ('tr', '*tr'):
            name, params = normalize_transform(name, dtype, params)
            d[name] = params
            n += 1
            if lim and n > lim:
                break
    return d


def transform_vector(v, tr):
    b1, b2, b3, b4, b5, b6, b7, b8, b9 = tr[3:]
    x, y, z = v
    xp = b1*x + b4*y + b7*z
    yp = b2*x + b5*y + b8*z
    zp = b3*x + b6*y + b9*z
    return xp, yp, zp


def transform_point(p, tr):
    v = transform_vector(p, tr)
    ox, oy, oz = tr[:3]
    xp = ox + v[0]
    yp = oy + v[1]
    zp = oz + v[2]
    return xp, yp, zp


if __name__ == '__main__':
    from .main import get_raw_geom
    from sys import argv

    cd, sd, td = get_raw_geom(argv[1])

    for k, v in list(sd.items()):
        bc, tr, st, pl = v
        if tr:
            print(k, v)

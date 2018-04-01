import numpy as np


def l2(mat1, mat2):
    return np.sqrt(np.sum((mat1 - mat2)**2))

def uniform_locations(screen_size, location_size, object_radius,
                      normalize=False):
    x = np.linspace(object_radius, screen_size-object_radius, location_size)
    grid = np.meshgrid(x, x)
    out = np.array(zip(*np.vstack(map(np.ravel, grid))))
    if normalize:
        div = location_size**2 / 2
        out = (out - div) / div
    return out

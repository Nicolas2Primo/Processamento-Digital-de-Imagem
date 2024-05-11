def gaussianKernel(h1, h2, sigma=1):
    import numpy as np
    h1_half = h1 / 2
    h2_half = h2 / 2
    sigma_sq = 2 * sigma**2

    x = np.arange(0, h1) - h1_half
    y = np.arange(0, h2) - h2_half
    X, Y = np.meshgrid(x, y)

    g = np.exp(-(X**2 + Y**2) / sigma_sq)

    return g / g.sum()
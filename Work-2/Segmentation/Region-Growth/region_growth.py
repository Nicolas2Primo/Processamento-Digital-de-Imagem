import numpy as np

def region_growing(image, seed, threshold):
    height, width = image.shape
    binary_image = np.zeros_like(image)
    pixels_to_check = [seed]

    # Verifica se a semente está dentro dos limites da imagem
    seed_i, seed_j = seed
    if not (0 <= seed_i < height and 0 <= seed_j < width):
        raise ValueError("Seed coordinates are out of bounds")

    while pixels_to_check:
        current_pixel = pixels_to_check.pop(0)
        current_i, current_j = current_pixel

        if binary_image[current_i, current_j] == 1:
            continue

        if image[current_i, current_j] <= threshold:
            binary_image[current_i, current_j] = 1

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    neighbor_i = current_i + di
                    neighbor_j = current_j + dj

                    # Tratamento de bordas aprimorado
                    if 0 <= neighbor_i < height and 0 <= neighbor_j < width:
                        pixels_to_check.append((neighbor_i, neighbor_j))
    
    return binary_image

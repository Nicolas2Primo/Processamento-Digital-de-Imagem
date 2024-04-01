import numpy as np
import matplotlib.pyplot as plt
import math as m

class LaplacianFilter:
    def __init__(self, img, kernel_type='lk1', kernel_size=3):
        self.img = np.array(img)
        self.original = self.img
        self.img_size_lin, self.img_size_col, *_ = self.img.shape
        self.kernel_size = kernel_size
        self.kernel_type = kernel_type
        self.kernel = self._generate_kernel(kernel_type, kernel_size)
        self.central = m.floor((kernel_size / 2))
        self.padding = np.zeros((self.img_size_lin + self.central * 2, self.img_size_col + self.central * 2))

    def _generate_kernel(self, kernel_type, kernel_size):
        if kernel_type == 'lk1':
            kernel = np.ones((kernel_size, kernel_size))
            kernel[int(kernel_size/2), int(kernel_size/2)] = -1 * (np.sum(kernel) - 1)
        elif kernel_type == 'lk2':
            kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        else:
            raise ValueError("Invalid kernel type. Choose 'standard' or 'enhanced'.")
        return kernel

    def _filter(self):
        self.padding[(0 + self.central):(self.img_size_lin + self.central), (0 + self.central):(self.img_size_col + self.central)] = self.img.copy()
        final_array = np.zeros(self.img.shape)
        sum = 0
        for j in range(0, self.img_size_lin):
            for k in range(0, self.img_size_col):
                for kl in range(0, self.kernel_size):
                    for kk in range(0, self.kernel_size):
                        sum = (self.padding[j + kl, k + kk] * self.kernel[kl, kk]) + sum

                value = m.ceil((sum / (self.kernel_size * self.kernel_size)))
                sum = 0
                final_array[j, k] = value

        final_array = np.uint8(final_array)
        print("FINISHED")
        return final_array

    def run_test(self, num_increments):
        original = self.original
        aux = np.zeros((self.img_size_lin, self.img_size_col))
        auxs = [original]
        plt.imshow(original, 'gray')
        plt.title('Original')
        plt.show()
        print(self.kernel)

        for i in range(num_increments):
            aux = self._filter()
            auxs.append(aux.copy())
            self.img = aux.copy()

        plt.imshow(aux, 'gray')
        plt.title(f'Filtered - Iteration {i + 1}')
        plt.show()
        #cv2.imwrite(f'filtered_laplacian_image_k{self.kernel_size}_n{num_increments}_-8.png',aux)
        self.img = original.copy()

import numpy as np
import matplotlib.pyplot as plt
import math as m

class PrewitFilter:
    def __init__(self, img, kernel_size):
        self.img = np.array(img)
        self.original = self.img
        self.img_size_lin, self.img_size_col, *_ = self.img.shape
        self.kernel_size = kernel_size
        self.kernel_horz, self.kernel_vert = self._generate_prewit_kernel(kernel_size)
        self.central = m.floor((kernel_size / 2))
        self.padding = np.zeros((self.img_size_lin + self.central * 2, self.img_size_col + self.central * 2))

    def _generate_prewit_kernel(self, size):
        kernel_horz = np.zeros((size, size))
        kernel_horz[:, 0] = -1
        kernel_horz[:, -1] = 1

        kernel_vert = np.zeros((size, size))
        kernel_vert[0, :] = -1
        kernel_vert[-1, :] = 1

        return kernel_horz, kernel_vert

    def _filter(self):
        self.padding[(0 + self.central):(self.img_size_lin + self.central), (0 + self.central):(self.img_size_col + self.central)] = self.img.copy()
        final_array = np.zeros(self.img.shape)
        sum_horz = 0
        sum_vert = 0
        for j in range(0, self.img_size_lin):
            for k in range(0, self.img_size_col):
                for kl in range(0, self.kernel_size):
                    for kk in range(0, self.kernel_size):
                        sum_horz = (self.padding[j + kl, k + kk] * self.kernel_horz[kl, kk]) + sum_horz
                        sum_vert = (self.padding[j + kl, k + kk] * self.kernel_vert[kl, kk]) + sum_vert

                Ph = m.ceil((sum_horz / (self.kernel_size ** 2)))
                Pv = m.ceil((sum_vert / (self.kernel_size ** 2)))
                sum_horz = 0
                sum_vert = 0
                final_array[j, k] = np.sqrt( Ph**2 + Pv**2)

        final_array = np.uint8(final_array)
        print("FINISHED")
        return final_array

    def run_test(self, num_increments):
        original = self.original
        aux = np.zeros((self.img_size_lin, self.img_size_col))
        auxs = [original]
       # print(original)
        plt.imshow(original, 'gray')
        plt.title('Original')
        plt.show()

        for i in range(num_increments):
            aux[:, :] = self._filter()
            #print(f"{i}\n", aux)
            auxs.append(aux.copy())
            self.img = aux.copy()

        plt.imshow(aux, 'gray')
        plt.title(f'Filtered - Iteration {i + 1}')
        plt.show()
        #cv2.imwrite(f'filtered_prewitt_image_k{self.kernel_size}_n{num_increments}.png',aux)
        self.img = original.copy()
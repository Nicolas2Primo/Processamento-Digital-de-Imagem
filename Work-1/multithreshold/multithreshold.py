import numpy as np
import matplotlib.pyplot as plt

class MultiThresholding:
    def __init__(self, img, multi_thresholds, multi_range):
        self.img = img
        self.multi_thresholds = multi_thresholds
        self.multi_range = multi_range

    def apply_multi_threshold(self):
        A = self.img
        D = np.zeros(A.shape)

        if len(self.multi_thresholds) == 2:
            T1, T2 = self.multi_thresholds
            Gmin = 0
            Gmed = self.multi_range[0]
            Gmax = 255

        elif len(self.multi_thresholds) == 3:
            T1, T2, T3 = self.multi_thresholds
            Gmin = 0
            Gmed1, Gmed2 = self.multi_range
            Gmax = 255

        for j in range(A.shape[0]):
            for k in range(A.shape[1]):
                if len(self.multi_thresholds) == 3:
                    if A[j, k] > T3:
                        D[j, k] = Gmax
                    elif A[j,k] <= T3 and A[j, k] > T2:
                        D[j, k] = Gmed2
                    elif A[j, k] <= T2 and A[j, k] > T1:
                        D[j, k] = Gmed1
                    elif A[j,k] <= T1:
                        D[j, k] = Gmin

                elif len(self.multi_thresholds) == 2:
                    if A[j, k] > T2:
                        D[j, k] = Gmax
                    elif A[j,k] <= T2 and A[j, k] > T1:
                        D[j, k] = Gmed
                    elif A[j,k] <= T1:
                        D[j, k] = Gmin

        D = np.uint8(D)

        print('################################')
        print('Processo finalizado')
        print('Multilimiar foi aplicado')
        print('################################')

        return D

    def apply_and_plot(self, num_iterations):
        U = np.zeros((num_iterations, self.img.shape[0], self.img.shape[1]))

        for k in range(num_iterations):
            if k == 0:
                U[k,:,:] = self.apply_multi_threshold()
            else:
                self.img = U[k-1,:,:]
                U[k, :, :] = self.apply_multi_threshold()

        plt.imshow(U[(num_iterations - 1),:,:], 'gray')
        plt.title('Img após limearização em %d e %d ' % (self.multi_thresholds[0], self.multi_thresholds[1]))
        plt.show()
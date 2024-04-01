import numpy as np
import matplotlib.pyplot as plt

class Thresholding:
    def __init__(self, img, threshold):
        self.img = img
        self.threshold = threshold

    def apply_threshold(self):
        img_min = np.min(self.img)
        img_max = np.max(self.img)
        thresholded_img = np.zeros_like(self.img)

        for j in range(self.img.shape[0]):
            for k in range(self.img.shape[1]):
                if self.img[j, k] > self.threshold:
                    thresholded_img[j, k] = img_max
                else:
                    thresholded_img[j, k] = img_min

        thresholded_img = np.uint8(thresholded_img)

        print('################################')
        print('Processo finalizado')
        print('Limiar foi aplicado')
        print('################################')

        return thresholded_img

    def apply_and_plot(self, num_iterations):
        U = np.zeros((num_iterations, self.img.shape[0], self.img.shape[1]))

        for k in range(num_iterations):
            if k == 0:
                U[k,:,:] = self.apply_threshold()
            else:
                self.img = U[k-1,:,:]
                U[k, :, :] = self.apply_threshold()

        plt.imshow(U[(num_iterations - 1),:,:], 'gray')
        plt.title('Img após limiarização em intensidade %d ' %self.threshold)
        plt.show()
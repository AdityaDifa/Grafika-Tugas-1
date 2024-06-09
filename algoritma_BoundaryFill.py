import numpy


class BoundaryFill:

    def boundary_fill(self,image,x,y,color):

        boundary_color = 0 # Warna batas (misalnya hitam)

        #jika input x dan y nya diluar batas
        if x < 0 or x >= image.shape[0] or y < 0 or y >= image.shape[1]:
            return image

        # Cek warna piksel saat ini
        current_color = image[y, x]

        # Jika warna piksel saat ini sama dengan warna batas, isi dengan warna yang diberikan
        if current_color == boundary_color:
            image[y, x] = color

            # Lakukan boundary fill secara rekursif untuk piksel di sekitarnya
            self.boundary_fill(image, x + 1, y, color)
            self.boundary_fill(image, x - 1, y, color)
            self.boundary_fill(image, x, y + 1, color)
            self.boundary_fill(image, x, y - 1, color)

        return image
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\Hamza\\pisa.jpg")
#Görüntü elde edildi

histogram = [0] * 256
# Histogramı hesaplamak için boş bir liste oluşturdum


# Görüntüyü dolaşarak histogramı hesaplamak için çift for döngüsü kullanıyorum
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        piksel_degeri = img[i, j, 0] 
        histogram[piksel_degeri] += 1

#Histogramı grafiğe aktarıyoruz
plt.bar(range(256), histogram,)
plt.xlim([0, 255])
plt.show()

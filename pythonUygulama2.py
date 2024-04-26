points = [(2,5), (5,7) , (1,1) , (6,2)]

import math
#Öklit mesafesi için kullanılan formülün programa yazılması. Bunun için math kütüphanesinden faydalanıldı.
def euclideanDistance(point1 , point2) :
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

#Döngüden cıkacak olan değerlerin içine aktarılacağı liste
distance = []

#for föngüsü kullanarak point içinde bulunan değer sayısı kadar işlem yapıalcağı belirtir.
# İçeride kullanılan ikinci for döngüsü i değerinden 1 fazla olarak alınmıştır. Aynı değerlerin tekrardan hesaplanmasından kaçınmak için yapılmıştır.
for i in range(len(points)):
    for j in range(i+1 , len(points)):
        result = euclideanDistance(points[i], points[j])
        distance.append(result)


print(distance)

min = min(distance)

print(f" En kısa mesafe {min} dir.")

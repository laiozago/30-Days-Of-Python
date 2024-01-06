import math
cat_1 = float(input('Cateto mede: '))
cat_2 = float(input('O outro cateto mede: '))
hip = math.hypot(cat_1,cat_2)

print('A medida da hipotenusa é {:.2f}'.format(hip))
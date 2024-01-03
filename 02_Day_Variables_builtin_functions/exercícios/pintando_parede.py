largura = float(input('Qual a largura da parede, em metros? '))
altura = float(input('Qual a altura da parede, em metros? '))

area = largura*altura
tinta = area/2

print('Sua parede tem {:.2f} m de largura por {:.2f} m de altura. A área total da parede é {:.2f} m² e você vai precisar de {:.2f} litros de tinta.'.format(largura,altura,area,tinta))
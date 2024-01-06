import math
import calculus
ang = float(input('Qual o ângulo '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('O ângulo {}° tem \n sen = {} \n cos = {} \n tg = {}'.format(ang,sen,cos,tg))
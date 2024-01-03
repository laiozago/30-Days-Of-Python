#função para calcular a media entre duas notas
def calculadore_de_media(a,b):
    media = (a+b)/2
    print('A média entre {} e {} é {:.1f}'.format(nota_1,nota_2,media)) #ATENÇÃO a forma de concatenar str e variaveis

nota_1 = float(input('primeira nota: '))
nota_2 = float(input('segunda nota: '))

calculadore_de_media(nota_1,nota_2)
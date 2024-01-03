def conversor_de_medidas(dist):
    km = dist / 1000
    hm = dist / 100
    dam = dist / 10
    dm = dist * 10
    cm = dist * 100
    mm = dist * 1000
    print('Quilômetros:', km)
    print('Hectômetros:', hm)
    print('Decâmetros:', dam)
    print('Metros:', dist)
    print('Decímetros:', dm)
    print('Centímetros:', cm)
    print('Milímetros:', mm)

distancia = float(input('Entre com a distância em metros: '))

conversor_de_medidas(distancia)

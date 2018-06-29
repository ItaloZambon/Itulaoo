verbo = input('Digite um verbo: ')
conjugar = ['o','a','as','amos','ais','am']
final = verbo[:-2]
for i in range(0,6):
    print(final+conjugar[i])
from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' *20)
print('Vou pensar em um numero de 0 a 5. Tente advinhar...')
print('-=-' *20)
jogador = int(input('Em que numero eu pensei?: '))
print('Processando...')
sleep(3)
if jogador == computador:
	print('PARABENS! vc conseguiu me vencer!!')
else:
	print('GANHEI!! Eu pensei no numero {} e nao no {}'.format(computador, jogador))
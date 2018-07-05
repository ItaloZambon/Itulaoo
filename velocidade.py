# -*- coding: utf-8 -*-
velo = float(input('Qual a velocidade do carro ? '))
if velo > 80:
	print('MULTADOOO!! vc passou do limite de velocidade >:( ')
	multa = (velo-80) * 7
	print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
else:
	print('Tenha um bom dia e dirija com segurança :) ')
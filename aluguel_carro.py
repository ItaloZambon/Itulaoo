# -*- coding: utf-8 -*-
dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos km rodados: '))
pago = dias * 60 + km * 0.15
print('Conforme os dias alugados e os km rodados o alguel ficará em: {}R$'.format(pago))
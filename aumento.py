# -*- coding: utf-8 -*-
valor_S = float(input('Digite o salario do contratado: '))
valor_de_Aumento = int(input('Digite a porcentagem do aumento: '))
conta_no_aumento = valor_S * valor_de_Aumento / 100
novo = conta_no_aumento + valor_S
print( 'O trabalhador seu deu bem em sua area com isso ele receberá {}% de aumento, o seu salario de {} ficou {}'.format(valor_de_Aumento, valor_S, novo))


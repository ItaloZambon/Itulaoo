# -*- coding: utf-8 -*-
larg = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
tinta = area / 2 
print(u'A parede contém {}x{} a sua áreia é de {} e precisará de {}l de tinta para pinta-la.'.format(larg, alt, area, tinta))
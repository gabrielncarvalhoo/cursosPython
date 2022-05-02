altura = float(input('Altura da parede em metros: '))
largura = float(input('Largura da parede em metros: '))
m2 = altura * largura
tinta = m2 / 2
print('Sua Parede tem dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de '
      'tinta.'.format(largura, altura, m2, tinta))
5
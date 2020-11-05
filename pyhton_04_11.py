def jogar():
  estilo_espada = input('Escolha seu estilo de espada entre medieval e futurista. Digite medieval e futurista ') .strip().lower() #.strip() serve para retirar os espaços da respota.
  if estilo_espada == 'medieval':
    print('Você revebeu uma espada!')
  elif estilo_espada == 'futurista':
    print('Você recebeu um Sabre de luz')
  else:
    print('Tente Novamente')
jogar()

animais = 'catdogfrog'
cat = animais[0:3]
dog = animais[3:6]
frog = animais [-4:]

print(cat,dog,frog)

lista = [3, 2, 4, 5, 8, 7]

for numero in lista:
  dobro = numero * 2  
  if dobro >= 5 and dobro <=10:
    print(dobro)

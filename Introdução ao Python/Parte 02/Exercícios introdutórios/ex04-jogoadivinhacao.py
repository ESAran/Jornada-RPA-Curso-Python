import random

def num_aleatorio():
  num = random.randint(0, 100)
  return num

def num_verifica(num):
  jogada = int(input("Faça sua tentativa com um número entre 0-100: "))

  if jogada == num:
    return 0
  elif jogada < num:
    return -1
  else:
    return 1



sorteado = num_aleatorio()
tentativas = 10
print("")
print("SUPER ULTRA MEGA JOGO DE ADIVINHAÇÃO")
while tentativas > 0:
  resultado = num_verifica(sorteado)
  if resultado == 0:
    print("Parabenxxxx caraaa, você acertou memo!")
    break
  elif resultado == -1:
    print("Opaaaaaa, quaseeee, mas tenta com um maior aí")
  else:
    print("Passouuu um poucoo caraa, tenta de novo, com um número menorr\n")

  if tentativas == 1:
    print("tu é ruim memo, vai tentar mais n, perdesse, seu tanso")
    tentativas -= 1
  else:
    tentativas -= 1

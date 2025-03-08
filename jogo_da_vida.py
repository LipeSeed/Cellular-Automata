import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def criar_grade(linhas, colunas):
  return np.random.choice([0, 1], size=(linhas, colunas))

def atualizar_grade(grade):
  linhas, colunas = grade.shape
  nova_grade = np.copy(grade)

  for i in range(linhas):
    for j in range(colunas):
      vizinhos_vivos = contar_vizinhos_vivos(grade, i, j)

      if grade[i, j] == 1:  # Célula viva
        if vizinhos_vivos < 2 or vizinhos_vivos > 3:
          nova_grade[i, j] = 0
      else:  # Célula morta
        if vizinhos_vivos == 3:
          nova_grade[i, j] = 1

  return nova_grade

def contar_vizinhos_vivos(grade, linha, coluna):
  linhas, colunas = grade.shape
  vizinhos_vivos = 0

  for i in range(linha - 1, linha + 2):
    for j in range(coluna - 1, coluna + 2):
      if (i == linha and j == coluna) or i < 0 or i >= linhas or j < 0 or j >= colunas:
        continue
      vizinhos_vivos += grade[i, j]

  return vizinhos_vivos

def animar(frame, grade, img):
  grade[:] = atualizar_grade(grade)
  img.set_array(grade)
  return img,

linhas = 50
colunas = 50
geracoes = 100

grade = criar_grade(linhas, colunas)

fig, ax = plt.subplots()
img = ax.imshow(grade, interpolation='nearest', cmap='binary')

animacao = animation.FuncAnimation(fig, animar, fargs=(grade, img), frames=geracoes, interval=100, blit=True)

plt.show()
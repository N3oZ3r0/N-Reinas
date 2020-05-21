def ataque(i, j, tablero, N):
  # comprueba la columna
  for k in range(1, i):
    if(tablero[k][j] == 1):
      return True

  # comprueba la diagonal superior derecha
  k = i-1
  l = j+1
  while (k>=1 and l<=N):
    if (tablero[k][l] == 1):
      return True
    k=k-1
    l=l+1

  # comprueba la diagonal superior izquierda
  k = i-1
  l = j-1
  while (k>=1 and l>=1):
    if (tablero[k][l] == 1):
      return True
    k=k-1
    l=l-1

  return False

def nreinas(fila, n, N, tablero):
  if (n==0):
    return True

  for j in range(1, N+1):
    if(not(ataque(fila, j, tablero, N))):
      tablero[fila][j] = 1

      if (nreinas(fila + 1, n - 1, N, tablero)):
        return True

      tablero[fila][j] = 0 #backtracking
  return False

if __name__ == '__main__':
  tablero = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

  nreinas(1, 4, 4, tablero)

  # imprimir tablero
  for i in range(1, 5):
      print(tablero[i][1:])
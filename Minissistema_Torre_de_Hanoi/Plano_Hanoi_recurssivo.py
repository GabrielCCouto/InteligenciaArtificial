count = 0

def hanoi_rec(n, origem, auxiliar, destino, disco=1):
    global count
    if n == 1:
        count += 1
        print(f"{count} - mover disco {disco} de {origem} para {destino}")
    else:
        hanoi_rec(n-1, origem, destino, auxiliar, disco)
        count += 1
        print(f"{count} - mover disco {disco+n-1} de {origem} para {destino}")
        hanoi_rec(n-1, auxiliar, origem, destino, disco)

hanoi_rec(3, 'A', 'B', 'C')

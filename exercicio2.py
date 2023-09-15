def fibonacci(n):
    fibonacci_sequence = [1, 1]  # Inicializa a sequência com os dois primeiros termos

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

n = int(input("Digite o valor de n: "))
if n <= 0:
    print("Por favor, insira um valor válido maior que zero.")
else:
    result = fibonacci(n)
    print(f"Série de Fibonacci até o {n}-ésimo termo: {result}")

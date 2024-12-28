// Função recursiva para calcular o fatorial
function fatorial(n) {
    if (n === 0 || n === 1) {
      return 1; // Caso base: fatorial de 0 ou 1 é 1
    }
    return n * fatorial(n - 1); // Chamada recursiva
  }
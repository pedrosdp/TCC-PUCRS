**Aulas 1 e 2 - Mario Souto**

Conceitos Fundamentais

Servidor em Nuvem: Conjunto de máquinas físicas trabalhando como um único sistema. Caso uma máquina falhe, outra assume a carga, garantindo a continuidade do serviço.

Latência: Medida da velocidade de conexão entre solicitação e resposta.

ENIAC: Primeiro computador digital eletrônico de grande escala.

MVP (Mínimo Produto Viável): Versão básica de um produto que atende às funções essenciais.

Modelo Cliente-Servidor

Funcionamento: Navegador (cliente) → Solicitação (Request) → Servidor → Resposta (Response) → Banco de Dados.

Processamento: Entrada → Processo → Saída.

Erro 500: O servidor está indisponível para processar solicitações.

Escalabilidade e Performance

Problema de alta demanda: Utilizar dois sistemas ou um Load Balancer (Balanceador de Carga).

Escalabilidade:
Horizontal: Adicionar máquinas menores.
Vertical: Aumentar a capacidade de uma máquina existente.

Performance e UX: Sensação de rapidez para o usuário.

Espera Passiva: Usuário espera sem interação.
Espera Ativa: Elementos como animações ou jogos.

Técnicas e Ferramentas
12 Factors: Princípios aplicáveis a aplicações em qualquer linguagem.

Cloudflare: Cache de conteúdo estático para melhorar o desempenho.

Server-Side Rendered (SSR): Conteúdo dinâmico processado no servidor antes de ser enviado. Exemplos: AWS, Vercel.

GTmetrix: Ferramenta para medir o desempenho de sites.

Minificação e Concatenar: Otimização de arquivos para reduzir latência.

Estruturas e Práticas
Fila (Queue): Estrutura FIFO (First In, First Out). Ex.: Quem entra primeiro sai primeiro.

Métodos: enqueue (adicionar), dequeue (remover).

Arrays: Estruturas para armazenar dados em sequência.
Métodos:
push: Adicionar no final.
shift: Remover do início.

Objetos e Classes:

Objeto: Conjunto de atributos e funções.

Classe: Receita para criar objetos.

Open-Closed Principle: Código aberto para extensão, mas fechado para modificação.

APIs (Application Programming Interface): Serviços que permitem interação entre sistemas, como Google Maps.

**Aula 3 - Edson Ifarraguirre Moreno**

Introdução ao JavaScript
JavaScript: Linguagem baseada em objetos, dinâmica e 
fracamente tipada, interpretada em navegadores.

Declaração de variáveis:
let: Variável mutável dentro de um escopo.
const: Constante imutável.
var: Variável mutável global (não recomendado).

Estruturas e Comandos

Comandos de Repetição:
for, while, do/while.

Comandos de Seleção:
if, else, switch.

Modularização: Utilização de funções (function() {}) para organizar o código.

Operadores:
Aritméticos, incremento/decremento, relacionais e lógicos.

Estruturas de Dados

Arrays: Permitem armazenar múltiplos valores de forma contínua.

Métodos úteis: length, push, pop, shift, unshift, splice, slice, at.

Set: Armazena valores únicos, excluindo duplicados automaticamente.

Map: Estrutura que associa chaves a valores. Aceita qualquer tipo de dado e evita repetição de chaves.

Listas Encadeadas:
Nodos com referências para o próximo elemento.
Operações: add, get, remove.

Árvores: Estruturas não-lineares que permitem algoritmos eficientes.

Conceitos: Pai, filho, raiz, folha, galhos.
Tipos: Árvore binária (máximo 2 filhos por nó).

Técnicas e Algoritmos

Recursão: Solução de problemas dividindo-os em partes menores até alcançar a resolução completa.

Algoritmos de Ordenação:
Simples: Bubble Sort, Selection Sort, Insertion Sort.
Avançados: Merge Sort, Quick Sort.
Busca:
Linear: Percorre todos os elementos.
Binária: Divide o conjunto para encontrar rapidamente um elemento.

Complexidade Algorítmica
Mede eficiência de um algoritmo com base em:
Tempo de execução.
Espaço ocupado na memória.

Notação Big-O: Representa o comportamento do algoritmo em termos de desempenho.

Ferramentas Importantes:

VS Code: Editor de código amplamente utilizado.
Node.js: Ambiente de execução para JavaScript no servidor.

MDN Web Docs: Fonte confiável para aprender tecnologias da web.

Quokka.js: Ferramenta para mostrar resultados de código em tempo real.
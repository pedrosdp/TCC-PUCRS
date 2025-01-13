# Aula 1 e 2 - Professor Alessandro Valério

## Introdução à Programação Orientada a Objetos (POO)

### Definição
- **Não é**:
  - Uma linguagem de programação.
  - Uma ferramenta ou framework.
- **É**:
  - Um estilo de programação focado no uso de **objetos** ao invés de funções.

---

## Motivação

- Muitas linguagens de programação implementam o paradigma de **Orientação a Objetos** (O.O).
- POO busca resolver limitações da **Programação Estruturada** e da **Programação Procedural**.

---

## Programação Estruturada e Procedural

### Programação Estruturada
- Baseada em:
  1. **Sequência**: Exemplo com comandos como **Go TO**.
  2. **Decisão**.
  3. **Iteração**.

### Programação Procedural
- Foco em:
  - Uso de **procedimentos** e **funções** para facilitar o reuso do código.
  - Seguir boas práticas para manter um **código limpo**.

### Problemas da Programação Estruturada e Procedural
- **Copia e cola** excessivo de funções.
- Alterações em uma função resultam em mudanças em várias outras funções, criando **interdependência**.

---

## Programação Orientada a Objetos (POO)

### Paradigma
- Foco no uso de **objetos**, onde cada um contém:
  - **Atributos** (dados ou propriedades).
  - **Métodos** (funções associadas ao objeto).

### Elementos de um Objeto
1. **Nome**:
   - Identificação do objeto.
2. **Conjunto de Atributos**:
   - Representam o **estado** do objeto.
3. **Comportamentos (Métodos)**:
   - Ações que o objeto pode realizar.

### Definição de Objeto
- Uma coleção de:
  - **Dados** (atributos ou propriedades).
  - **Funcionalidades** (métodos).
- Relacionados entre si para formar uma unidade.

---

## Exemplo de Criação de Objeto

```javascript
var pessoa = {
    nome: "Valentina",
    idade: 60,
    saudar: function() {
        console.log("Olá");
    }
};

# Aula 1 e 2 - Professor Alessandro Valério (Continuação)

## Atributos ou Propriedades

- **Definição**:
  - Um ou mais dados presentes em um objeto.
  - Possuem:
    - **Nome único**.
    - **Valor ou referência**.
- **Como acessar um atributo?**
  - Usamos a notação de ponto:  
    `objeto.atributo`.

---

## Métodos

- **Definição**:
  - Representam funcionalidades associadas a um objeto.
- **Como acessar um método?**
  - Usamos a notação de ponto com parênteses:  
    `objeto.metodo()`.

---

## Criação de Objetos

- **Forma Literal**:
  - Escrever o objeto como ele é, diretamente no código.  
  - Exemplo:
    ```javascript
    var pessoa = {
        nome: "Valentina",
        idade: 60,
        saudar: function() {
            console.log("Olá");
        }
    };
    pessoa.saudar(); // Saída: Olá
    ```

## Tipos de Dados

### **Tipos de Valor (Imutáveis)**:
1. **Number**  
2. **String**  
3. **Boolean**  
4. **Symbol**  
5. **undefined**  
6. **null**

### **Tipos de Referência (Mutáveis e Complexos)**:
- **Object**

---

## Conceitos Principais de POO

1. **Encapsulamento**:
   - Proteção e isolamento de atributos.
   - Facilita a redução de complexidade e melhora a segurança dos dados.

2. **Abstração**:
   - Processo de entender o problema e simplificá-lo.
   - Permite trabalhar apenas com os aspectos relevantes.

3. **Herança**:
   - Compartilhamento de atributos e métodos entre objetos.
   - Ajuda a eliminar redundâncias, reaproveitando e agrupando código comum.

4. **Polimorfismo**:
   - Capacidade de modificar o comportamento herdado de um objeto-pai.
   - **JavaScript** suporta **sobrescrita de métodos** (classe filha).  
   - **Sobrecarga** (métodos com o mesmo nome, mas assinaturas diferentes) **não é suportada em JavaScript**.

---

## Vantagens do POO

1. **Encapsulamento**:
   - Reduz complexidade.
   - Protege os dados.
2. **Abstração**:
   - Simplifica o desenvolvimento.
   - Promove maior reutilização de código.
3. **Herança**:
   - Elimina redundâncias no código.
4. **Polimorfismo**:
   - Remove lógica desnecessária e limpa o código.

---

## Formas de Criar Objetos

1. **Literais**:
   - Criar diretamente no código.
   - Exemplo:
     ```javascript
     var carro = {
         marca: "Toyota",
         modelo: "Corolla"
     };
     ```

2. **Fábricas**:
   - Funções que criam e retornam objetos.
   - Exemplo:
     ```javascript
     function criarPessoa(nome, idade) {
         return {
             nome: nome,
             idade: idade
         };
     }
     var pessoa = criarPessoa("Carlos", 30);
     ```

3. **Construtores**:
   - Funções que criam objetos utilizando o operador `new`.
   - Exemplo:
     ```javascript
     function Pessoa(nome, idade) {
         this.nome = nome;
         this.idade = idade;
     }
     var pessoa = new Pessoa("Maria", 25);
     ```

4. **Protótipos**:
   - Mecanismo de herança entre objetos.
   - Cada objeto pode ter um protótipo que serve como modelo para herdar propriedades e métodos.
   - Exemplo:
     ```javascript
     var animal = {
         comer: function() {
             console.log("Comendo...");
         }
     };
     var cachorro = Object.create(animal);
     cachorro.comer(); // Saída: Comendo...
     ```
   - Funções úteis:
     - `Object.getPrototypeOf(objeto)`

5. **Classes**:
   - Sintaxe mais moderna introduzida no ES6 para criar objetos.
   - Exemplo:
     ```javascript
     class Pessoa {
         constructor(nome, idade) {
             this.nome = nome;
             this.idade = idade;
         }
         saudar() {
             console.log(`Olá, meu nome é ${this.nome}`);
         }
     }
     var pessoa = new Pessoa("João", 40);
     pessoa.saudar(); // Saída: Olá, meu nome é João
     ```

---

## Atributos e Métodos com `this`

- Sempre que for necessário acessar um atributo ou método dentro do próprio objeto, usamos a palavra-chave **`this`**.
- Exemplo:
  ```javascript
  class Pessoa {
      constructor(nome, idade) {
          this.nome = nome;
          this.idade = idade;
      }
      apresentar() {
          console.log(`Meu nome é ${this.nome} e tenho ${this.idade} anos.`);
      }
  }

## Visibilidade em POO

### Atributos e Métodos: Públicos e Privados

1. **Público**:
   - Atributos e métodos acessíveis de qualquer lugar.
   - Exemplo em JavaScript:
     ```javascript
     class Pessoa {
         constructor(nome) {
             this.nome = nome; // Atributo público
         }
         apresentar() {
             console.log(`Meu nome é ${this.nome}`); // Método público
         }
     }
     let pessoa = new Pessoa("Carlos");
     pessoa.apresentar(); // Saída: Meu nome é Carlos
     ```

2. **Privado**:
   - Atributos e métodos acessíveis apenas dentro do próprio objeto.
   - **JavaScript** suporta atributos privados com o uso de um **identificador prefixado** (`#`).
   - Exemplo:
     ```javascript
     class ContaBancaria {
         #saldo; // Atributo privado
         constructor(saldoInicial) {
             this.#saldo = saldoInicial;
         }
         depositar(valor) {
             this.#saldo += valor; // Método acessa atributo privado
         }
         consultarSaldo() {
             console.log(`Saldo: R$ ${this.#saldo}`);
         }
     }
     let conta = new ContaBancaria(100);
     conta.depositar(50);
     conta.consultarSaldo(); // Saída: Saldo: R$ 150
     // console.log(conta.#saldo); // Erro: Não é possível acessar atributo privado fora da classe
     ```

---

### Como Implementar Privacidade em JavaScript?

1. **Atributos Privados com `#`**:
   - Introduzido no ES2020 para criar propriedades privadas.
   - Exemplo:
     ```javascript
     class Usuario {
         #senha;
         constructor(nome, senha) {
             this.nome = nome;
             this.#senha = senha; // Atributo privado
         }
         autenticar(senha) {
             return this.#senha === senha; // Verifica senha
         }
     }
     let user = new Usuario("Alice", "12345");
     console.log(user.autenticar("12345")); // Saída: true
     // console.log(user.#senha); // Erro: Atributo privado
     ```

2. **Encapsulamento com Variáveis Locais**:
   - Usando funções com **closures**.
   - Exemplo:
     ```javascript
     function criarConta(saldoInicial) {
         let saldo = saldoInicial; // Variável local privada
         return {
             depositar(valor) {
                 saldo += valor;
             },
             consultarSaldo() {
                 console.log(`Saldo: R$ ${saldo}`);
             }
         };
     }
     let conta = criarConta(100);
     conta.depositar(50);
     conta.consultarSaldo(); // Saída: Saldo: R$ 150
     ```

---

### Identificadores Prefixados

- **Uso de Prefixos para Identificação**:
  - Ajuda a distinguir visibilidade ou uso específico de atributos e métodos.


# Aula 3 - Edson Ifarraguirre Moreno

## Paradigma de Programação
- **Linguagens Suportadas**: JavaScript, Java, C#, Python
- **Pilares**:
  - **Abstração**
  - **Encapsulamento**
  - **Herança**
  - **Polimorfismo**
- Largamente empregado na indústria.

## Declaração de Variáveis em JavaScript

### `var`
- Declara uma variável com **escopo de função**.

### `let`
- Declara uma variável com **escopo de bloco** ou **variável local**.

### `const`
- Declara uma **constante** com **escopo de bloco**.

## Objetos

### Intrínsecos ao JavaScript:
- `Array`
- `Boolean`
- `Date`
- `Math`
- `Number`
- `String`
- `RegExp`
- `Global`

## Tipos de Dados
- `Undefined`
- `Null`
- `Boolean`
- `String`
- `Number`
- `Object`
- `Symbol`

Arrays - Objeto do tipo Array
    Permite o armazenamento de uma coleção de múltiplos itens
    São espaços;

let a = []
let a ["A", "B", "C"]
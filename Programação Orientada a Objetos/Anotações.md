Aula 1 e 2 - Professor Alessandro Valério

Faz parte de um paradigma de programação com foco em objetos em vez de funções.

Não é uma Linguagem de programação
Não é uma ferramenta ou framework

É um estilo de programação;

Motivação: Muitas linguagens implementam O.O

Programação Estruturada: Sequência (Go TO), decisão e iteração;

Programação Procedural: Foco no uso de pprocedimentos e funções para facilitar o reuso;

Boa prática/código limpo;

Programação Estruturada e Procedural: muito copia e cola de funções; Mudanças em uma função resultam em mudanças em outras funções. Interdependência entre funções.

Programação Orientada a Objetos
    Paradigma com foco no uso de objetos, onde cada um contém suas variáveis e funções;

tudo que é dado de um objeto é atributo;

Objeto - Conjunto de componentes

    Todo objeto tem um nome;
    Conjunto de atributos; estado daquele objeto
    Comportamentos ou métodos; ações;

Objeto é coleção de dados e/ou funcionalidades; Alguma relação entre si;

dados -> variáveis (atributos ou propriedades)

EXEMPLO criação de objeto:

var pessoa = {
    nome: "Valentina",
    idade: 60,
    saudar: fuction(){
        console.log ("Olá");
    }
}

Atributo ou Propriedade: Um ou mais dados presentes em um objeto;

Possuem nome único. Possuem valor ou referência;

Para acessar o atributo: 

objeto.atributo

Métoodos = representa um ou mais funcionalidades presentes em um objeto;

Como acesso método? 

objeto.metodo()

O primeiro jeito de criar objetos é como fizemos até agora: A gente vai criar de forma literal - como é, como está sendo lido (Alessandro Valério).

TIPOS de VALOR (imutáveis)
    Number
    String
    Boolean
    Symbol
    undefined
    null

Tipos de Referência (mutáveis e complexos)
    Object

Conceitos Principais
    
    -Encapsulamento - Proteção de atributos - Isolamento
    
    -Abstração - Tentar entender o problema; Fazer sentido;
    
    -Herança - Compartilhamento de atributos e métodos entre objetos; Reaproveita código e agrupa o que é comum a diferente objetos; Ajuda a eliminar redundâncias;

    -Polimorfismo - É possível alterar um comportamento herdado de um objeto-pai. Limpeza de código, removendo lógica excedente;
        *Sobrescrita de método (classe filha);
        *Sobrecarga (Mesmo nome mas diferentes assinaturas)
    JavaScript não suporta SOBRECARGA.

Vantagens
    Encapsulamento - Redução de complexidade e proteção de dados;
    Abstração - Redução de Complexidade e maior reuso;
    Herança - Eliminar redundâncias no código;
    Polimorfismo - Eliminar lógica desnecessária no código;

Formas de criar objetos
    Literais
    Fábricas - Funções que criam e retornam objetos; 'Syntax Sugar'
    Construtores
    Protótipos
    Classes

var pessoa = {
nome: ['Fulano',"de Tal"],
anoDeNascimento: 1990,
profissão: "Estudante",
calculaIdade: function(){
    return new Date().getFullYear() - this.anoDeNascimento
}

}
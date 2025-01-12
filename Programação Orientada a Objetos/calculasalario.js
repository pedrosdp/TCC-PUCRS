const empregado = {
    salarioBase: 5000,
    valorHoraExtra: 100,
    qtHorasExtras: 10,
    calculaSalario: function() {
        return this.salarioBase + (this.valorHoraExtra * this.qtHorasExtras);
    }
};

// Exemplo de uso:
console.log(empregado.calculaSalario());


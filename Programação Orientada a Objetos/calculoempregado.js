function criaEmpregado(salarioBase, valorHoraExtra, qtHorasExtras) {
    return {
        salarioBase,
        valorHoraExtra,
        qtHorasExtras,
        calculaSalario: function() {
            return this.salarioBase + (this.valorHoraExtra * this.qtHorasExtras);
        }
    };
}
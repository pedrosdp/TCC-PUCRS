const funcoes = require('./funcoes');

test('Dois mais dois devera ser quatro', ()=>{
    expect (funcoes.somarDoisValores(2,2))
    .toBe(4);
});
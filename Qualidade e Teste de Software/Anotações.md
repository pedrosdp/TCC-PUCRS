# Aula 1 e 2 - Ricardo Beck

## O teste de software é um exercício de disciplina

---

### O que é qualidade?
Qualidade é uma sensação, segundo o QAI, que um produto ou serviço atende a necessidade do cliente.

---

### O que é um projeto complexo
São projetos que demandam uma efetiva gestão de riscos no processo tendo como dependências internas e externas.

---

### Ciclo de vida de projetos de software
- **Waterfall - Cascata**  
  Projetos regulares com etapas definidas para: Investigação, prototipação, desenvolvimento, testes e liberação.

- **Ciclo de vida ágil**  
  Projetos iterativos onde a cada etapa de tempo (sprint) ocorre uma entrega de valor.

---

### Tipos de testes e suas características
Qualidade é caracterizada como uma "sensação" pelo **Quality Assurance Institute**. O usuário ou cliente sabe que um produto tem "qualidade" se esse produto, serviço ou artefato serve ao seu propósito.

---

### Conceito de caixa transparente
Advém da possibilidade de conhecermos as partes "internas" do artefato a ser testado.

---

### Uma unidade para teste
Em geral temos:
- **DD path** - Caminho decisão à decisão  
- **DU path** - Declaração e Uso das variáveis

---

### Necessidade de isolamento entre componentes
As unidades devem ser isoladas entre si, de forma a garantir o mínimo de interferência externa quando os estímulos forem recebidos.

---

### Estratégias de teste unitário
- **TDD (Test Driven Development)**  
  Cria-se o teste unitário antes de começar a codificação.

- **BDD (Behavior Driven Development)**  
  Entende-se a demanda da unidade para que sejam criados os testes. Podem ser baseados em "promessas" ou requisitos funcionais / não funcionais.


# Diferenças entre Teoria e Prática

- No dia a dia, cria-se o código e depois testa-se.  
- A regra de ouro é **80% ou mais de cobertura de código**.

---

## Integração dos Testes Unitários no Dia a Dia

### Ferramental para Criação/Execução e Relatórios
- **Java** - IDE Eclipse - JUnit  
- **JavaScript** - Mocha  
- Jest  

### Criação e Apresentação de Relatórios
- **Allure** (GitHub)

---

### Lint
Ferramenta para análise de código estático.

---

## Testes de Integração
Avaliam o ecossistema no qual os diferentes métodos ou classes se integram compondo a solução.

### Estratégias de Integração de Componentes
- **Top-down**  
- **Bottom-up**  
- **Sanduíche**

---

## Ferramental para Criação/Execução e Relatórios
- **Jenkins**  
- **Codeway**

---

## Testes de Interface com o Usuário
### Pontos de Verificação
- Alinhamento dos componentes visuais.  
- Verificação dos padrões de ancoragem, padronização das cores, fontes e espaçamentos.  
- Verificação do vocabulário usado.

---

## Diferenças entre Testes de Front-end e Testes de Interface Gráfica
Testes de front-end são mais técnicos, focando na funcionalidade do código, enquanto os testes de interface gráfica avaliam a experiência e apresentação visual para o usuário.

---

## Árvore do Sistema
Ferramentas e técnicas para planejamento e organização:
- **Mental Maps**  
- **Word**  
- **Jira**

# Acessibilidade
- Considerar o suporte a:
  - **Teclado** (navegação e atalhos)  
  - **Voz** (comandos de voz e leitores de tela)  
  - **Alto-contraste** (para usuários com baixa visão)  
  - **Fluxos simples** (facilidade na navegação)  
- Seguir as diretrizes do **W3C**.

---

## Quais Estratégias Aplicar?
- O custo do defeito tende a **aumentar conforme o processo de desenvolvimento de Software avança**. É importante identificar e corrigir problemas o mais cedo possível.

---

## Teste de Performance
### Avaliação
- Número de usuários por tempo.  
- Realizar avaliações/inspeções periódicas para validar o desempenho em cenários específicos.  

### Considerações
- **Entendimento do ambiente** no qual o software será executado.

---

### Definição de Baseline
- **Baseline**: É o padrão atual ou padrão definido como referência para comparação de desempenho.

### Ferramentas
- **LoadRunner**  
- **JMeter**  
  Ambas as ferramentas geram relatórios para análise.

---

## SLA e Performance
### Garantia de Qualidade
Para garantir a qualidade, deve-se seguir:
- **Estratégia de teste**  
- **Plano de testes**  
- **Casos de teste**  
- **Pré-requisitos**  
- **Passos de teste**  
- **Resultado esperado**  
- **Relatório de testes**

---

## Repetibilidade do Processo
- Deve ser **auditável a qualquer momento**.
- Elementos importantes:
  - **Versionamento**  
  - **Planejamento**  
  - **Exercício de disciplina**

---

### Relatórios de Teste
- Os relatórios devem demonstrar o **andamento da qualidade do produto**.

---

### Priorização dos Itens Identificados
- Os defeitos encontrados devem ser priorizados com base no **impacto ao usuário**.

---

### Métricas Voltadas ao Controle de Qualidade
O controle das métricas é essencial para apoiar decisões gerenciais:
- Defeitos por **prioridade**.  
- Defeitos por **sistema/browser/requisito**.


    # Teste AB

## Definição de ROI
- **Retorno sobre investimento (ROI)** é um cálculo que avalia os gastos relacionados à qualidade e compara com o possível prejuízo que poderia ter ocorrido por não aplicar essas estratégias.

---

## Estratégia de Qualidade de Software
- Para criar a estratégia, é fundamental entender o **propósito da solução** e os objetivos do projeto.

---

## Projetos Ágeis
- A qualidade deve estar **sempre presente** em todas as etapas do ciclo de vida.
- Manter o entendimento do ciclo de vida e **atualização contínua**.

### Desenvolvimento Agile
1. **Ciclos de desenvolvimento**: Adicionar valor continuamente.  
2. **Review**: Validar o que foi feito.  
3. **Feedback**: Coletar melhorias.  
4. **Documentação**: Manter registros organizados e compreensíveis.  
5. **Ajustes**: Rastrear e aplicar melhorias.  
6. **Próxima Sprint**: Planejar e executar a etapa seguinte.

- A qualidade deve ser refletida de forma direta em **todos os processos do ciclo de vida**.

---

## Testador x SDET

### SDET (Software Development Engineer in Test)
- Profissional que pode atuar como desenvolvedor de software ou desenvolvedor de testes.
- Pode auxiliar no processo dependendo da demanda.  
- **Conhece o código**, o que possibilita análises mais profundas.  
- Um profissional **mais completo** para atuar no desenvolvimento e testes.  
- Não é, necessariamente, especializado apenas em testes.

---

## Certificadores de Mercado
- **QAI**  
- **ISTQB** - Oferece treinamentos voltados para testes.

### Certificações Mais Reconhecidas pela Indústria
- **CSTE** - QAI  
- **CSQA** - QAI  
- **CAST** - QAI  

---

## KPIs (Key Performance Indicators)
- Indicadores de desempenho chave para monitorar e avaliar a qualidade.

### Como Correlacionar Níveis de Qualidade com Métricas?
- **Nível de teste unitário**  
- **Nível de teste de integração**  
- **Nível de sistema**

---

## Ferramentas
- **JMeter**: Uma ferramenta Java para realizar testes de carga e estresse em recursos estáticos ou dinâmicos, simulando usuários virtuais.  
- **LoadRunner**: Ferramenta para testes de desempenho.  
- **Perfmon** (Windows): Ferramenta para monitoramento de desempenho.

---

## Exemplos - Testes A/B

### Quando e Por Que Aplicar?
- Usados para comparar **duas versões de uma solução** e identificar qual apresenta melhor desempenho.
- Permite tomada de decisão baseada em métricas de desempenho e interação do usuário.

---

## Analytics
- **Monitoramento de Interações**:
  - Onde o usuário clicou?  
  - Quanto tempo ele gastou em cada interação?  
- A análise dessas métricas auxilia no **aperfeiçoamento da experiência do usuário** e na tomada de decisões informadas.
 
Aula 3 - Daniel Callegari

Qualidade de Software - Assegurar que o software cumpra com as suas especificações e atenda às necessidades dos clientes. 

Verificação da correção, frente aos requisitos. Feita pela equipe; verificando se atende especificações á procura de DEFEITOS
Consistência, clareza, segurança dos requisitos

Validação com o cliente, no ambiente final
Junto com o cliente; atende ao que o cliente quer? à procura de PROBLEMAS 
Critérios: usuabilidade, desempenho, portabilidade do produto

Técnicas Estáticas - Não requerem que o sistema seja executado - Revisões
Técnica Dinâmicas requerem trablhar com uma representação executável do sistema - Testes

Níveis de Teste de SOFTWARE

  Teste de Unidade - Cada componente é testado separadamente.

  Teste de Integração - Interfaces entre os componentes
  
  Teste de Sistema - Extremo do  teste de integração; Analisa as funcionalidades do sistema como um todo.

  Teste de Regressão - Re-teste após reparo de falhas ou inclusão de funcionalidades.

caso de teste é um subconjunto de entradas e saídas planejadas, para um ambiente controloado de execução. 

Roteiro de teste é conjunto de casos de teste.

Desafio: Definir um subconjunto mínimo de casos de teste com a maior probabilidade de apontar erros.

Técnicas de TESTE

  CAIXA PRETA - Teste Funcional - O que o sofwar faz e não como ele faz]
-Independe da linguagem-paradigma
-Pode ser manual ou automatizado
-Pode ser usado em todos os níveis

  CAIXA BRANCA - Teste Estrutural - Sobre o código fonte
-Ocorre sobre o código fonte
-Complexidade Ciclomática - É uma métrica - pode ser regiões; arcos; nodos;

teste de unidades: 
  Junit (para java)
  Jest (para javascript)

A menor unidade testável em um sistema
Diversas granularidades

teste de integração - TDD (test-driven development)
1) adicione um teste
2) execute. o novo teste deve falhar por motivos esperados
3) mais simples que passa no novo teste
4) Todos os testes agora devem passar
5) Refatore
6) Repita

Sempre de maneira incremental. para feedback mais rápido

Utiliza-se código de apoio

Drivers: Responsáveis pelo controle dos testes.
Stubs: Simulam comportamento da UNIDADE

Caso do Foguete ariane 4. cálculo de inclinação;
erro de overflow - no ariane 5;

Técnicas de TOP-DOWN(stubs) ou BOTTOM-UP (drivers)

Teste no nível de INTEGRAÇÃO
  Orientado a objetos;
  Características específicas;

Testes de sistema, aceitação e regressão
  Os testes lidam com o comportamento de um sistema como um todo, mas com diferente propósitos.

Teste no nível de SISTEMA

  Comportamento funcional
  Requisitos de qualidade

  FURPS MODEL
  Funcionalidade
  Confiabilidade
  Eficiência
  Manutenibilidade
  Portabilidade
  Usabilidade

Junit - Test



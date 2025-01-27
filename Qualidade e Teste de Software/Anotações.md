Aula 1 e 2 - Ricardo Beck

O teste de software é um exercício de disciplina;

O que é qualidade? 

    Qualidade é uma sensação, segundo o QAI, que um produto ou serviço atende a necessidade do cliente.

O que é um projeto complexo

    São projetos que demandam uma efetiva gestão de riscos no processo tendo como dependências internas e externas.

Ciclo de vida de projetos de software

    Waterfall - Cascata - Projetos regulares com etapas definidas para: Investigação, prototipação, desenvolvimento, testes e liberação;

    Ciclo de vida ágil; - Projetos interativos onde a cada etapa de tempo (sprint) ocorre uma entrega de valor;

Tipos de testes e suas características

    Qualidade é caracterizada como uma "sensação" pelo Quality Assurance Institute, o usuário ou cliente sabe de um produto tem "qualidade" se esse produto, serviço ou artefato serve ao seu propósito;

Conceito de caixa transparente
    advém da possibilidade de conhecermos as partes "internas" do artefato a ser tesatdo.

Uma unidade para teste
    Em geral temos:
        DD path - Caminho decisão à decisão
        DU path - Declaração e Uso das variáveis

Necessidade de isolamento entre componentes
    As unidades devem ser isoladas entre si, de forma a garantir o mínimo de interferência externa quando os estímulos forem recebidos.

Estratégias de tese unitário

TDD = Test Driven Development

    Cria-se o teste unitário antes de começar a codificação.

BDD = Behavior Driven Development
    Entende-se a demanda da unidade para que sejam criados os testes. Podem ser baseados em "promessas" ou requisitos funcionais / não funcionais.

Diferenças entre teoria e prática
    No dia-a-dia cria-se o código e depois testa-se
    A regra de ouro é 80% ou mais de cobertura de código.

Integração dos testes unitários no dia-a-dia

Ferramental para criação/execução e relatórios
    Java - Ide Eclipse - Junit
    JavaScript - Mocha
    Jest 
Criação e apresentação de relatórios
Allure - github

Lint;

Testes de integração: Avaliam o ecossistema no qal os diferentes métodos ou classes se integram compondo a solução;

Estratégias de integração de componentes
Top-down
Bottom-up
Sanduíche

jenkins e codeway = ferarmental para criação/excução e relatórios

Testes de Interface com o usuário
    Pontos
        Verificação do alinhamento dos componentes visuis.
        Verificação dos padrões de ancoragem, padronização das cores, fontes e espaçamentos
        Verificação do vocabulário usado.

Diferenças entre testes de front-end e testes de interface gráfica

Árvore do sistema;
    Mental maps
    Word
    Jira

Acessibilidade - teclado, voz, alto-contraste e fluxos simples; W3C;

Quais estratégias aplicar?

    O custo do defeito tende a aumentar conforme o processo de desenvolvimento de Software.

Teste de performance - Num de usuários por tempo
    São avaliações/inspeções periódicas que devem ser feitas visando um cenário de uso específico.
    Entendimento do ambiente

Definição de Baseline
    é definida como o padrão atual ou padrão definido;

LoadRunner
JMeter
Ambas as ferramentas geram relatórios para análise.

SLA e Performance

Garantia de QUALIDADE;
    Estratégia de teste
    Plano de testes
    Casos ed teste
    Pré-requisito
    Passos de teste
    Resultado esperado
    Relatório de testes

Repetibilidade do processo
    Deve ser auditável a qualquer momento.
    Versionamento
    Planejamento
    Exercício de disciplina

    Relatórios de teste
        Os relatórios de teste devem demonstar o andamento da qualdade no produto
    
    Priorização dos itens identificados
        Os defeitos achados devem sempre ser priorizados de acordo com impacto ao usuário.

    Métricas voltadas ao controle de qualidade
        O controle das métricas é necessário para apoiar as decisões gerenciais;
            Defeitos por prioridade 
            Defeitos por Sistema/Browser/requisito

    Teste AB    

Definição de ROI : Retorno de investimento (return on investment) é um cálculo que auxilia o entendimento dos gastos compromentidos com a qualidade e o que poderia ter sido o prejuízo por não aplicar.

Estratégia de Qualidade de Software
    Para compor a estratégia é necessário entender o propósito da solução.

Projetos ágeis  
    Qualidade sempre presente.
    Entender o ciclo de vida e como estar sempre atualizado

Desenvolvimento Agile
    1. Ciclos de desenvolvimento (adicionado valor)
    2. Review - validar o que foi feito
    3. Feedback
    4. documentados, guardados e entendido
    5. Ajustes e rastrear
    5. Próxima sprint

como atuar? de maneira direta, a qualidade deve ser refletida em todos os processo do ciclo de vida

Testador x SDET

    SDET: Profissional que pode trabalhar como desenvolvedor de software ou desenvolvedor de testes. 
    pode auxiliar nos processos dependendo da demanda
    Tem um viés, por conhecer o código.
    Profissional mais completo para atuar
    Não é, necessariamente, especializado em testes

    Certificadores de mercado
    QAI
    ISTQB - treinamentos

    Certificações mais reconhecidas pela indústria
    CSTE - QAI
    CSQA - QAI
    CAST - QAI

KPIs = Key Performance Indicator.
Quais KPis devo escolher?

como correlacionar níveis de qualidade com métricas?
    Nivel de teste unitário
    Nível de teste de integração
    Nível de sistema

JMeter = uma ferramenta Java que realiza testes de
carga e de estresse em recursos estáticos
ou dinâmicos, oferecidos por sistemas
computacionais, através de usuários virtuais.

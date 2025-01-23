# Aula 1 e 2 - Vinicius Soares

## Contexto

### SOA - Service Oriented Architecture
SOA é uma abordagem arquitetural corporativa que permite a criação de serviços de negócio interoperáveis que podem ser facilmente reutilizados e compartilhados entre aplicações e empresas.

- **Reusabilidade**;

### Benefícios do SOA
- **Desacoplamento**: Integrações inteligentes;
- **Reutilização de serviços**;
- **Infraestrutura de plataforma**.

---

### Monólito x Microservices

#### Monólito
- Típico de um sistema complexo - Implementadas em um único processo.
  - Fácil de desenvolver;
  - Fácil manutenção;
  - Apenas um deploy;
  - Tráfego de rede baixo;

##### Problemas:
- Aumento de complexidade e tamanho ao longo do tempo;
- Alta dependência de componentes de código;
- Escalabilidade do sistema é limitada;
- Falta de flexibilidade;
- Dificuldade para colocar alterações em produção;

---

#### Microserviço
- Manutenção e evolução dos serviços mais estáveis;
- Serviços com baixo nível de acoplamento e interdependência;
- Escalabilidade do sistema;
- Redução de custos;
- Flexibilidade de tecnologia;
- Facilidade de colocar alterações em produção;
- Resiliência;
- Aumento da produtividade;
- Implementação de entrega contínua;
- Monitoramento e automação de processos;
- Foco na entrega de valor ao cliente.


   ## Riscos dos Microserviços

- **Aumento da complexidade da coordenação**;
- **Comunicação entre os microsserviços**;
- **Governança**.

---

## Características Principais

- **Newman, Sam**: "Um conjunto de pequenos autônomos que trabalham juntos".
- **Software modularizado**.
- **API RESTful**: Comunicação baseada em HTTP e JSON.
- **Out-of-process**: Possibilidade de execução fora dos processos.
- **Chamadas remotas**: Microsserviços são acessados por chamadas remotas.
- **Independente de linguagem de programação**.
- **Baixo acoplamento**: Foco no domínio específico de negócio.
- **Escalabilidade**:
  - Horizontal.
  - Vertical.

---

## Características Organizacionais

- **Agilidade**.
- **Equipe pequena e focada**: O conceito de "TWO PIZZAS team" (equipes pequenas o suficiente para serem alimentadas com duas pizzas).

---

## Práticas Recomendadas

1. **Organização em torno do domínio da empresa**.
2. **Descentralização completa**.
3. **Cada microserviço possui seu próprio serviço de dados**.

---

### Boas Práticas para APIs

- APIs bem projetadas: Evitar o vazamento de detalhes da implementação.
- **Autenticação e certificado**: Utilizar um gateway para segurança e gerenciamento.

---

### Resiliência

- **Isole falhas**: Garantir que falhas em um serviço não afetem o sistema inteiro.

## IaaS (Infrastructure as a Service)

- **Infraestrutura como serviço**: Computação de infraestrutura sob demanda.

### Modelos:
1. **Servidores**;
2. **Storage**;
3. **Rede**;
4. **Sistemas operacionais**.

- Aluguel de espaço para esses recursos em uma infraestrutura externa.

### Tipos de Nuvem:
- **Nuvem pública**.
- **Nuvem privada**.
- **Nuvem híbrida** (utilizando VPN).

### Quando usar?
- Quando a demanda for **volátil**.
- Empresas sem capacidade de investimento em hardware.

---

## PaaS (Platform as a Service)

- **Plataforma como serviço**: 
  - Uma camada middleware e/ou componentes prontos.
  - Uma camada de abstração entre sua aplicação e a nuvem.

### Benefícios:
- Plataforma e ambiente para permitir que os desenvolvedores criem aplicativos e serviços na internet.
- **Desenvolvimento 100% focado no negócio**.
- **Alta produtividade**.
- **Menor custo e mais entregas**.
- Contra o efeito **lock-in**:
  - Cenário em que uma solução tecnológica impede a migração para outra, "trancando" o usuário dentro dela.

# THE TWELVE (Os Doze Fatores)

1. **Base de Código**:
   - Mantenha uma base de código por aplicação.
2. **Dependências**:
   - Declare e isole explicitamente as dependências.
   - Utilize um gerenciador de dependências configurado para seu projeto (ex.: Maven, Gradle, npm, pip, etc.).
3. **Configurações**:
   - A troca de ambiente não pode afetar a aplicação.
4. **Serviços de Apoio**:
   - Trate serviços como recursos conectados à aplicação.
5. **Construa, Lance e Execute**:
   - Separe as etapas de construção, lançamento e execução.
6. **Processos**:
   - Aplique processos independentes e sem estado.
7. **Vínculo de Porta**:
   - Exponha serviços por portas configuráveis.
8. **Concorrência**:
   - Divida seu aplicativo em pequenos pedaços escaláveis.
9. **Descartabilidade**:
   - A aplicação deve ser facilmente inicializável e desligável.
10. **Paridade entre Desenvolvimento e Produção**:
    - Mantenha a máxima similaridade entre os ambientes de desenvolvimento e produção.
11. **Logs**:
    - Trate logs como um fluxo contínuo de eventos.
12. **Processos Administrativos**:
    - Utilize processos únicos e curtos para manutenção ou gerenciamento.

---

## Aplicações - **Cloud Native**

### Definição:
- **Containerrizado**.
- **Gerenciado**.
- **Orientado a microserviços**.
- **Baseado em nuvem**.

---

## Containers

- Pequenos sistemas baseados em **Linux**.
- Compartilham o mesmo **Kernel**.
- Permitem o compartilhamento de ambientes customizados.

### Por que os contêineres são bons para microserviços?
- Possibilitam o compartilhamento do **sistema operacional** e de **bibliotecas**, otimizando recursos e simplificando o gerenciamento.

    # Docker

## Maturidade com Cloud Native

- **Cenário atual**:
  - A tecnologia é relativamente **nova**, e a maioria das empresas não tem experiência suficiente para navegá-la por conta própria.
  - **Riscos**: É muito fácil e caro cometer erros.

- **Estratégia**:  
  - Utilize o conceito de **AS-IS TO BE**:
    - **AS-IS**: Onde você está agora.
    - **TO-BE**: Onde deseja chegar a partir daqui.

---

## Níveis de Maturidade em Cloud

1. **Nível 0 - Cloud Ready**:
   - Preparado para nuvem, mas não utiliza recursos nativos.
2. **Nível 1 - Cloud Friendly**:
   - Infraestrutura e serviços com alguma compatibilidade com a nuvem.
3. **Nível 2 - Cloud Resilient**:
   - Projetado para aproveitar as vantagens de resiliência na nuvem.
4. **Nível 3 - Cloud Native**:
   - Totalmente integrado e otimizado para o ambiente nativo da nuvem.

---

## Particionamento de Serviços

### **Domain-Driven Design (DDD)**
- **Definição**: 
  - Conceito criado por **Eric Evans**.
  - Reúne um conjunto de boas práticas, padrões, ferramentas e recursos de orientação a objetos.
  - Objetivo: Construção de sistemas de acordo com o domínio e as regras de negócio do cliente.

### Principais Componentes do DDD:
1. **Modelo de Domínio**:
   - Reflete o **negócio e domínio** do cliente.
2. **Linguagem Onipresente**:
   - Vocabulário compartilhado entre a equipe de desenvolvimento e as partes interessadas no negócio.
3. **Arquitetura em Camadas**:
   - Estrutura bem definida que separa responsabilidades.
4. **Padrões de Design**:
   - Uso de padrões que facilitam a implementação de sistemas robustos.

### Características:
- **Modelo Evolutivo**:
  - É atualizado continuamente, **sprint após sprint**, permitindo adaptações de acordo com as necessidades do cliente e do negócio.


# Event Storming

- **Definição**: 
  - Uma técnica de **design rápido** para mapear e compreender sistemas complexos.

## Passos do Event Storming:
1. **Mapeando os Eventos**:
   - Identifique os eventos significativos que ocorrem no sistema.
2. **Identificando os Comandos**:
   - Relacione os comandos que acionam os eventos.
3. **Associando os Aggregates**:
   - Identifique os aggregates que controlam o estado do domínio.
4. **Delimitando as Fronteiras do Modelo**:
   - Estabeleça os limites do modelo e os contextos delimitados.
5. **Identificando os Domínios de Negócio**:
   - Agrupe funcionalidades relacionadas para determinar os domínios de negócio.

---

## Comunicação

### Tipos de Comunicação:
1. **Síncrona**:
   - Exemplos:
     - REST
     - SOAP
     - CDI
2. **Assíncrona**:
   - Exemplos:
     - Mensagens
     - Eventos
     - Replicação de base de dados.

---

## Comunicação Orientada a Eventos

- **Exemplo de Métrica**:
  - Tempo para o **usuário**: 4 segundos até a aplicação ser renderizada.

---

## CQRS (Command Query Responsibility Segregation)

- **Definição**:
  - Uma abordagem arquitetural que separa operações de **leitura** (Query) das de **escrita** (Command).
- **Características**:
  - Pode ser complexo de implementar.
  - Facilita o uso de diferentes modelos para leitura e escrita, otimizando desempenho e escalabilidade.


# Orquestração e Coreografia

## Orquestração
- **Definição**: Processo sincronizado de comunicação.
- **Características**:
  - Possui uma lógica bem definida na sequência de eventos.
  - **Acoplamento apertado**: Alta dependência entre os componentes.

## Coreografia
- **Definição**: Gerenciamento de fluxos de longa duração.
- Não possui um controlador central; os serviços interagem de maneira autônoma.

---

# SAGAS

- **Definição**: Uma sequência de transações locais que juntas garantem a consistência do sistema.
- **Tipos de Saga**:
  1. **Baseada em Orquestração**:
     - Um orquestrador central controla a sequência de transações.
  2. **Baseada em Coreografia**:
     - Os serviços interagem entre si com base em eventos, sem um controlador central.

---

# Registro e Descoberta de Serviços

## **Service Registry**:
- Um repositório central onde os serviços registram sua localização e informações de conexão.

## **Descoberta de Serviços**:
- **Problema**: Como o Serviço A se comunica com o Serviço B sem ter conhecimento prévio da localização de B?
- **Soluções**:
  - REST API.
  - **Tipos de Descoberta**:
    - **Client-SIDE**: O cliente encontra o serviço diretamente usando o registro.
    - **Server-SIDE**: Um intermediário (geralmente um gateway) realiza a descoberta.

---

# Integração e Deploy Contínuo

- **Definição**: Desenvolvimento de software onde as equipes integram seu trabalho continuamente.
- **Objetivo**: Colocar o software em produção rapidamente e receber feedback dos usuários.

### **Deploy Contínuo**
- **Benefícios**:
  - **Medida real de progresso**: Teste contínuo com feedback do usuário.
  - Reduz consideravelmente o risco de release.
  - Cada commit gera um **release candidate**.
- **Pirâmide de Testes**:
  - Garanta que os testes abrangem diferentes níveis do sistema (unidade, integração, aceitação).

---

# Build Pipeline

- **Etapas**:
  1. **Poll SCM**: Monitoramento do sistema de controle de versão.
  2. **Compilação**: Geração do código executável.
  3. **Cobertura dos Testes**: Garantir que todas as partes importantes do sistema estão sendo testadas.
  4. **Qualidade**: Avaliação de código e performance.

---

# Database Continuous Migration

- **Definição**: Automação no processo de migração de banco de dados.
- Garantir que mudanças no esquema ou nos dados sejam consistentes com cada versão do software.

---

# Rollback

- **Definição**: 
  - Processo de reversão para uma versão anterior do sistema em caso de falhas.
- **Objetivo**:
  - Minimizar o impacto no usuário e restaurar a funcionalidade rapidamente.


# Aula 3 - Luis Fernando Planella Gonzalez

## Comunicação Assíncrona via Filas

### Modelos de Comunicação:
1. **Requisição / Resposta**:
   - Relacionamento típico entre **cliente / servidor**.
2. **Produtor / Consumidor**:
   - Um **produtor** envia mensagens para a fila, e um **consumidor** as processa.

---

### Fila de Mensagens
- Cada mensagem produzida por um **produtor** é entregue a um único **consumidor**.

### Tópico de Mensagens
- Permite que múltiplos consumidores recebam a mesma mensagem.

### Message Broker
- Sistema especializado em enviar e receber mensagens.
- Exemplos:
  - **Kafka**
  - **ActiveMQ**
  - **RabbitMQ**

---

## Tipos de Entrega de Mensagens

1. **No máximo uma vez (at-most-once delivery)**:
   - A mensagem pode ser entregue apenas uma vez ou perdida.
2. **Ao menos uma vez (at-least-once delivery)**:
   - A mensagem será entregue, mas pode ser duplicada.
3. **Exatamente uma vez (exactly-once delivery)**:
   - A mensagem será entregue apenas uma vez, garantindo integridade.

---

## Por que usar Mensagens?

1. **Notificar Eventos de Domínio**:
   - Permitir que outros serviços sejam informados sobre alterações ou eventos importantes.
2. **Atualizar Caches de Dados de Outros Serviços**:
   - Garantir que serviços compartilhem dados atualizados.
3. **Processamento Paralelo**:
   - Dividir o processamento em partes para maior eficiência.
4. **Resolver Problemas com Transações de Banco de Dados**:
   - Garantir consistência e integridade nas operações distribuídas.

---

## Caixa de Saída Transacional

- **Definição**:
  - Técnica para garantir a consistência entre a base de dados e as mensagens enviadas para filas.
- **Como funciona**:
  1. As mensagens são armazenadas em uma **caixa de saída transacional** (outbox).
  2. Após a transação ser confirmada no banco de dados, as mensagens são enviadas.


# Serverless

- **Definição**:
  - Apesar do nome, as aplicações **serverless** necessitam de um servidor para rodar.
  - A diferença é que as aplicações **não sabem qual servidor** será responsável por executá-las.
  - **Geralmente associado ao FaaS (Functions as a Service)**.

---

## FaaS - Functions as a Service

### Características:
- **Nem todo tipo de aplicação é adequado para o modelo**.
- Ideal para **funções disparadas por eventos**.
- O desenvolvedor empacota as funções que serão executadas no modelo.
- Geralmente utiliza um **container** (como o Docker).
- **Recursos alocados sob demanda**:
  - Quando há demanda, o ambiente automaticamente aloca os recursos necessários para executar a função.

---

## Knative

- **Definição**:
  - Uma solução padronizada para rodar aplicações serverless.
- **Roda sobre Kubernetes**:
  - Utiliza containers para gerenciar as funções.
  - Kubernetes oferece:
    - **Resolução de DNS**.
    - **Balanceamento de carga** para serviços.
    - **Escalonamento automático** de serviços.

---

## Exemplo de `Dockerfile` para Knative

```dockerfile
# imagem base do Python como exemplo
FROM python:3.9-slim

# o diretório de trabalho
WORKDIR /app

# os arquivos necessários para a aplicação
COPY . .

# as dependências
RUN pip install -r requirements.txt

# rodar a aplicação
CMD ["python", "app.py"]




Aula 1 e 2 - Vinicius Soares

Contexto

    SOA - Service; Oriented; Archeitecture
    SOA é uma abordagem arquitetural corporaiva que permite a criação de serviços de negócio interoperáveis que podem ser facilmente reutilizados e compartilhados entre aplicações e empresas.

    Reusabilidade;

    Benefício do SOA
        DEesacoplamento = Integrações inteligentes
        Reutilização de serviços
        Infraestrutura de plataforma

    Monólito x Microservices

    Monolito = Típica de um sistema complexo - Implementadas em um único processo.
        Fácil de desenvolver;
        Fácil manutenção;
        Apenas um deploy;
        Tráfego de rede baixo;

    Problemas:
        Aumeno de complexidade e tamanho ao longo do tempo;
        Alta dependência de componentes de código;
        Escalabilidade do sistema é limitada;
        Falta de flexibilidade;
        Dificuldade para colocar alterações em produção;

    Microserviço:
        Manutenção e evolução dos serviços mais estáveis;
        Serviços com baixo nível de acoplamento e interdependência;
        Escalabilidade do sistema;
        Redução de custos;
        Flexibilidade de tecnologia;
        Facilidade de colocar alterações em produção
        Resiliencia;
        Amento da produtividade;
        Implementação de entrega contínua;
        Monitoramento e automação de processos;
        Foco na entrega de valor ao cliente;

    RISCOS: Aumento da complexidade da coordenação; Comunicação entre os microsserviços; Governança;

    Características principais
        Newman, Sam; "Um conjunto de pequenos autônomos que trabalham juntos"

        Software modularizado;

        API RESTFULL - Comunicação (HTTP - JSon)

        Out-of-process - Possibilidade de execução fora dos processos;

    Chamadas remotas - Microsserviços são acessados por chamadas remotas.
    Independente de linguagem de programação.

    Baixo acoplamento. Você é dono somente do seu domínio de negócio.

    Escalabilidade horizontal e vertical;

    Características Organizacionais
        Agilidade
        Equpe pequena e focada = TWO PIZZAS team
        
PRÁTICAS RECOMENDADAS;
    1) Em torno de domínio de empresa
    2) Descentralize tudo.
    3) Cada micro possui seu serviço de dados;

APis bem projetadas. Evite o vazamento de detalhes da implementação.

autenticação, certificado - gateway

ISOLE FALHAS;

### IaaS

      Infra como serviço; 
      Computação de infraestrutura sob demanda.
    3 modelos
        servidores
        storage
        rede
        sistemas operacionais;

    Vai alugar espaços para estes recursos em uma infra externa.

Nuvem pública
Nuvem privada
Nuvem híbrida - vpn

quando usar? quando a demanda for volátil;
             empresas sem capacidade de investimento em hardware

### PaaS

        Plataforma como serviço
        uma camada middleware e/ou componentes prontos
        uma camada de abstração entre seu aplicatio em nuvem
    
    Plataforma e um ambiente para permitir que os desenvolvedores criem aplicativos e serviços da internet;

    Desenvolvimento 100% focado no negócio;
    Produtividade
    Menos custo e mais entregas contra o efeito lock-in (é usado para se referir a um cenário em que você adquire uma solução tecnológica e depois se vê impossibilitado de trocá-la por outra, estando trancado dentro dela).

THE TWELVE

    1) Base de Código
    2) Dependências - Declare e isole explicitamente as dependências; Tenha sempre um gerenciador de dependências configurado para seu projeto (maven, gradle, npm, pip e etc)
    3) Configurações - A troca de ambiente não pode afetar a sua aplicação;
    4) Serviços de Apoio
    5) Construa, Lance e execute
    6) Processos
    7) Vínculo de porta;
    8) Concorrência (Divida seu aplicativo em pequenos pedaços)
    9) Descartabilidade;
    10) Paridade entre desenvolvimento e produção;
    11) Logs - Fluxo de Eventos;
    12) Processos Administrativos;

    Aplicações - CLOUD NATIVE
        Definição
            Containerrizado
            Gerenciado
            Orientado a microserviços
            Cloud

Containers
    Pequenos sistemas LINUX
    Compartilhado KERNEL
    Compartilhamento de ambientes customizados
Pq os contêineres são bons para micro serviços? 
    Compartilhar o SO e Bibliotecas

    Docker

Maturidade com CLOUD NATIVE
    Muito novo e a maioria das empresas não têm experiência para navegar por conta própria. É muito fácil e caro cometer erros.
    AS-IS TO BE onde você está agora e onde ir a partir daqui

Nível
3 - Cloud Native
2 - Cloud Resilient
1 - Cloud Friendly
0 - Cloud Ready

Particionamento de SERVIÇOS

    Domain DRIVE DESIGN: Eric Evans - DDD é uma abordagem que reúne um conjunto de boas práticas, padrões, ferramentas e recursos da orientação a objetos que têm como objetivo a construção e desenvolvimento de sistemas de acordo com o domínio e regras de negócio do cliente.
    DDD - MODELO
    Domínio e negócio do cliente;
    Linguagem onipresente, arquitetura em camadas e os padrões;
    
    Modelo é evolutivo; A cada sprint; 

### EVEN STORMING = É uma técnica de desing rápido;

Mapeando os Eventos
Identificando os Comandos
Associando os Aggregates
Delimitando as Fronteiras do Modelo e 
Identificando Domínios de Negócio

COMUNICAÇÃO

    Síncrona - Rest, SOAP, CDI
    Assíncrona - Mensagens, eventos, replicação de base;

Comunicação orientada a eventos

    usuário - 4 segundo até a aplicação renderizada;
    
CQRS - Complexo



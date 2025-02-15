Aula 1 e 2 Manoel Veras

DATACENTER para a NUVEM;

Arquitetura HYPERSCALE;

3 maiores - AMAZON, MICROSOFT e GOOGLE;

MUDANÇA nas NUVENS.

Troca de despesas de capital por despesas variáveis.

Economia de escala.

Parar de especular sobre a capacidade.

Aumento da velocidade e agilidade.

Chega de gastar dinheiro para executar e operar datacenters.

Torna-se global em minutos.

Arquitetura? Arquitetura Tecnológica
    Arquitetura de NUVEM
    Arquitetura do DATACENTER

Multinancy - Multi-Inquilino;

Containers são modelo de Virtualização com objetivo de implatar e executar aplicativos distribuídos

VMs x Containers 
    Docker e Kubernetes(gerenciamento)

Como se define uma arquitetura de nuvem? 
    Requisitos do Negócio - Frameworks
        TOGAF (referência) - Open group
            ADM

Arquitetura tem muito haver com planejamento

Como se define uma arquitetura de nuvem? 
    
    Arquitetura de Referência (AR): É um documento que contém um conjunto de boas práticas que deve ser utilizado por todos os membors de uma organização.
    NIST - Arquitetura usada como padrão

Atores - Broken (terceiro) compra serviço de AWS, Microsoft

Cloud Consumer - Principais stakelholders do serviço de nuvem.

Cloud Auditor - Segurança, privacidade e perfomance.

Cloud Provider - Entidade responsável por manter os serviços da nuvem disponíveis para as partes interessadas. tendo pública, privada e híbrida. Prover e gerenciar o acesso. Inclui recursos de hardware, rede, componentes de armazenamento e etc. Controles. Cloud Service Management. Business Suport (Accountability). Provisionamento e Configuração. Portabilidade e Interoperabilidade. Segurança. Privacidade.
Qual modelo? SAAS IASS PAS

Cloud Broker - Entidade que gerencia o uso, o desempenho e a entrega dos serviços entre um cliente e um ou mais provedores de nuvem; 

Cloud Carrier - Fornece os meios para o consumidor acessar o provedor de nuvem (Exemplo: provedores de acesso a internet).

Exemplo: Arquitetura da IBM;

Requisitos técnicos.
    Busca de Padrão.
    Padrão da Arquitetura de Nuvem
    Elementos Essenciais
    Catálogo de padrões. Cloudpatterns

Sines 4.0 de Portugal... data center escalável, atender diversos clientes no mundo inteiro. Isolamento entre as partes. Sines no Brasil? Lugares mais frio. Apoio político.

Brasil.. Microsoft e AWS. Google ainda não.. chile.

Santander em campinas, tecnologia avançada;

Aspectos essenciais da Arquitetura em Nuvem (Princípios)

    1) Otimização de Custos - Pode até ficar mais caro é preciso analisar; Plataformas tem ferramentas. Gerenciamento Financeiro;
    
    2) Excelência Operacional - Trabalhando de forma correta; 
        Antecipar falhas; Testes;
    
    3) Eficiência de Performance - Atender os requisitos;
        Monitorar; Usar tecnologias avançadas; Usar containers;

    4) Confiabilidade - Data Center replicado; Recuperar falhas automaticamente; Escalabilidade; Disponibilidade - Estudo; Cálculo de disponibilidade com dependências rígidas. Cálculo de disponibilidade com componentes redundantes;

    5) Segurança - Especialistas em seg. da nuvem; Implenmentar uma base sóldia de identidade e se preparar para a segurança;


Multi-Cloud e Broken;

Plataformas 

Amazon - AWS = Precursora na NUVEM; 2006; Prós= Maior força do mercado. Novos Produtos e Serviços; Contra= Custos, as empresas não entendem muito bem.
Bare-Metal Server; Tem seu próprio Banco de dados; Firewall e segurança na rede; 

Microsoft Azure = É a que mais conseguiu chegar perto da AWS. Vantagem pq tem os outros apps; Ligação entre eles; Machine Learning;

GCP = Google Cloud Platform; IaaS e PaaS; 10% do mercado; Principal fator custos. Permite criar as VMs. Pionerio em cobrança por segundos; BigTable;

oracle, alibaba, IBM; procurando nichos;

Case de ambiente monolítico para Nuvem; Empresa de Delivery precisavam melhorar. Durante os picos a solução caia e agora a aplicação é escalável; Tiveram um ganho absurdo; Elasticidade da INFRA; Redundância dos serviços; Backups; Paga pelo uso; Autoscaling;

AWS WA Tool - Tá pensando certo ou não?

Vendor Lock In. Pensar bem, para não pagar o preço;


Aula 03 - Tiago Coelho Ferreto

Histórico - 

*Virtualização Anos 60 e 70 - IBM System/360
*Internet (Anos 70 e 80) - ARPANET
*PCs e Supercomputadores (anos 80 e 90)
*Grid Computing (anos 90 e 2000) - vários clusters
*Virtualização (anos 90 e 2000) - VMware

Nuvem pq? 
-Reduzir os investimentos com infraestrutura
-Evitar a subutilização de recursos
-Necessidade de uma plataforma única

O que é Computação em NUVEM?
    é um modelo pay-per-use para permitir o acesso a rede sob demanda.

    self-service - processo automatizado

    elasticidade

    multitenant - ambiente compartilhado (isolado)

    Modelos de serviço

        SaaS - aplicação e infra - tudo responsabilidade do provedor
        PaaS - desenvolver apps
        IaaS - recursos operacionais básicos

Modelos de implantação

Nuvem pública - Estrutura compartilhada.
    
    AWS (nuvem: netflix)
    
    Microsoft (walmart, linkedin, boeing)

    Google (snapchat, airbnb e paypal) - autoelasticidade
    
    Outras (ibm cloud, oracle, alibaba cloud)

São datacenters espalhados pelo mundo. 

Evolução
    Colocation
    Densidade
    Containers
    Modular
    SW defined - Gerencia por software

Power usage efective - PUE

Serviços de NUVEM
    Principais Serviços
        
        1) Computação

                a) Máquina Virtual - EC2, Azure Virtual e Google. 
                (Imagem base, tipo de instância, rede, disco, escalabilidade vertical x horizontal)
                
                b) Container (Provisonamento de aplicações) Hospedagem das imagens no register. Kubernetes (orquestrar os containers)

                c) função como serviço (computação sem servidor)

        2) Armazenamento
                
                a) baseado em objetos (Armazenaento de arquivos) Cloud Storage
                b) baseado em bloco
                c) sistema de arquivos distribuídos (arquivos compartilhados entre diversas instâncias)
                d) banco de dados gerenciados pelo povedor de nuvem. Amazon RDS, Azure SQL, Cloud SQL
                
        3) Comunicação
                a) Rede virtual privada (não existe acesso externo) Amazon VPC
                b) Load balancer
                c) CDN - Content Delivery Network. Rede rápida para distribuição de conteúdo. Clientes acessam conteudo amis próximo. Menos latência. Menos tráfego. Amazon CloudFront. Azure CDN. Cloud CDN.

        4) Segurança
                a) Controle de acesso (quem vai conseguir acessar a nuvem). Usuários, chaves. Least privilege principie.

    Serviços avançados de nuvem
        
        Big Data Analytics - Hadcop e Spark
        
        Edge Computing - Computação na borda; aproximar os dados do usuário; AWS local zones;

    Outros serviços
        AWS Cloud Formation
        Amazon Managed Blockchain
        Amazon HoneyCode
        AWS CodeBuild
        Amazon WorkSpaces
        AWS IoT Core
        Amazon Gamel.ift
        
Soluções, Arquiteturas e Custo na nuvem

Certificações em Nuvem
    Exames
        AWS (11)
        Azure

Nuvem privada

    Azure Stack. Alocar localmente as nuvens.
    OpenStack.

Cloud Native Computing
 é uma abordagem para criar e executar aplicativos que exploram totalmente as vantagens do modelo de computação em nuvem.

 Cloud Foundry

Nuvem híbrida





Aula 1 e 2 - Andrea Konzen

Histórico
1970 - ARPANET
1983 - Protocolo TCP/IP
1991 - HTML - WWW
2000 - Meio fundamental de comunicação

Web 1.0 (estática): criação na mão de poucos.

Web 2.0 (interativa): público virou criador de conteúdo

Web 3.0 (interativa inteligente): Inteligência artificial; Personalização;

**Arquitetura Web e características**

Conjunto de padrões, princípios, técnicas e boas práticas utilizados para projetar e desenvolver sistemas e aplicações web.

1) Estrutura
2) Componentes da aplicação
3) Regras
4) Protocolos de comunicação entre os componentes

Estruturação HTML + CSS
Integração com back-end
Escolha de ferramentas e tecnologias apropriadas (escalabilidade, desempenho, segurança)

Arquiteturas 

Cliente-servidor - 3 camadas - Front-end; back-end; banco de dados;

Orientada a serviços (SOA) - Serviços independentes. Cada serviço é responsável por um tarefa específica. Serviço que pode ser acessado por outros componentes. Mais flexíveis.

Baseada em microserviços - Dividida em microsserviços independentes que se comunicam entr si por meio de APIs. Podem ser facilmente substituídos ou atualizados sem afetar o restante do sistema. Maior tolerância a falhas.
Permite que cada microserviço seja desenvolvido com a linguagem de programação e tecnologia mais adequadas para a funcionalidade específica. 

Aplicações WEB -
Estrutural - Informações importantes (requisitos)
Navegacional - Navegação ao sistema
Apresentação - Para o usuário

Protocolos - É uma convenção que controla e possibilita conexão, comunicação, transferência de dados entre dois sistemas computacionais. Responsaveis por coletar os dados transmitidos pela rede e dividí-los em pequenos pedações (Origem e destino)

Sintaxe-Semantica e Timing

Protocolos de Internet
TCP-IP - Padrão da internet. Usado para transmitir dados entre dispositivos em redes.
HTTP-HTTPS - Transferência de hipertexto.
FTP - Transferência de Arquivos
DNS - Nomes de domínios em IP
SMTP-POP3-IMAP - Enviar e receber e-mail (correio simples)
ICMP - 

-REDE 5 camadas

1 aplicação (HTTP; FTP; SMTP; DNS; SSH; TLS): Responsável por toda comunicação entre aplicativos em diferentes dispositivos de rede. Define formatos de mensagens e regras de comunicação.

HTTP: Transferência de dados na WEB.
HTTPS: Camada adicional de segurança (TLS) - Conexão criptografada.
FTP: Transferência de Arquivos
SMTP: Transferência de e-mails (Envio)
DNS: Tradução de nomes de domínio em endereços IP.
SSH: Comunicação segura entre computadores (Criptografia) - Acesso remoto seguro, transferência seguro, acesso banco de dados
TLS: Criptografia de dois computadores. Compras online e dados bancários. 

2 transporte (TCP e UDP) Comunicação confiável e eficiente. Sem erros e em ordem correta e com uma velocidade adequada.

TCP : Complementado pelo IP. Bastante versátil; Função principal: Verificar se os dados que circulam entre os dispositivos de uma rede são enviados de forma correra e a sequência apropriada. Confiabilidade dos dados. 

UDP : Envie datagram IPV4 e IPV6 sem garantias que o pcaote chegue. Voltado para velocidade - Voz, Jogos.

3 rede
4 enlace
5 física

_____
Frontend

Front-end não é designer; Front-end (HTML, CSS, Javascript)
tags do HTML <html> <head> <title> <body>
CSS - Estilo Visual; Responsiva; style.css
Java Script: Interatividade com usuário
Vue.js: framework front-end

Back-end

Fica por trás. lógica de negócia. Conjunto de elementos: sistemas, banco de dados entre outros.
PHp,PHYTON, RUBY, Node.js
Banco de dados: MySQL e Postgre
frameworks disponíveis.

Tipos de Sistemas WEB 
    
    **SPA (Sigle Page Application): é um modelo de desenvolvimento. Única página web. O conteúdo todo. Mais rápida e Mais fluida.
    AJAX: Chamada Assincrona
    E-Commerce, Rede sociais, jogos online.
    Redução da Carga do Servidor
    Melhor escalabilidade e manutenibilidade
    Maior interatividade e personalização
    Benefícios: Velocidade.Melhor experiência. Desenvolvimento mais fácil. Arquitetura modular. Acesso off-line. Maior segurança. Facilidade de manutenção. 
    1 paǵiana HTML e usa JavaScript e AJAX
    Arquitetura: View; Modelo; Controlador; Serviços; Roteamento; Gerenciador de estado; Bibliotecas e frameworks;
    Exemplo: GMAIL
    
    **MPA (Multi Page Application): cada página é carregada como uma página separada, com sua URL, e as ações do usuário geralmente exigem o carregamento de uma nova página. Várias páginas HTML independentes. 
    Mecanimos de busca são mais amigáveis.
    Manutenção mais fácil.
    Rápido tempo de carregamento. Apenas o necessário.
    Boa usabilidade.
    Desvantagens: Transições mais lentas. Requisições de servidor. Dificuldade mem gerenciar o estado do aplicativo. 
    Arquitetura: Cada página é carregada em resposta a uma requisição do cliente.
    Exemplo: AMAZON

    **PWA (Progressive Web APP): São aplicativos web que oferecem uma experiência de usuário semelhante à de um aplicativo móvel nativo mas que são executados em um navegador da web. Combinação entre um "site" e um aplicativo móvel.
    Acessibilidade e facilidade de desenvolvimento
    Pode ser encontrada em mecanismos de busca
    URL
    Aprimoramento progressivo
    Enviar notificações
    SER RESPONSIVA.. diferentes dispositivos.
    Sempre HTTPS
    Instalação fácil. não requer download 
    Benefícios: Desenvolvimento mais rápido e fácil, custos reduzidos. Fácil manutenção. Multiplataforma. Melhor experiência do usuário. Fácil distribuição.
    Service Workers: Scripts em segundo plano. 
    Manifesto da Web em PWA é um arquivo JSON que contém informações sobre a aplicação web progressiva como: nome, ícone, cor de tema, orientação de tela, entre outras. É importante para que a PWA possa ser adicionada à tela inicial do dispositivo e se comportar de forma semelhante a um aplicativo nativo.
    Exemplo: Twitter Lite; starbucks; 

    //Projeto para WEB: Serve para ter um modelo e ganhar em qualidade.

    TOPO da pirâmide (Usuário)
    1) Projeto de interfaces
    2) Projeto estético (ou de layout)
    3) Projeto Conteúdo
    4) Projeto de Arquitetura - Modelos
    5) Projeto de Navegação
    6) Projeto em nível de componentes
    BASE da pirâmide (tecnologia)
    
   Exemplo prático: Projeto de mobilidade para desenvolvimento WEBAPPS
    
    Aplicativo de delivery de comida;

Conceitos HTML

Elementos, etiqueta (TAG) e atributos.

Tag simples e Tag dupla;

Acentos <meta charset="UTF-8"> dentro do HEAD

Formulários <form>

CSS
JavaScript client side
Manipulação do DOM; adicionar remover Formato de árvore. Pai, filhos e irmãos

Aula 3 - Luiz Fernando Palanella Gonzalesz.


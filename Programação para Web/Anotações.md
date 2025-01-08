# **Aula 1 e 2 - Andrea Konzen**

## **Histórico da Web**
- **1970:** ARPANET.
- **1983:** Protocolo TCP/IP.
- **1991:** HTML e World Wide Web (WWW).
- **2000:** Tornou-se meio fundamental de comunicação.

## **Evolução da Web**
1. **Web 1.0 (Estática):** Criação de conteúdo na mão de poucos.
2. **Web 2.0 (Interativa):** Usuários passaram a ser criadores de conteúdo.
3. **Web 3.0 (Interativa Inteligente):** Uso de inteligência artificial e personalização.

---

## **Arquitetura Web e Características**
Conjunto de padrões, princípios, técnicas e boas práticas para projetar e desenvolver sistemas e aplicações web.

### **Componentes Principais**
1. **Estrutura.**
2. **Componentes da aplicação.**
3. **Regras.**
4. **Protocolos de comunicação.**

### **Práticas Importantes**
- Estruturação com HTML e CSS.
- Integração com back-end.
- Escolha de ferramentas e tecnologias apropriadas (escalabilidade, desempenho, segurança).

---

## **Arquiteturas Web**
1. **Cliente-Servidor (3 camadas):**
   - **Camadas:** Front-end, back-end, banco de dados.
2. **Orientada a Serviços (SOA):**
   - Serviços independentes, responsáveis por tarefas específicas.
   - Mais flexível e acessível por outros componentes.
3. **Baseada em Microserviços:**
   - Dividida em microsserviços independentes que se comunicam via APIs.
   - Alta tolerância a falhas e flexibilidade na escolha de tecnologias.

---

## **Tipos de Aplicações Web**
### **SPA (Single Page Application):**
- **Descrição:** Única página web com atualizações dinâmicas via JavaScript e AJAX.
- **Benefícios:**
  - Maior interatividade e personalização.
  - Melhor escalabilidade e manutenção.
  - Acesso offline e maior segurança.
- **Exemplo:** Gmail.

### **MPA (Multi Page Application):**
- **Descrição:** Cada página é carregada separadamente com URLs distintas.
- **Benefícios:**
  - Amigável para mecanismos de busca.
  - Tempo de carregamento rápido.
- **Desvantagens:**
  - Transições mais lentas.
  - Mais requisições ao servidor.
- **Exemplo:** Amazon.

### **PWA (Progressive Web App):**
- **Descrição:** Aplicativos web que funcionam como apps nativos, executados no navegador.
- **Benefícios:**
  - Fácil manutenção e multidevices.
  - Funcionalidade offline via Service Workers.
  - Manifesto Web (JSON) para informações como ícone e tema.
- **Exemplo:** Twitter Lite, Starbucks.

---

## **Protocolos de Internet**
- **TCP/IP:** Padrão para comunicação de dados em redes.
- **HTTP/HTTPS:** Transferência de hipertexto. HTTPS oferece camada extra de segurança (TLS).
- **FTP:** Transferência de arquivos.
- **DNS:** Tradução de nomes de domínio para endereços IP.
- **SMTP/POP3/IMAP:** Envio e recebimento de e-mails.
- **SSH:** Comunicação segura com criptografia.

---

## **Estrutura da Rede (Modelo de 5 Camadas)**
1. **Aplicação:** Protocolos como HTTP, FTP, DNS, SSH.
2. **Transporte:**
   - **TCP:** Comunicação confiável e ordenada.
   - **UDP:** Comunicação rápida, sem garantia de entrega.
3. **Rede:** Roteamento e envio de pacotes.
4. **Enlace:** Comunicação entre dispositivos conectados.
5. **Física:** Transmissão de dados no hardware.

---

## **Front-End**
- **Tecnologias:** HTML, CSS, JavaScript.
- **Frameworks:** Vue.js.
- **HTML:**
  - Tags como `<html>`, `<head>`, `<title>`, `<body>`.
- **CSS:** Estilo visual e responsividade.
- **JavaScript:** Interatividade com o usuário.

---

## **Back-End**
- **Definição:** Lógica de negócios, sistemas e banco de dados.
- **Tecnologias:** PHP, Python, Ruby, Node.js.
- **Bancos de Dados:** MySQL, PostgreSQL.

---

## **Web Design e Acessibilidade**
- **Web Design Responsivo:**
  - **Responsivo:** Uso de CSS (Media Queries).
  - **Adaptativo:** Renderização baseada no servidor.
  - **Mobile-First:** Priorizar dispositivos móveis no design.
  - **Breakpoints:** Padrões definidos, como os do Bootstrap e Material Design.
- **SVG (Scalable Vector Graphics):** Imagens vetoriais escaláveis.
- **Tema Escuro:**
  - Reduz fadiga visual e afeta menos o sono.
  - **CSS Media Query:** `prefers-color-scheme`.
- **Animação Reduzida:**
  - `@media (prefers-reduced-motion: reduce)`.

---

## **Boas Práticas**
- **Semântica no HTML:** Melhorar acessibilidade e SEO.
- **Atributos ARIA:** Tornar aplicações acessíveis.
- **Shadow DOM:** Isolar componentes no DOM.
- **Web Components:** Criar componentes reutilizáveis e independentes.

---

## **Ferramentas e Conceitos Adicionais**
- **Lighthouse:** Geração de relatórios de desempenho e acessibilidade.
- **Bootstrap e Material Design:** Componentes para design responsivo.
- **Service Workers:** Scripts que permitem funcionalidade offline em PWAs.
- **W3C e WAI:** Definem padrões para acessibilidade na web.

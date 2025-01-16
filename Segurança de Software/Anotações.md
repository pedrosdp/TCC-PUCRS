# Segurança de Software

## Aula 1 e 2 - Moises Brandalise

### Por que a segurança é importante no desenvolvimento de software?

- **Migração dos serviços em nuvem**

### SQL Injection
- Técnica usada para explorar vulnerabilidades em sistemas que utilizam a linguagem SQL para se comunicar com um banco de dados.
- Consiste na inserção de códigos maliciosos em campos de entrada de formulários de uma aplicação web.

### Valor do Dado (LGPD)

- A **IBM** publicou um relatório mostrando que o setor de **manufatura** é o mais atacado.

### Kaspersky
- Dados sobre detecção:
  - Centro de controle - Detecções por segundo.
  - O **Brasil** é o **3º país com mais tentativas de ataques**, sendo o **primeiro** o ataque de força bruta no **RDP**.

---

## Principais Riscos de Segurança

1. **Ataques Hackers**
2. **Vazamento de dados**
3. **Ataques de Phishing**
   - Utilizam **engenharia social**.
4. **Malware**
   - Infecta aplicativos.

---

## Principais Organizações - Recursos e Orientações

1. **ISO (Organização Internacional de Normalização)**
   - Padronização de normas: **27001**, **27002**, **27034**.
   
2. **W3C (Consórcio WWW)**
   - Padrões para **HTML**, **CSS**, e o protocolo **HTTPS**.

3. **OWASP**
   - Organização de voluntários.
   - Fornece:
     - **10 principais vulnerabilidades**.
     - **Melhores práticas de segurança**.

4. **NIST (National Institute of Standards and Technology)**
   - Agência americana voltada ao desenvolvimento seguro.
   - Pioneira em **cibersegurança**.
   - Empresas que trabalham com o governo dos EUA devem cumprir rigorosos padrões de segurança.

5. **IETF (Internet Engineering Task Force)**
   - Padronização de **criptografia**.
   - Trabalha com protocolos como **TLS** e **IPSec**.

6. **PCI SSC (Payment Card Industry Security Standards Council)**
   - Define padrões de segurança para empresas que processam pagamentos.


# Criptografia

## Definição
- É importante para garantir a **privacidade** e a **integridade** das informações.
- **Criptografia** transforma informações para protegê-las.

---

## Chaves Criptográficas
- A criptografia utiliza **chaves** para codificar e decodificar informações.
- Uma **chave** é um valor secreto usado para transformar a informação.

---

## Tipos de Cifras

### Cifras Simétricas
- Utilizam a **mesma chave** para codificar e decodificar.
- **Vantagens:**
  - Velocidade (consomem menos recursos computacionais).
  - Boa para segurança em comunicações e aplicações financeiras.

### Cifras Assimétricas
- Utilizam um **par de chaves diferentes**:
  - **Chave Pública:** Pode ser distribuída livremente.
  - **Chave Privada:** Deve ser mantida em segredo.
- **Aplicações:**
  - Certificado digital.
  - Assinatura digital.
  - Garantia de autenticidade e integridade.

---

## HASH
- Um método de criptografia que usa um algoritmo matemático para transformar uma mensagem em uma string de caracteres fixa.
- **Aplicações:**
  - Em jogos: Geração de números aleatórios para personagens, objetos e eventos.
  - Tecnologias **Blockchain**.
- Exemplos: **AES** e **SHA256**.

---

## Implementação Correta de Algoritmos de Criptografia
1. **Dados em repouso**: Proteção de dados locais (ex.: BitLocker da Microsoft).
2. **Dados em movimento**: Comunicação segura (ex.: VPN).

---

## Cofres de Senhas
- Ferramentas para armazenar senhas de forma segura.
- Podem ser softwares ou hardwares.
- **Exemplos:**
  - Vault, Azure, AWS, etc.
- Facilitam a gestão do ciclo de vida das senhas.

---

## Prevenção de Ataques

### Salting
- Técnica usada para proteger senhas em bancos de dados.
- Adiciona um valor único e secreto (salt) a cada senha antes de criptografá-la.

### Hashing
- Processo matemático que converte um bloco de dados em um valor de comprimento fixo.


# Teste e Auditoria

- **Revisão de Código**: Identificação e correção de erros ou conflitos no código.
- Exemplo de papéis:
  1. **Escrita do código**: Desenvolvedor (1ª linha).
  2. **Auxílio**: Revisão ou suporte de equipe (2ª linha).
  3. **Auditoria**: Testes para validação (3ª linha).

---

## Padrões de Criptografia

1. **AES** (Advanced Encryption Standard)
2. **RSA** (Rivest-Shamir-Adleman)
3. **SHA** (Secure Hash Algorithm)

---

## Protocolos de Comunicação Segura

### Modelo Referencial OSI
- Conjunto de regras e procedimentos para comunicação entre dispositivos de rede.
- É um modelo teórico que define **sete camadas**, descrevendo como os dispositivos devem interagir.

### As 7 Camadas do Modelo OSI

1. **Aplicação**: Interfaces com aplicativos.
2. **Apresentação**: Formatação de dados e criptografia.
3. **Sessão**: Controle de sessões entre aplicativos.
4. **Transporte**: Gerenciamento de conexões entre hosts/portas.
5. **Rede**: Gerenciamento de endereços lógicos e roteadores.
6. **Enlace**: Gerenciamento de endereços físicos, pontes e switches.
7. **Físico**: Hardware e sinais elétricos.

---

## LibSignal
- Biblioteca usada para implementar **criptografia de ponta a ponta**.
- Amplamente utilizada em aplicativos de mensagens seguras.

# Segurança no Desenvolvimento de Software

## Identificação dos Riscos de Segurança e Vulnerabilidades
- Analisar as ameaças
- Identificar ativos
- Avaliar as vulnerabilidades
- Avaliar o impacto
- Classificar os riscos
- Plano de mitigação
- Monitoramento

## Gerenciamento de Vulnerabilidades e Riscos
- Responsável
- Testes regulares
- Acompanhar as mudanças
- Treinamento

## Integração da Segurança no Processo
- **DEVSECOPS**: Desde o início do projeto
- Utilizar ferramentas:
  - **Snyk**: Ferramenta de segurança que ajuda a proteger aplicativos e bibliotecas de terceiros contra vulnerabilidades conhecidas.
  - **Waspzap**: Software que oferece uma plataforma de comunicação segura e criptografada para smartphones Android. É um fork do aplicativo de mensagens instantâneas Signal.
- Conjunto de diretrizes a serem seguidas

## Treinamento e Conscientização dos Desenvolvedores
- Treinamentos
- Materiais
- Revisão conjunta de código
- Checklist:
  - Validação de entrada
  - Gerenciamento de sessão
  - Proteção contra injeção de código
  - Gerenciamento de senhas
  - Configuração do servidor
  - Controle de acesso
  - Proteção de dados
- Recompensas

## Bughunt
- Recompensas para vulnerabilidades

## Ciclo de Vida
1. Identificar ativos
2. Análise de riscos
3. Requisitos de segurança
4. Políticas de segurança
5. Testes de segurança
6. Revisão

## Projeto e Implementação Seguros
- **Spoofing**: Falsificação de identidade
- **Tampering**: Violação ou adulteração
- **Repudiation**: Negação de ter realizado uma ação
- **Information Disclosure**: Divulgação ou vazamento de informações
- **Denial of Service**: Negação de serviço
- **Elevation of Privilege**: Aumento indevido de privilégios

## Testes de Segurança e Avaliação
- Testes de invasão
- Análise de vulnerabilidades

## Implantação e Manutenção Seguras
- Configuração de servidores
- Autenticação e autorização
- Monitoramento

## Análise de Código Estática e Dinâmica
- **Estática (SAST)**: Análise do código fonte
- **Dinâmica (DAST)**: Análise durante a execução da aplicação
- **Soluções Estáticas**: SonarQube, Veracode, ESLint, PMD, FindBugs
- **Soluções Dinâmicas**: Burp Suite, OWASP ZAP, Acunetix, Qualys, IBM AppScan

## Teste de Invasão e Avaliação de Vulnerabilidades
- **Tipos**:
  - Blackbox
  - Whitebox
- **Escopo**:
  - Vulnerabilidades
  - Testes SQL
  - Outros
  - Documentação

## Gerenciamento de Configuração Segura
- Com o **Ansible**, é possível realizar a instalação de patches de segurança em todos os servidores em execução.
- **Ferramentas**: Ansible, Chef, Puppet

### Ansible
1. Configuração e implantação
2. Teste de segurança automatizado
3. Gerenciamento de vulnerabilidades
4. Monitoramento de segurança
5. Auditoria e conformidade

## Autenticação e Autorização Seguras
- Garantir que apenas usuários autorizados tenham acesso à aplicação e aos dados sensíveis
- **Protocolos**:
  - OAuth
  - OpenID Connect
  - JWT
- **SSO** (Single Sign-On)
- Multifator
- Permissões:
  - Role-Based
  - Rule-Based
- Monitoramento
- Atualização
- **SALT** armazenado em outro local (outra tabela)

## Criptografia e Gerenciamento de Chaves
- Cofres:
  - HashiCorp Vault
  - Amazon Web Services (AWS) Key Management Service (KMS)
  - Microsoft Azure Key Vault
  - Google Cloud Key Management Service (KMS)

# Monitoramento e Detecção de Incidentes
- **Planejamento**
- **Coleta de Dados**
- **Correlação**
- **Notificação**
- **Investigar e Responder**

---

# Problemas Comuns de Segurança Indicados pela OWASP e TOP 10

## O que é OWASP
- Organização que mantém uma lista atualizada de problemas de segurança em aplicativos da web.
- Baseada em **dados reais** e nas **25 fraquezas do CWE**.

### Principais Problemas de Segurança:
1. Quebra de controle de acesso
2. Falhas criptográficas
3. Injeção (ex.: injeção de código malicioso, injeção SQL)
4. Design inseguro
5. Configuração de segurança incorreta
6. Componentes vulneráveis e desatualizados
7. Falhas na identificação e autenticação
8. Falhas na integridade de software e dados
9. Falhas no registro e monitoramento
10. Falsificação de solicitação do lado servidor (SSRF)

---

# Autenticação e Autorização

## Autenticação
- Processo de verificar a identidade de um usuário ou sistema.
- **Métodos de Autenticação**:
  - Senhas
  - Smart cards e outros dispositivos
  - Biometria

## Autorização
- Conceder ou negar permissões de acesso a recursos.
- **Controle de Acesso**:
  - Granularidade
  - Baseada em funções (Role-Based) ou regras (Rule-Based)
  - Permissões específicas

---

## Métodos de Autenticação
- **Algo que o usuário sabe** (ex.: senha)
- **Algo que o usuário possui** (ex.: smart cards)
- **Algo que o usuário é** (ex.: biometria)

### Outras Abordagens:
- **Multifator Adaptativo**
- **Passwordless** (sem senha)

---

# Implementação
- **Sistemas de Gerenciamento de Usuários**
- **Controle de Acessos**

---

## Protocolos e Ferramentas
- **Protocolo LDAP**: Gerenciamento de diretórios e serviços de diretório.
- **WSO2**: Plataforma para gerenciamento de identidade e autenticação.

# Aula 3 - Avelino Francisco Zorzo

## Contexto Atual e Segurança

### Criptografia
- **Defesa - Ataque - Teoria - Prática**
- "Na prática, eu tenho segurança se for bem feito."  
  — *Avelino Francisco Zorzo*

---

## Dois Problemas Práticos
1. **Engenharia Social**:  
   - Ataque simples utilizando WhatsApp.
2. **Heartbleed**:  
   - Vulnerabilidade no HTTPS baseada na suposição de que todos seriam honestos.

---

## Segurança - Metas
1. **Privacidade**  
   Garantir que os dados sejam acessíveis apenas a quem tem permissão.
2. **Autenticação**  
   Verificar a identidade de usuários ou sistemas.
3. **Integridade**  
   Garantir que os dados não sejam alterados ou corrompidos durante a transmissão.
4. **Não-repúdio**  
   Garantir que as ações ou comunicações não possam ser negadas posteriormente.

Criptografia como funciona

  
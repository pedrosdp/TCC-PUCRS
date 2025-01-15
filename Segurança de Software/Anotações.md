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

Segurança no DESENVOLVIMENTO DE SOFTWARE





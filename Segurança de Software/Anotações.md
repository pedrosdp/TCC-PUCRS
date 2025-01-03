Segurança de Software

Aula 1 e 2 - Moises Brandalise

Por que a segurança é importante no desenvolvimento de software...

**Migração dos serviços em núvem

**SQL INJECTION - Técnica usada para explorar vulnerabilidades em sistemas que utilizam a linguagem SQL para se comunicar com um banco de dados, que consiste na inserção de códigos maliciosos em campos de entrada de formulários de uma aplicação web.

**Valor do Dado (LGPD)

IBM publica Ramos da indústria ataque (MANUFAtURa é o Maior)

KASPERSKY - Centro de controle - Detecções por segundo. Brasil é 3º mais tentativa de ataques.
Sendo o primeiro o ataque de força bruta no RDP.

Principais riscos de segurança.
1) Ataques Hackers
2) Vazamento de dados
3) Ataques de Phishing (Utiliza de engenharia social)
4) Malware - Infecta app

Principais Organizações -  Recursos e orientações

1) ISO (Organização Internacional de Normalização) - Padronização de normas 27001/27002/27034
2) W3C - Consórcio WWW - html, css, protocolo https;
3) OWASP - Voluntários - 10 principais vulnerabilidades; Melhores práticas;
4) NIST - Agência Americana para desenvolvimento seguro. Cybersegurança. Empresas que trablham com o governo dos EUA são obrigadas a cumprir os rigoros padrôes de segurança;
5) IETF - Padroniza padrões de criptografia. TLS e IpSeC.
6) PCI SSC - Padrão para empresas.

Criptografia: É importante para garantir a privacidade e a integridade de informações.

Quando fala em criptografia, a gente faa em transformar. 

Chave Criptográficas: A criptográficas usa chaves para codificar e decodificar informações. Uma chave é um valor secreto que é usado para transformar a informação.

Cifras Simétricas: Mesma chave
Cifras assimétricas: par de chaves diferentes (Pública e Privada)

Atenção: Não tentem inventar uma criptografia, utilizem os algoritmos que já temos à disposição, em suas últimas versões.

Simétrica: Mesma chave. Velocidade (Menos recurso computacional);Segurança;Financeiras e comunicações

Assimétrica: Par de chaves. Chave pública distribuída livremente. Chave privada mantida em segredo.
Certificado digital;
Assinatura digital; Autencidade e Integridade.

HASH: Uma forma de criptografia que usa um algoritmo matemático para transformar uma mensagem em uma string de caracteres fixa.
Em jogos, as funções hash são usadas para gerar números aleatórios para personagens, objetos e eventos. 
Tecnologias blockchain
AES e SHA256

Implementação correta do algoritmos de criptografia. 
-Dados em repouso (local)
-Dados em movimento
Bitlocker da Microsoft (Dados da máquina criptografados)
VPN (canal seguro de comunicação)

Cofres de senha: software ou hardware; 
Facilita a gestão do ciclo de vida.
Exemplo: Vault, Azure, AWS, etc

Prevenção de ataques
-Salting> técnica de criptografia usada para proteger senhas em banco de dados, que adiciona um valor único e secreto, conhecido como salt, a cada senha antes de criptografá-la e armazena-la˜
-Hashing> procsso matemático que converte um bloco de dados em um valor de comprimento fixo.

Teste e Auditoria: Revisão de código. Conflitos. 
Exemplo: Ao escrever código (1ª linha) pode-se ter o papel de uma empresa (2ª linha auxiliando) e uma auditoria (3ª linha testando).

Padrões de criptografia
AES - Advanced Encryption Standard)
RSA - Rivest-Shamir-Adleman
SHA - Secure Hash Algorithm

Protocolos de Comunicação SEGURA
    Modelos Referencial OSI
Conjunto de regras e procedimentos
É um modelo teórico de rede que define sete camadas diferentes que descrevem como os dispositivos de rede devem se comunicar entre si.

7 camadas
Aplicação - Interfaces com Aplicativos
Apresentação - Formatos/Criptografia
Sessão - Controle de Sessões entre Aplicativos
Transporte - Conexão entre host/Portas
Rede - Endereço lógico/ Roteadores
Enlace - Endereço físico/ Pontes e Switches
Físico - Hardware-Sinal Elétrico

LIBSIGNAL - Criptografia de ponta a ponta;


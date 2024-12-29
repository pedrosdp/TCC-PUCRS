Devops

Aula 1 e 2 - Fabrício Veronez

Desenvolvimento de software

Planejamento (Requisitos); Desenvolvimento; Testes; Implantação (Disponibilizado);

Profissional de Operação - É o cara que vai cuidar do software que está em implantação que está sendo executado. Conhece de infraestrutura. Tem como objetivo manter a solução estável;

Profissional de Desenvolvimento - Conhece profundamente de programação; Tem como objetivo novos recursos. Não tem contato com ambiente de produção; Novas features. 

Devops. Foco no produto na entrega. Comunicação ágil e simplificada. O objetivo é resolver o problema e aprender com ele
3 maneiras: 
*Fluxo (Análise e Otimização do processos; testes; deploy contínuo; entrega de baixo risco). *Feedback (Implementar e coletar métricas; observabilidade; Teste A/B; Feedback dos resultados). 
*Aprendizado Contínuo e Experimentação (Aprender com os erros; experimentação controlada).

Devops: Plan, Code, Build, Test, Release, Deploy, Operate, Monitor;

Twelve Factor Apps (HEROKU) - Automação; Maior portabilidade; Software como serviço;

1. Código Base
Uma aplicação, um repositório. GIT (Desenvolvimento, Homologação e Produção);

2. Dependências (pipe - pyton; npm - node)
Declare tudo explicitamente. Gerenciamento de Pacote;

3. Configuração - Exemplo: Docker
Use variáveis de ambiente. Nunca deixe configurações (como senhas e chaves) no código.

4. Serviços de Apoio - Exemplo: Serviços de Mensageria; Firesytem (Storage);
Trate serviços externos como recursos.

5. Construção, Lançamento e Execução
Separe build, *release* e run.

6. Processos - Aplicação Stateless;
Sem estado nos processos.
Não armazene dados no filesystem local ou memória; use serviços externos.

7. Port Binding
A aplicação deve expor um serviço HTTP.

8. Concurrency (Concorrência)
Escale processos, não máquinas. 

9. Descartabilidade
Inicie rápido, encerre com segurança.
Processos devem iniciar ou parar sem prejudicar o sistema.

10. Paridade entre Ambientes
Ambientes idênticos.
Mantenha desenvolvimento, teste e produção o mais parecidos possível.

11. Logs - Stack de observabilidade;
Trate logs como fluxo de eventos.

12. Processos Administrativos - Migration;
Use processos únicos para tarefas manuais.
Scripts administrativos (migrar banco, depurar) devem ser separados do código principal.

Versionamento de código; Git - Github

Chave SSH - forma eficiente de credenciamento/autenticação;

Gitclone - copiar repositório para local;

Git add - adicionar no index (intermediário);

Commit - Adicionado no repositório (local);

Git push - enviar para o GIT (servidor);

Git pull - pegar alterações do servidor;

Branch - Ramificações no repositório (main.funionalidades.)

Git Merge = Copiar uma branch

Fork = Cópia de um repositório -  Realizado no https://github.com/pedrosdp/conversao-temperatura

*Containers*: Padronização, Involucro; Portabilidade; Confiabilidade; Idempotência (Sempre o mesmo comportamento);

Todos os processos da minha etapa de criação de ambiente e execução de aplicações serão feitos em containers.

Setup do Ambiente (Node, MongoDB, RabbitMQ);

Máquina do desenvolvedor = Servidor = Nuvem

Docker: 
Imagem (Template) - Elemento básico para criação do Container;

Arquitetura: Docker Daemon (Docker Host); Docker Client; Docker Registry (Repositório) - Docker Hub;

Docker container run (criar)
Docker container rm (destruir)

porta local com a porta do container (80);

Robo 3T: fornece uma ferramenta MONGODB de código aberto com funcionalidades inovadoras para atender às necesidades;

DockerFile - Criar imagem em qualquer lugar;

Lembrete: Versionamento da imagem é uma boa prática;

Pipeline: Conjunto de etapas automatizadas. Cadeia de execução. 

Pipeline CI (Integração Contínua) Codificação - Commit - Build - Teste - Geração de Pacote de entrega; Todas as etapas que são necesśarias para entrega minimizando os erros;

Deploy (implantar) Contínuo - Release;Teste;Aceite;Deploy em Produção.

GitLab;
Github Actions - Workflow, Events, Jobs, Steps, Actions, Runners;

Pipeline: https://github.com/pedrosdp/conversao-temperatura

Kubernetes - Sistema de código aberto para automatizar a implantação, o dimensionamento e o gerenciamento de aplicativos em containers. Agrupa os containers.

Aula 3 - Marco Aurélo Souza Mangan

Conjunto de Configurações: PetClinic serve como demonstração das capacidades de um framework de desenvolvimento de softwares. Plataforma Java.

Importante: a implementação é gradual;

Lean = Enxuto

Left-shift o shift-left = priorizar participação dos envolvidos ao aplicar atividades de garantia de qualidade, segurança, privacidade, desempenho, verificão e validação MAIS CEDO.

Automação






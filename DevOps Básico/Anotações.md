# **DevOps Básico**

## **Aulas 1 e 2 - Fabrício Veronez**

### **Desenvolvimento de Software**
- **Etapas do desenvolvimento:**
  - Planejamento (Requisitos)
  - Desenvolvimento
  - Testes
  - Implantação (Disponibilização)

### **Papéis no Desenvolvimento**
- **Profissional de Operação:**
  - Cuida do software em implantação.
  - Conhece infraestrutura.
  - Objetivo: Manter a solução estável.
- **Profissional de Desenvolvimento:**
  - Conhece profundamente programação.
  - Objetivo: Criar novos recursos e features.
  - Não interage com o ambiente de produção.

### **DevOps**
- **Foco:** Produto e entrega ágil.
- **Objetivo:** Resolver problemas e aprender com eles.
- **Três Maneiras do DevOps:**
  1. **Fluxo:** Análise e otimização de processos, testes, deploy contínuo, entrega de baixo risco.
  2. **Feedback:** Implementar métricas, observabilidade, testes A/B, coletar resultados.
  3. **Aprendizado Contínuo:** Aprender com erros, experimentação controlada.
- **Ciclo do DevOps:**
  - Plan → Code → Build → Test → Release → Deploy → Operate → Monitor.

---

## **Twelve Factor Apps (Heroku)**
1. **Código Base:** Uma aplicação, um repositório. Uso do Git.
2. **Dependências:** Declare todas explicitamente (ex.: `pip` para Python, `npm` para Node).
3. **Configuração:** Use variáveis de ambiente (ex.: senhas e chaves).
4. **Serviços de Apoio:** Trate serviços externos como recursos (ex.: Mensageria, Storage).
5. **Construção, Lançamento e Execução:** Separe build, release e run.
6. **Processos:** Sem estado nos processos (stateless).
7. **Port Binding:** Aplicações devem expor serviços HTTP diretamente.
8. **Concorrência:** Escale processos, não máquinas.
9. **Descartabilidade:** Inicie e finalize processos rapidamente e com segurança.
10. **Paridade entre Ambientes:** Mantenha desenvolvimento, teste e produção semelhantes.
11. **Logs:** Trate logs como fluxo de eventos.
12. **Processos Administrativos:** Use scripts separados para tarefas manuais.

---

## **Versionamento de Código**
- **Git:** Ferramenta para controle de versões.
- **Comandos básicos:**
  - `git clone`: Copiar repositório para a máquina local.
  - `git add`: Adicionar arquivos ao índice.
  - `git commit`: Salvar alterações localmente.
  - `git push`: Enviar alterações ao servidor remoto.
  - `git pull`: Trazer alterações do servidor remoto.
  - `git merge`: Unir branches.
  - **Branch:** Criação de ramificações (ex.: `main`, `funcionalidades`).
  - **Fork:** Cópia de um repositório para personalização.

---

## **Containers**
- **Definição:** Padronização, portabilidade, confiabilidade e idempotência (mesmo comportamento em execuções).
- **Processos em Containers:** Toda a configuração do ambiente é feita em containers.
- **Ferramentas:**
  - **Docker:**
    - **Imagem:** Template básico para criação de containers.
    - **Arquitetura:** Docker Daemon, Docker Client, Docker Registry (Docker Hub).
    - **Comandos:**
      - `docker container run`: Criar container.
      - `docker container rm`: Remover container.
      - Mapear portas (ex.: local 80 para porta do container).
    - **Dockerfile:** Criar imagens customizadas.
    - **Prática:** Versione suas imagens.

---

## **Pipeline**
- **Definição:** Cadeia de execução automatizada.
- **Tipos:**
  - **CI (Integração Contínua):** Codificação → Commit → Build → Teste → Geração de pacote.
  - **Deploy Contínuo:** Implantação automática após aprovação.
- **Ferramentas:**
  - **GitHub Actions:** Configuração de workflows e runners.
  - **Kubernetes:** Sistema para automatizar implantação, dimensionamento e gerenciamento de containers.

---

## **Aula 3 - Marco Aurélio Souza Mangan**

### **Configurações e Ferramentas**
- **PetClinic:** Demonstração de framework em Java.
- **Lean Development (Enxuto):** Implementação gradual.
- **Shift-Left:** Priorizar atividades de garantia de qualidade, segurança e desempenho mais cedo no processo.

### **Práticas DevOps**
1. **Propriedade Coletiva:** Código é responsabilidade de todos.
2. **Automatização de Construção:** Ex.: GitHub Actions.
3. **Testes:** Automatizados para garantir qualidade.

---

## **Gerência de Configuração**
- **Elementos:**
  - Gerência de versões e mudanças (Git e GitHub).
  - Dependências internas e construção (ex.: Maven, Gradle, npm, Yarn).
  - Gerência de pacotes (ex.: apt, Homebrew, Windows Package Manager).
- **Ferramentas:**
  - **SDKMAN:** Gerenciamento de ferramentas de desenvolvimento.
  - **Spring Boot:** Conjunto de utilitários e bibliotecas para projetos Java.
  - **Sonar:** Análise de código para verificar conformidade com regras e boas práticas.
  - **Google Jib:** Plugin Maven para criação de containers.

---

### **Livros **
- **Pro Git:** Livro sobre versionamento com Git.
```
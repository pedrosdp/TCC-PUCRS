1. Conceitos Fundamentais
Big Data: Volume, velocidade, variedade, validade, volatilidade e valência.
Teorema CAP: Consistência (C), Disponibilidade (A) e Tolerância a Partições (P) — impossível garantir os três simultaneamente.
Modelos de Bancos NoSQL:
Chave-Valor: Ex.: Redis.
Documentos: Ex.: MongoDB.
Colunar: Ex.: Cassandra.
Grafos: Ex.: Neo4j.
2. Modelagem de Dados
Modelagem Conceitual: Compreensão dos requisitos e identificação dos dados essenciais.
Modelagem Lógica: Estruturação dos dados em tabelas, chaves primárias e relacionamentos.
Normalização: Aplicação de formas normais para evitar redundância.
Teorema CAP e Modelos ACID/BASE:
ACID: Atomicidade, Consistência, Isolamento e Durabilidade (bancos relacionais).
BASE: Basicamente disponível, Estado suave, Consistência eventual (bancos NoSQL).
3. Bancos NoSQL em Detalhe
3.1. MongoDB (Documentos)
Dados em formato BSON.
Suporte nativo a escalabilidade horizontal (sharding).
Flexibilidade de esquema.
Linguagem baseada em JavaScript.
Escalabilidade:
Horizontal: Sharding, mestre-escravo e peer-to-peer.
Vertical: Expansão de hardware.
Desvantagens: Limitações em transações ACID e consistência eventual.
3.2. Cassandra (Colunar)
Arquitetura distribuída e altamente escalável.
Consistência eventual.
Suporte a grandes volumes de escrita.
Componentes: Keyspace, Tabelas, Primary Key, Partition Key, Clustering Key.
Casos de uso: E-commerce, serviços financeiros, time-series e distribuição de conteúdo.
Desvantagens: Leituras mais lentas que escritas, ausência de joins e agregações nativas.
3.3. Redis (Chave-Valor)
Estrutura de dados em memória (RAM), arquitetura single-thread.
Alta performance em leitura/escrita.
Persistência opcional: RDB, AOF ou sem persistência.
Casos de uso: Caches, sessões de usuário, sistemas de mensagens e placares em tempo real.
Desvantagens: Limitação de armazenamento em memória, falta de paralelismo e custo elevado para grandes volumes.
3.4. Neo4j (Grafos)
Orientado a grafos, ideal para mapear relacionamentos complexos.
Suporte a transações ACID.
Usa a linguagem CYPHER para consultas.
Casos de uso: Redes sociais, detecção de fraudes, recomendação de conteúdo e gestão de identidades.
Desvantagens: Baixa eficiência em operações de agregação e escrita massiva, além de uma comunidade menor.
4. Escalabilidade e Performance
Escalabilidade Horizontal: Distribuição de dados entre múltiplos servidores (sharding, peer-to-peer).
Escalabilidade Vertical: Potencialização de hardware existente.
Failover: Tolerância a falhas, permitindo continuidade dos serviços.
Load Balance: Distribuição de carga entre servidores para otimização do desempenho.
5. Estratégias de Implementação
Two-Phase Commit: Coordenação de transações distribuídas.
Tradeoffs em NoSQL: Compromissos entre desempenho, consistência e disponibilidade.
Escolha do Banco de Dados: Baseada em requisitos específicos do projeto e perfil dos dados.
6. Boas Práticas
Pensar em como os dados serão acessados antes de modelar.
Avaliar o custo de escalabilidade e manutenção dos bancos.
Evitar misturar muitos bancos diferentes para não comprometer a consistência.
Considerar a frequência de acesso aos dados no planejamento.
7. Considerações Finais
Bancos NoSQL oferecem soluções flexíveis e escaláveis, mas não substituem totalmente bancos relacionais.
A escolha do banco deve considerar volume de dados, tipo de transações e necessidades de escalabilidade.
A compreensão dos trade-offs de cada modelo é essencial para uma implementação eficiente.
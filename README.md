# Assistente Virtual da Secretaria Acadêmica com RAG

## Descrição

Este projeto consiste em um assistente virtual para atendimento acadêmico, desenvolvido como atividade prática da disciplina de Engenharia de Software com IA.

A solução utiliza uma base de conhecimento composta por documentos da secretaria acadêmica para responder dúvidas dos alunos sobre processos como matrícula, cancelamento, transferência e horário de atendimento.

O objetivo é demonstrar os conceitos fundamentais de agentes conversacionais e Retrieval-Augmented Generation (RAG), permitindo que as respostas sejam baseadas em informações previamente cadastradas.

---

## Objetivo

Desenvolver um agente simples capaz de:

- Receber perguntas em linguagem natural;
- Consultar uma base de conhecimento institucional;
- Recuperar informações relevantes;
- Apresentar respostas ao usuário.

---

## Tecnologias Utilizadas

- Python 3
- Streamlit
- VS Code
- Git/GitHub
- GitHub Copilot (apoio ao desenvolvimento)
- Arquivos TXT como base de conhecimento

---

## Estrutura do Projeto

secretaria-rag
│
├── documentos
│   ├── matricula.txt
│   ├── transferencia.txt
│   ├── cancelamento.txt
│   └── atendimento.txt
│
├── app.py
├── requirements.txt
└── README.md

---

## Arquitetura da Solução

Usuário
   ↓
Pergunta
   ↓
Busca na Base de Conhecimento
   ↓
Documento Relacionado
   ↓
Resposta

---

## Base de Conhecimento

A base de conhecimento é composta por documentos textuais contendo informações da secretaria acadêmica:

- Matrícula
- Transferência
- Cancelamento
- Atendimento

Esses documentos são consultados para fornecer respostas ao usuário.

---

## Exemplos de Perguntas

- Como faço minha matrícula?
- Como solicitar transferência?
- Qual é o horário de atendimento?
- Como cancelar minha matrícula?

---

## Conceito de RAG Utilizado

O projeto implementa o conceito de Retrieval-Augmented Generation (RAG) de forma simplificada.

### Retrieval (Recuperação)

O sistema consulta a base de conhecimento local e identifica o documento relacionado à dúvida do usuário.

### Generation (Geração)

A resposta apresentada ao usuário é baseada exclusivamente no conteúdo recuperado da base de conhecimento.

Essa abordagem reduz respostas sem fundamento e garante que as informações exibidas estejam alinhadas aos documentos institucionais cadastrados.

---

## Uso de IA no Desenvolvimento

A Inteligência Artificial foi utilizada como apoio durante o desenvolvimento do projeto para:

- Estruturação da solução;
- Geração inicial de código;
- Correção de erros;
- Apoio na documentação;
- Refinamento da implementação.

Todas as sugestões geradas foram analisadas e validadas antes da utilização.

---

## Resultados Obtidos

O sistema foi capaz de:

- Consultar a base de conhecimento;
- Identificar informações relevantes;
- Responder dúvidas básicas de alunos;
- Demonstrar os conceitos fundamentais de agentes conversacionais e RAG.

---

## Limitações

- Base de conhecimento reduzida;
- Poucos documentos cadastrados;
- Busca simples por palavras-chave;
- Não utiliza banco vetorial;
- Não possui persistência de histórico.

---

## Trabalhos Futuros

Como evolução da solução, podem ser implementados:

- Integração com modelos de IA generativa (Gemini ou Ollama);
- Busca vetorial utilizando embeddings;
- Inclusão de documentos em PDF;
- Histórico de conversas;
- Interface administrativa para atualização da base de conhecimento.

---

## Conclusão

O projeto demonstrou de forma prática como um assistente virtual pode utilizar uma base de conhecimento para responder dúvidas de usuários. Mesmo utilizando uma arquitetura simplificada, foi possível compreender os conceitos fundamentais de RAG, engenharia de prompts e apoio da IA no ciclo de desenvolvimento de software.
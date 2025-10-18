# SGE - Sistema de Gerenciamento de Estoque

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
  <img alt="DjangoREST" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
  <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
</p>

Sistema completo de gerenciamento de estoque desenvolvido em Django que permite controlar produtos, fornecedores, entradas/saídas, com dashboard analítico, notificações via WhatsApp e relatórios gerados por IA.

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Arquitetura](#-arquitetura)
- [Tecnologias](#-tecnologias)
- [Como Executar](#-como-executar)
- [Integração Webhook](#-integração-webhook)
- [Agente de IA](#-agente-de-ia)

## 🎯 Sobre o Projeto

Sistema web completo para gestão de estoque com controle de produtos, marcas, categorias, fornecedores, entradas e saídas. Inclui dashboards interativos com gráficos, autenticação JWT, notificações automáticas via WhatsApp e relatórios estratégicos gerados por IA.

## ⚡ Funcionalidades

### Gestão de Cadastros

- CRUD completo de produtos, marcas, categorias e fornecedores
- Controle de entradas e saídas de estoque
- Atualização automática de quantidade em estoque via Django Signals
- Sistema de permissões granular por usuário

### Dashboard Analítico

- Métricas em tempo real (valor em estoque, custo, lucro)
- Gráficos de vendas dos últimos 7 dias
- Distribuição de produtos por categoria e marca
- Estatísticas de vendas e produtos vendidos

### API RESTful

- Autenticação JWT (access token 1 dia, refresh token 7 dias)
- Endpoints completos para todas as entidades
- Documentação interativa
- Proteção por permissões

### Notificações Automáticas

- Envio de notificação via WhatsApp quando há saída de produtos
- Integração com webhook externo
- Dados formatados com detalhes da venda e lucro

### Agente de IA (OpenAI)

- Análise diária automatizada dos dados de estoque
- Sugestões estratégicas de reposição
- Identificação de produtos com alta/baixa rotatividade
- Alertas de ruptura de estoque
- Comando: `python manage.py sge_agent_invoke`

## 🏗 Arquitetura

### Estrutura de Apps Django

**authentication/** - Autenticação JWT via Simple JWT

**brands/** - Gerenciamento de marcas de produtos

**categories/** - Gerenciamento de categorias

**suppliers/** - Cadastro de fornecedores

**products/** - Controle completo de produtos (título, preço, quantidade, etc)

**inflows/** - Registro de entradas de estoque (aumenta quantidade via signal)

**outflows/** - Registro de saídas/vendas (diminui quantidade via signal e dispara webhook)

**ai/** - Agente inteligente OpenAI para análise e relatórios estratégicos

**services/** - Serviços externos (integração com webhook de notificações)

### Django Signals

- **inflows.signals**: Aumenta quantidade do produto ao registrar entrada
- **outflows.signals**: Diminui quantidade e envia evento para webhook ao registrar saída

## 🛠 Tecnologias

- **Django 4.2** - Framework web Python
- **Django REST Framework 3.15** - API RESTful
- **Simple JWT** - Autenticação JWT
- **PostgreSQL 15** - Banco de dados
- **Docker & Docker Compose** - Containerização
- **OpenAI API** - Geração de relatórios com IA
- **Bootstrap 5** - Interface responsiva
- **Chart.js** - Gráficos interativos
- **Flake8** - Qualidade de código

## 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose
- Chave API da OpenAI

### Instalação com Docker

1. Clone o repositório

```bash
git clone <url-do-repositório>
cd sge
```

2. Configure as variáveis de ambiente (`.env`)

```env
OPENAI_MODEL=gpt-4
OPENAI_API_KEY=sua_chave_openai
```

3. Inicie os containers

```bash
docker-compose up -d
```

4. Acesse a aplicação

- Sistema: `http://localhost:8000`
- Admin: `http://localhost:8000/admin`
- API: `http://localhost:8000/api/v1/`

### Comandos Úteis

```bash
# Executar testes
python manage.py test

# Invocar agente de IA
python manage.py sge_agent_invoke

# Verificar qualidade do código
flake8 .
```

## 🔗 Integração Webhook

Este sistema envia notificações automáticas via webhook sempre que uma saída de produto é registrada.

**Webhook Receptor (Projeto Separado):**

- **Repositório**: [SGE Webhook Notifier](https://github.com/httpablo/notify-django)
- **Função**: Recebe eventos de saída e envia notificações via WhatsApp (CallMeBot API)
- **Endpoint**: `POST /api/v1/webhooks/order/`

**Payload enviado:**

```json
{
  "event_type": "create_outflow",
  "timestamp": "2024-11-20 14:30:00",
  "product": "Nome do Produto",
  "product_cost_price": 100.0,
  "product_selling_price": 150.0,
  "quantity": 5,
  "description": "Descrição da saída"
}
```

**Configuração:**
O envio do webhook é feito pelo arquivo `services/notify.py` e disparado automaticamente pelo signal em `outflows/signals.py` quando uma nova saída é criada.

Para configurar o webhook receptor, consulte o [README do projeto webhook](https://github.com/httpablo/notify-django).

## 🤖 Agente de IA

O sistema inclui um agente inteligente que analisa dados de estoque usando a API da OpenAI.

**Recursos do Agente:**

- Análise automática de produtos e saídas
- Sugestões de reposição baseadas em rotatividade
- Identificação de produtos com risco de ruptura
- Estimativas de faturamento
- Recomendações estratégicas

**Execução Manual:**

```bash
python manage.py sge_agent_invoke
```

**Resultado:**
Os relatórios são salvos no banco de dados (model `AIResult`) e exibidos no dashboard principal em um accordion expansível.

## 📊 Endpoints da API

### Autenticação

```
POST   /api/v1/authentication/token/          - Obter tokens JWT
POST   /api/v1/authentication/token/refresh/  - Renovar token
POST   /api/v1/authentication/token/verify/   - Verificar token
```

### Recursos Principais

```
GET/POST    /api/v1/brands/            - Listar/Criar marcas
GET/POST    /api/v1/categories/        - Listar/Criar categorias
GET/POST    /api/v1/suppliers/         - Listar/Criar fornecedores
GET/POST    /api/v1/products/          - Listar/Criar produtos
GET/POST    /api/v1/inflows/           - Listar/Criar entradas
GET/POST    /api/v1/outflows/          - Listar/Criar saídas
```

## 🧪 Testes

O projeto possui testes unitários para os principais models:

```bash
# Executar todos os testes
python manage.py test

# Testes específicos
python manage.py test brands
python manage.py test products
```

## 🔗 Projetos Relacionados

- **[SGE Webhook Notifier](https://github.com/httpablo/notify-django)** - Sistema de notificações WhatsApp para eventos de saída

---

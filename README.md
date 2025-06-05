# 📦 Sistema de Gerenciamento de Estoque (SGE)

O Sistema de Gerenciamento de Estoque (SGE) é uma aplicação web desenvolvida com Django, focada no controle eficiente de produtos, marcas, fornecedores, categorias, entradas e saídas de estoque. O sistema utiliza autenticação via JWT, fornece dashboards com métricas e gráficos, integra webhooks para notificações via WhatsApp e ainda conta com um agente de IA (via API da OpenAI) para gerar relatórios e sugestões estratégicas com base nos dados de estoque.

---
## 🚀 Funcionalidades Principais

* Cadastro de produtos, marcas, fornecedores, categorias, entradas e saídas.
* Cálculo automático da quantidade disponível em estoque com base nas movimentações.
* Autenticação JWT protegendo rotas e funcionalidades restritas.
* Dashboards interativos com métricas e gráficos de:
    * Vendas
    * Entradas
    * Saídas
    * Valor total em estoque
* Notificações automáticas via WhatsApp por webhooks no evento de saída de produtos.
* Geração de relatórios diários inteligentes através de um agente de IA (OpenAI API), com análise estratégica dos dados de estoque.

---
## 🛠️ Tecnologias Utilizadas

* Django
* Django REST Framework
* Bootstrap
* Chart.js
* Docker
* JWT (JSON Web Tokens)
* API OpenAI
* Webhooks

---
## ⚙️ Requisitos Não Funcionais

* Interface web responsiva e intuitiva.
* Sistema de autenticação seguro com tokens JWT.
* Relatórios inteligentes automatizados com a OpenAI API.
* Integração com serviços externos via Webhooks.
* Contêineres Docker.
* Cobertura de testes para garantir qualidade e confiabilidade.

---

## 🧪 Execução de Testes

Para rodar os testes automatizados:

```bash
python manage.py test
```

---

## 🤖 Agente de Inteligência Artificial

O sistema conta com um **agente de IA** que consome dados de produtos e saídas no formato **JSON**, processa essas informações usando a **API da OpenAI** e gera **relatórios estratégicos diários** com sugestões para otimização do estoque e tomada de decisões gerenciais.

---

## 🐳 Execução com Docker

### Construa a imagem:

```bash
docker-compose build
```

### Suba os containers:

```bash
docker-compose up
```

A aplicação estará disponível em: [http://localhost:8000](http://localhost:8000)

---

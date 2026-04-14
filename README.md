# 💸 Nology Cashback App - Desafio Técnico

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

Este projeto foi desenvolvido como resolução do **Desafio Técnico para Estágio em Desenvolvimento da Nology**. Trata-se de uma aplicação Full-Stack que simula um sistema de cálculo e registro de cashback para uma Fintech, aplicando regras de negócio específicas para clientes normais e VIPs.

## 🔗 Links de Produção

- **Frontend (Aplicação Web):** [Acesse o App Aqui](https://teste-tecnico-nology-ddio.vercel.app/)
- **Backend (Documentação da API):** [Swagger UI](https://teste-tecnico-nology.onrender.com/docs)

---

## 🏛️ Arquitetura do Projeto (Monorepo)

O projeto foi estruturado seguindo boas práticas de separação de responsabilidades e microsserviços, utilizando um único repositório (*Monorepo*) para facilitar o controle de versão, mas com deploys independentes:

1. **Frontend (Vercel):** Interface de usuário responsiva construída com HTML5, CSS3 (Modern UI) e Vanilla JavaScript. Consome a API RESTful remotamente. O Vercel foi configurado para fazer o build focando exclusivamente no diretório `FrontEnd/`.
2. **Backend (Render):** API de alta performance construída em **Python 3** com **FastAPI**. Responsável por toda a validação de dados, cálculo das regras de negócio e comunicação com o banco de dados via **SQLAlchemy** (ORM).
3. **Database (PostgreSQL no Render):** Banco de dados relacional em nuvem utilizado para persistir o histórico de transações, registrando o IP real do usuário via header `x-forwarded-for` configurado na API.

---

## 💼 Regras de Negócio Implementadas

A lógica central da aplicação (isolada nativamente no arquivo `questao1.py` e integrada à API) respeita as seguintes diretrizes:

1. **Cashback Base:** Calculado sempre a 5% sobre o valor final da compra.
2. **Bônus VIP:** Adicional de 10% calculado **sobre o valor do cashback base** (e não somado diretamente à porcentagem original).
3. **Multiplicador:** Qualquer compra com valor superior a R$ 500,00 ativa o benefício do **dobro de cashback** (aplicado após o cálculo do bônus VIP, se houver).

---
cd Teste-Tecnico-Nology

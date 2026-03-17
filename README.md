## Tecnologias Utilizadas

- **Python** – linguagem principal da aplicação
- **FastAPI** – framework web moderno para construção de APIs
- **Docker** – containerização da aplicação para execução consistente


Essas tecnologias foram escolhidas por oferecerem:

- Alta performance e simplicidade
- Facilidade de desenvolvimento de APIs REST
- Padronização do ambiente via containers

---
# Estrutura do Projeto

app/
controllers/
models/
routes/
services/

tests/

Dockerfile
docker-compose.yml
requirements.txt

README.md

**Descrição:**

- **controllers** – lógica de processamento das requisições
- **models** – modelos de dados (Pydantic)
- **routes** – definição dos endpoints da API
- **services** – regras de negócio e cálculo do risco
- **tests** – testes automatizados

---

# Como Rodar o Projeto com Docker

## 1 Clonar o repositório

git clone https://github.com/PLSantosBrito/borysta-case-api
cd borysta-case-api

## 2 Construir e iniciar os containers

docker compose up --build

Após iniciar, a API estará disponível em:

http://localhost:8000

---

# Documentação da API

A documentação automática gerada pelo FastAPI pode ser acessada em:

http://localhost:8000/docs

Interface baseada em Swagger para testar os endpoints diretamente pelo navegador.

---

# Endpoint Principal

## POST `/api/v1/risk-score`

Realiza a análise de risco de uma ou mais mercadorias.

### Exemplo de Requisição

[
{
"pin_id":"123456789",
"company_name":"Tech Indústria S.A.",
"merchandise_value":150000,
"origin_state":"SP",
"destination_state":"AM",
"has_previous_infractions":false
}
]

# Exemplo de Resposta

[
{
"pin_id": "123456789",
"risk_score": 63,
"recommended_channel": "AMARELO",
"analysis_timestamp": "2026-03-16T14:21:30.123Z"
}
]

---

# Regras de Classificação de Risco

A classificação segue três canais:

| Canal | Critério |
| VERDE | Valor abaixo de 100.000 sem infrações |
| AMARELO | Valor entre 100.000 e 500.000 sem infrações |
| VERMELHO | Valor acima de 500.000 ou histórico de infrações |

O **risk score** é gerado aleatoriamente dentro do intervalo correspondente ao canal.

---

# Observações

A API aceita **um ou mais objetos no payload**, permitindo processar múltiplas mercadorias em uma única requisição.

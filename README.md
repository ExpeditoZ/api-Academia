# api-Academia
Esta API de Gerenciamento de Academia organiza clientes, treinos e planos de assinatura, permitindo criar, listar, atualizar e remover informações. Ela gerencia dados dos clientes, treinos personalizados e planos com preços, facilitando o controle e administração de academias de forma simples e eficiente.

## Tecnologias Utilizadas  
- **Python 3.10+**  
- **FastAPI**  
- **Uvicorn** (servidor ASGI)  
- **Postman** (para testar as rotas)  

---
Endpoints da API
Clientes
Cadastrar Cliente

Método: POST
URL: /clientes
Corpo (exemplo):
json
Copiar código
{
    "nome": "João Silva",
    "idade": 28,
    "endereco": "Rua Exemplo, 123",
    "telefone": 88988278850,
    "plano": "Mensal"
}
Listar Clientes

Método: GET
URL: /clientes
Obter Cliente pelo ID

Método: GET
URL: /clientes/{cliente_id}
Atualizar Cliente

Método: PUT
URL: /clientes/{cliente_id}
Corpo (exemplo):
json
Copiar código
{
    "nome": "João Silva Atualizado",
    "idade": 29,
    "endereco": "Rua Atualizada, 456",
    "telefone": 88988278851,
    "plano": "Anual"
}
Remover Cliente

Método: DELETE
URL: /clientes/{cliente_id}
Treinos
Cadastrar Treino

Método: POST
URL: /treinos
Corpo (exemplo):
json
Copiar código
{
    "cliente_id": 1,
    "descricao": "Treino A - Peito e Tríceps",
    "duracao": "1 hora",
    "frequencia_semana": 3
}
Listar Treinos

Método: GET
URL: /treinos
Obter Treino pelo ID

Método: GET
URL: /treinos/{treino_id}
Atualizar Treino

Método: PUT
URL: /treinos/{treino_id}
Corpo (exemplo):
json
Copiar código
{
    "cliente_id": 1,
    "descricao": "Treino A Atualizado",
    "duracao": "1 hora",
    "frequencia_semana": 4
}
Remover Treino

Método: DELETE
URL: /treinos/{treino_id}
Planos
Cadastrar Plano

Método: POST
URL: /planos
Corpo (exemplo):
json
Copiar código
{
    "nome": "Mensal",
    "preco": 100.0
}
Listar Planos

Método: GET
URL: /planos
Obter Plano pelo ID

Método: GET
URL: /planos/{plano_id}
Atualizar Plano

Método: PUT
URL: /planos/{plano_id}
Corpo (exemplo):
json
Copiar código
{
    "nome": "Mensal Atualizado",
    "preco": 110.0
}
Remover Plano

Método: DELETE
URL: /planos/{plano_id}

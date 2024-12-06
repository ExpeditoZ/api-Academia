from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI(
    title="Gerenciamento da Academia",
    description="API para gerenciar clientes, treinos e planos da academia.",
    version="1.0.0",
)

# Dados iniciais
CLIENTES = [
     {"id": 1, "nome": "Expedito Farias De Melo", "idade": 21, "endereco": "Rua Delfino Alves", "telefone": 88935478848, "plano": "Mensal"},
     {"id": 2, "nome": "Pedro Henrique Pereira Facundo", "idade": 20, "endereco": "Rua Jesse Alves da Silva", "telefone": 88988546847, "plano": "Anual"},
]

TREINOS = [
    {"id": 1, "cliente_id": 1, "descricao": "Treino A - Peito e Tríceps", "duracao": "1 hora", "frequencia_semana": 3},
    {"id": 2, "cliente_id": 2, "descricao": "Treino B - Costas e Bíceps", "duracao": "1 hora", "frequencia_semana": 2},
]

PLANOS = [
    {"id": 1, "nome": "Mensal", "preco": 100.00},
    {"id": 2, "nome": "Anual", "preco": 1000.00},
]

# Modelos
class Cliente(BaseModel):
    nome: str
    idade: int
    endereco: str
    telefone: int
    plano: str


class Treino(BaseModel):
    cliente_id: int
    descricao: str
    duracao: str
    frequencia_semana: int


class Plano(BaseModel):
    nome: str
    preco: float


# Rota raiz
@app.get("/", tags=["root"])
def read_root():
    """Rota raiz."""
    return {"message": "Bem-vindo à API de Gerenciamento da Academia!"}


# Endpoints para Clientes
@app.get("/clientes", tags=["clientes"], response_model=List[dict])
def listar_clientes():
    """Listar todos os clientes."""
    return CLIENTES


@app.get("/clientes/{cliente_id}", tags=["clientes"], response_model=dict)
def obter_cliente(cliente_id: int):
    """Obter cliente pelo ID."""
    cliente = next((cliente for cliente in CLIENTES if cliente["id"] == cliente_id), None)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return cliente


@app.post("/clientes", tags=["clientes"], response_model=dict)
def cadastrar_cliente(cliente: Cliente):
    """Cadastrar novo cliente."""
    novo_cliente = cliente.dict()
    novo_cliente["id"] = len(CLIENTES) + 1
    CLIENTES.append(novo_cliente)
    return novo_cliente


@app.put("/clientes/{cliente_id}", tags=["clientes"], response_model=dict)
def atualizar_cliente(cliente_id: int, cliente: Cliente):
    """Atualizar informações de um cliente existente."""
    for index, clien in enumerate(CLIENTES):
        if clien["id"] == cliente_id:
            CLIENTES[index] = {**clien, **cliente.dict()}
            CLIENTES[index]["id"] = cliente_id  # Garante que o ID não muda
            return CLIENTES[index]
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")


@app.delete("/clientes/{cliente_id}", tags=["clientes"])
def remover_cliente(cliente_id: int):
    """Remover cliente pelo ID."""
    for index, cliente in enumerate(CLIENTES):
        if cliente["id"] == cliente_id:
            CLIENTES.pop(index)
            return {"message": "Cliente removido com sucesso."}
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")


# Endpoints para Treinos
@app.get("/treinos", tags=["treinos"], response_model=List[dict])
def listar_treinos():
    """Listar todos os treinos."""
    return TREINOS


@app.get("/treinos/{treino_id}", tags=["treinos"], response_model=dict)
def obter_treino(treino_id: int):
    """Obter treino pelo ID."""
    treino = next((treino for treino in TREINOS if treino["id"] == treino_id), None)
    if treino is None:
        raise HTTPException(status_code=404, detail="Treino não encontrado.")
    return treino


@app.post("/treinos", tags=["treinos"], response_model=dict)
def cadastrar_treino(treino: Treino):
    """Cadastrar novo treino."""
    novo_treino = treino.dict()
    novo_treino["id"] = len(TREINOS) + 1
    TREINOS.append(novo_treino)
    return novo_treino


@app.put("/treinos/{treino_id}", tags=["treinos"], response_model=dict)
def atualizar_treino(treino_id: int, treino: Treino):
    """Atualizar informações de um treino existente."""
    for index, t in enumerate(TREINOS):
        if t["id"] == treino_id:
            TREINOS[index] = {**t, **treino.dict()}
            TREINOS[index]["id"] = treino_id
            return TREINOS[index]
    raise HTTPException(status_code=404, detail="Treino não encontrado.")


@app.delete("/treinos/{treino_id}", tags=["treinos"])
def remover_treino(treino_id: int):
    """Remover treino pelo ID."""
    for index, treino in enumerate(TREINOS):
        if treino["id"] == treino_id:
            TREINOS.pop(index)
            return {"message": "Treino removido com sucesso."}
    raise HTTPException(status_code=404, detail="Treino não encontrado.")


# Endpoints para Planos
@app.get("/planos", tags=["planos"], response_model=List[dict])
def listar_planos():
    """Listar todos os planos."""
    return PLANOS


@app.get("/planos/{plano_id}", tags=["planos"], response_model=dict)
def obter_plano(plano_id: int):
    """Obter plano pelo ID."""
    plano = next((plano for plano in PLANOS if plano["id"] == plano_id), None)
    if plano is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado.")
    return plano


@app.post("/planos", tags=["planos"], response_model=dict)
def cadastrar_plano(plano: Plano):
    """Cadastrar novo plano."""
    novo_plano = plano.dict()
    novo_plano["id"] = len(PLANOS) + 1
    PLANOS.append(novo_plano)
    return novo_plano


@app.put("/planos/{plano_id}", tags=["planos"], response_model=dict)
def atualizar_plano(plano_id: int, plano: Plano):
    """Atualizar informações de um plano existente."""
    for index, p in enumerate(PLANOS):
        if p["id"] == plano_id:
            PLANOS[index] = {**p, **plano.dict()}
            PLANOS[index]["id"] = plano_id
            return PLANOS[index]
    raise HTTPException(status_code=404, detail="Plano não encontrado.")


@app.delete("/planos/{plano_id}", tags=["planos"])
def remover_plano(plano_id: int):
    """Remover plano pelo ID."""
    for index, plano in enumerate(PLANOS):
        if plano["id"] == plano_id:
            PLANOS.pop(index)
            return {"message": "Plano removido com sucesso."}
    raise HTTPException(status_code=404, detail="Plano não encontrado.")

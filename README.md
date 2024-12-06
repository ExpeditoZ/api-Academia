# api-Academia
Esta API de Gerenciamento de Academia organiza clientes, treinos e planos de assinatura, permitindo criar, listar, atualizar e remover informações. Ela gerencia dados dos clientes, treinos personalizados e planos com preços, facilitando o controle e administração de academias de forma simples e eficiente.

## Tecnologias Utilizadas  
- **Python 3.10+**  
- **FastAPI**  
- **Uvicorn** (servidor ASGI)  
- **Postman** (para testar as rotas)  

---

### Como Executar  
1. Tenha o **Python** instalado em sua máquina.  
2. Instale as dependências necessárias com o comando:  
   ```bash
   pip install requirements.txt
3. Executar o servidor:
   ```bash
   uvicorn main:app --reload
4. Abra o servidor usando a URL: http://127.0.0.1:8000.
5. Na URL: http://127.0.0.1:8000/docs, será possível acessar o Swagger, onde está disponível as partes da API para gerenciar clientes, treinos e planos da academia.
   
### Complementações
Este projeto é uma aplicação prática para aprender e implementar conceitos básicos de desenvolvimento de APIs utilizando FastAPI.

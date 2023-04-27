# API Consumíveis

Este MVP faz parte do projeto final da disciplina de **Desenvolvimento Full Stack Básico** do curso de Pós Graduação em Engenharia de Software da PUC-Rio.

O objetivo aqui é ilutsrar o conteudo apresentado nas aulas usando como o exemplo o gerenciamento logístico de consumíveis de uma rede de clínicas de estética.

---
## Como executar 


Para executar corretamente a API, é necessário ter todas as bibliotecas Python listadas no arquivo **requirements.txt** instaladas. Após clonar o repositório, é preciso abrir o diretório raiz no terminal para executar os comandos necessários.

Recomenda-se o uso de ambientes virtuais, como o **virtualenv**, para evitar conflitos de dependências com outras aplicações Python.

Para criar um ambiente virtual, basta rodar o comando **python -m venv env**.

Para iniciar o ambiente virtual, basta rodar o comando **env/Scripts/Activate**

Para instalar as dependências, basta rodar o comando **pip install -r requirements.txt**.

Para iniciar a API, execute o comando **python -m flask run --host 0.0.0.0 --port 5000**. Se estiver em modo de desenvolvimento.

Por fim, abra o endereço **http://localhost:5000/#/** no navegador para verificar o status da API em execução.
# Minha API

Este MVP faz parte do projeto final da disciplina de **Desenvolvimento Full Stack Básico** do curso de Pós Graduação em Engenharia de Software da PUC-Rio.

O objetivo aqui é ilutsrar o conteudo apresentado nas aulas usando como o exemplo o gerenciamento logístico de consumíveis de uma rede de clínicas de estética.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenpython -m venv .v.pypa.io/en/latest/).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ python -m flask run --host 0.0.0.0 --port 5000 
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ python -m flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

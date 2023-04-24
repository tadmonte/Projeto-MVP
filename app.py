from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect,request
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from model import Session
from logger import logger
from schemas import *
from flask_cors import CORS
from model.produto import Produto
from datetime import datetime

info = Info(title="API Consumíveis", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags

produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")



@app.get('/')
def home():

    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(body: ProdutoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos.
    """
    #body = request.get_json()
    print(body)
    produto = Produto(
        nome=body.nome,
        quantidade=body.quantidade,
        valor=body.valor,
        unidade=body.unidade,
        validade=datetime.strptime(body.validade,'%Y-%m-%d'))
        
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200
        
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    # except Exception as e:
    #     # caso um erro fora do previsto
    #     error_msg = "Não foi possível salvar novo item :/"
    #     logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
    #     return {"mesage": error_msg}, 400


@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os Produto cadastrados

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).all()

    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200





@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um Produto a partir do nome informado
    Retorna uma mensagem de confirmação da remoção.
    """
    produto_nome = unquote(unquote(query.nome))
    print(produto_nome)
    logger.debug(f"Deletando dados sobre produto #{produto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Produto).filter(Produto.nome == produto_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{produto_nome}")
        return {"mesage": "Produto removido", "nome": produto_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404



    """Adiciona de um novo comentário à um produtos cadastrado na base identificado pelo id

    Retorna uma representação dos produtos e comentários associados.
    """
    produto_id  = form.produto_id
    logger.debug(f"Adicionando comentários ao produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo produto
    produto = session.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        # se produto não encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404

  



    logger.debug(f"Adicionado comentário ao produto #{produto_id}")

    # retorna a representação de produto
    return apresenta_produto(produto), 200

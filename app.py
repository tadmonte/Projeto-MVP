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



produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")



@app.get('/')
def home():

    return redirect('/openapi')


@app.post('/item', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(body: ProdutoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos.
    """
    
    print(body)
    produto = Produto(
        nome=body.nome,
        quantidade=body.quantidade,
        valor=body.valor,
        unidade=body.unidade,
        validade=datetime.strptime(body.validade,'%Y-%m-%d'))
        
    print(produto.id)

    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    
    try:
        
        session = Session()
        session.add(produto)
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200
        

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        print(e)
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.put('/editar', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def editar(body: ProdutoEditarSchema):
    try:
               
        if not body:
            return {"message": "Dados do produto não fornecidos no JSON"}, 400

        session = Session()

        with session.begin_nested():
            produto = session.query(Produto).filter(Produto.id == body.id).first()

            if not produto:
                return {"message": f"Produto com ID {body.id} não encontrado"}, 404

            produto.nome = body.nome
            produto.quantidade = body.quantidade
            produto.valor = body.valor
            produto.unidade = body.unidade

            if 'validade' in body:
                produto.validade = datetime.strptime(body['validade'], '%Y-%m-%d')

            session.commit()
        
        return apresenta_produto(produto), 200

    except Exception as e:
        error_msg = "Não foi possível editar o produto."
        logger.error(f"Erro ao editar produto com ID {produto_id}: {str(e)}")
        return {"message": error_msg}, 400


@app.get('/lista', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Lista todos os produtos cadastrados no banco.

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    session = Session()
    produtos = session.query(Produto).all()

    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200





@app.delete('/excluir', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um Produto a partir do nome informado
    Retorna uma mensagem de confirmação da remoção.
    """
    produto_id = unquote(unquote(query.id))
    print(produto_id)
    logger.debug(f"Deletando dados sobre produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Produto).filter(Produto.id == produto_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{produto_id}")
        return {"mesage": "Produto removido", "id": produto_id}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_id}', {error_msg}")
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



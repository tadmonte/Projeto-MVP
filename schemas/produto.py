from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto
from datetime import datetime




class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Toxina Botulínica 3ml"
    quantidade: Optional[int] = 50
    valor: float = 1768.34
    unidade: str = "Rio Design Barra - RJ"
    validade: datetime = datetime.now()


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Teste"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
            "unidade": produto.unidade,
            "validade": produto.validade
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Toxina Botulínica 3ml"
    quantidade: Optional[int] = 50
    valor: float = 1768.34
    unidade: str = "Rio Design Barra - RJ"
    validade: datetime = datetime.now()
   


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "unidade": produto.unidade,
        "validade": produto.validade,
        
    }

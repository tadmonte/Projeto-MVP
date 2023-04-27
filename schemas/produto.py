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
    validade: str = "2023-12-25"


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    id: str = "1"


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
            "id": produto.id,
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
            "unidade": produto.unidade,
            "validade": produto.validade
        })

    return {"produtos": result}

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

class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto.
    """
    id: int = 1
    nome: str = "Toxina Botulínica 3ml"
    quantidade: Optional[int] = 50
    valor: float = 1768.34
    unidade: str = "Rio Design Barra - RJ"
    validade: datetime = datetime.strptime("2023-12-25",'%Y-%m-%d').date()
   


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str



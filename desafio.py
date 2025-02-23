from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

# CRIANDO AS TABELAS NO DB
class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    endereco = Column(String(80))
    telefone = Column(String(15))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    preco = Column(Integer, nullable=False)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    fornecedor = relationship("Fornecedor")

engine = create_engine('sqlite:///desafio.db', echo=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()


# INSERINDO DADOS NO DB
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome="Fornecedor 1", endereco = "Rua A, 100", telefone = "1234567"),
            Fornecedor(nome="Fornecedor 2", endereco = "Rua B, 101", telefone = "7654321"),
            Fornecedor(nome="Fornecedor 3", endereco = "Rua C, 102", telefone = "0987654"),
            Fornecedor(nome="Fornecedor 4", endereco = "Rua D, 103", telefone = "4567890")
        ]
except SQLAlchemyError as e:
    print(f"O seguinte erro ocorreu ao registrar o fornecedor {e}")

session.add_all(fornecedores)
session.commit()

try:
    with Session() as session:
        produtos = [
            Produto(nome="Produto 1", preco = 10, fornecedor_id = 1),
            Produto(nome="Produto 2", preco = 11, fornecedor_id = 2),
            Produto(nome="Produto 3", preco = 12, fornecedor_id = 3),
            Produto(nome="Produto 4", preco = 14, fornecedor_id = 4)
        ]
except SQLAlchemyError as e:
    print(f"O seguinte erro ocorreu ao registrar o fornecedor {e}")

session.add_all(produtos)
session.commit()
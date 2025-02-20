from sqlalchemy import create_engine

# Conexão do SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão SQLite feita!!!")

## dialetos
## engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# NO SQL ALCHEMY ELE FAZ UMA CORRESPONDÊNCIA DE TIPO ENTRE, por exemplo, STR e VARCHAR

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


Base.metadata.create_all(engine)


# CRIAR UMA SESSÃO NO SQLALCHEMY
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# novo_usuario = Usuario(nome='Matheus', idade=56)
# session.add(novo_usuario)
# session.commit()

with Session() as session:
    novo_usuario = Usuario(nome='Pedro', idade=55)
    session.add(novo_usuario)

    
print("Usuário adicionado")

# FAZENDO UMA QUERY
usuario = session.query(Usuario).filter_by(nome='Pedro').first()
print(f"Usuário encontrado: {usuario.nome}, com Idade de {usuario.idade} anos")



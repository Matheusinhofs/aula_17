from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy import create_engine
from desafio import Produto, produtos, engine


session = Session(engine)

consulta = select(Produto)

for products in session.scalars(consulta).all:
    print(products)
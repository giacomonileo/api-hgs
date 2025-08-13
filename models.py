from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Imovel(Base):
    __tablename__ = "imóveis"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    tipo = Column("tipo", String)
    data_registro = Column("data_registro", String)
    ref = Column("ref", String)
    bairro = Column("bairro", String)
    area_construida = Column("area_construida", String)
    quarto = Column("quarto", String)
    vaga_garagem = Column("vaga_garagem", String)
    status = Column("status", String)
    proprietario = Column("proprietario", String)
    fone = Column("fone", String)


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    fone = Column("fone", String)
    endereco = Column("endereço", String)
    cpf = Column("cpf", String)
    data_cadastro = Column("data_cadastro", String)

class Locador(Base):
    __tablename__ = "locadores"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    endereco = Column("endereço", String)
    fone = Column("fone", String)
    data_cadastro = Column("data_cadastro", String)
    tipo = Column("tipo", String)
    valor = Column("valor", String)
    prazo = Column("prazo", String)
    avaliacao = Column("avaliação", String)

class Comprador(Base):
    __tablename__ = "compradores"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    endereco = Column("endereço", String)
    fone = Column("fone", String)
    data_cadastro = Column("data_cadastro", String)
    tipo = Column("tipo", String)
    valor = Column("valor", String)
    forma_pagamento = Column("forma pagamento", String)
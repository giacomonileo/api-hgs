from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///meubanco.db"

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()
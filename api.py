from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from routes import configure_routes
from models import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///meubanco.db"
db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Cria a sessão do SQLAlchemy
Session = sessionmaker(bind=db)
session = Session()

# Passa o 'app' e a 'session' para a função de rotas
configure_routes(app, session)

if __name__ == '__main__':
    Base.metadata.create_all(bind=db)
app.run(debug=True)
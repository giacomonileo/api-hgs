from flask import jsonify, request
from models import Imovel, Cliente # Importe suas classes aqui

# A função configure_routes vai receber a instância do app e a sessão do SQLAlchemy
def configure_routes(app, session):

    # --- Rota para buscar imóveis
    @app.route('/imoveis', methods=['GET'])
    def listar_imoveis():
        imoveis = session.query(Imovel).all()
        # ... o resto da sua lógica da rota
        imoveis_json = []
        for imovel in imoveis:
            imoveis_json.append({
                'id': imovel.id,
                'tipo': imovel.tipo,
                'data_registro': imovel.data_registro,
                'ref': imovel.ref,
                'bairro': imovel.bairro,
                'area_construida': imovel.area_construida,
                'quarto': imovel.quarto,
                'vaga_garagem': imovel.vaga_garagem,
                'status': imovel.status,
                'proprietario': imovel.proprietario,
                'fone': imovel.fone,
            })
        return jsonify(imoveis_json)

    # --- Rota para buscar um único imóvel pelo ID ---
    @app.route('/imoveis/<int:id>', methods=['GET'])
    def buscar_imovel_por_id(id):
        imovel = session.query(Imovel).filter_by(id=id).first()

        if imovel:
            imovel_json = {
                'id': imovel.id,
                'tipo': imovel.tipo,
                'data_registro': imovel.data_registro,
                'ref': imovel.ref,
                'bairro': imovel.bairro,
                'area_construida': imovel.area_construida,
                'quarto': imovel.quarto,
                'vaga_garagem': imovel.vaga_garagem,
                'status': imovel.status,
                'proprietario': imovel.proprietario,
                'fone': imovel.fone,
            }
            return jsonify(imovel_json)
        else:
            return jsonify({'message': 'Imóvel não encontrado'}), 404

    # --- Rota para adicionar um novo imóvel ---
    @app.route('/imoveis', methods=['POST'])
    def adicionar_imovel():
        dados = request.get_json()
        
        # ... o resto da sua lógica da rota
        novo_imovel = Imovel(
            tipo=dados.get('tipo'),
            data_registro=dados.get('data_registro'),
            ref=dados.get('ref'),
            bairro=dados.get('bairro'),
            area_construida=dados.get('area_construida'),
            quarto=dados.get('quarto'),
            vaga_garagem=dados.get('vaga_garagem'),
            status=dados.get('status'),
            proprietario=dados.get('proprietario'),
            fone=dados.get('fone')
        )
        session.add(novo_imovel)
        session.commit()

        return jsonify({
            'message': 'Imóvel adicionado com sucesso!',
            'id': novo_imovel.id
        }), 201

    # --- Rota para atualizar um imóvel existente ---
    @app.route('/imoveis/<int:id>', methods=['PUT'])
    def atualizar_imovel(id):
        imovel = session.query(Imovel).filter_by(id=id).first()
        if imovel:
            dados = request.get_json()
            
            # ... o resto da sua lógica da rota
            imovel.tipo = dados.get('tipo', imovel.tipo)
            imovel.data_registro = dados.get('data_registro', imovel.data_registro)
            imovel.ref = dados.get('ref', imovel.ref)
            imovel.bairro = dados.get('bairro', imovel.bairro)
            imovel.area_construida = dados.get('area_construida', imovel.area_construida)
            imovel.quarto = dados.get('quarto', imovel.quarto)
            imovel.vaga_garagem = dados.get('vaga_garagem', imovel.vaga_garagem)
            imovel.status = dados.get('status', imovel.status)
            imovel.proprietario = dados.get('proprietario', imovel.proprietario)
            imovel.fone = dados.get('fone', imovel.fone)

            session.commit()
            return jsonify({'message': 'Imóvel atualizado com sucesso!'})
        else:
            return jsonify({'message': 'Imóvel não encontrado'}), 404

    # --- Rota para deletar um imóvel ---
    @app.route('/imoveis/<int:id>', methods=['DELETE'])
    def deletar_imovel(id):
        imovel = session.query(Imovel).filter_by(id=id).first()
        if imovel:
            session.delete(imovel)
            session.commit()
            return jsonify({'message': f'Imóvel com ID {id} deletado com sucesso!'})
        else:
            return jsonify({'message': 'Imóvel não encontrado'}), 404
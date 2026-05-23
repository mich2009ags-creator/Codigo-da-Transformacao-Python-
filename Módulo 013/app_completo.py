from flask import Flask, request, jsonify
from database import (
    criar_tabela, inserir_usuario, buscar_todos_usuarios,
    buscar_usuario_por_id, buscar_usuario_por_email,
    atualizar_usuario, deletar_usuario
)

app = Flask(__name__)

# Inicializa o banco de dados
criar_tabela()

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    """Rota POST para cadastrar usuário com persistência no SQLite"""
    dados = request.get_json()
    
    if not dados:
        return jsonify({'erro': 'Nenhum dado foi enviado'}), 400
    
    # Valida campos obrigatórios
    campos_obrigatorios = ['nome', 'email', 'idade']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({'erro': f'Campo "{campo}" é obrigatório'}), 400
    
    # Verifica se email já existe
    if buscar_usuario_por_email(dados['email']):
        return jsonify({'erro': 'Email já cadastrado'}), 409
    
    try:
        # Insere no banco
        usuario_id = inserir_usuario(
            nome=dados['nome'],
            email=dados['email'],
            idade=dados['idade'],
            profissao=dados.get('profissao')
        )
        
        return jsonify({
            'mensagem': 'Usuário cadastrado com sucesso!',
            'id': usuario_id
        }), 201
    
    except Exception as e:
        return jsonify({'erro': f'Erro ao cadastrar: {str(e)}'}), 500

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """Rota GET para listar todos os usuários"""
    usuarios = buscar_todos_usuarios()
    return jsonify({
        'total': len(usuarios),
        'usuarios': usuarios
    })

@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obter_usuario(id_usuario):
    """Rota GET para obter um usuário específico"""
    usuario = buscar_usuario_por_id(id_usuario)
    
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario_rota(id_usuario):
    """Rota PUT para atualizar um usuário"""
    dados = request.get_json()
    
    if not dados:
        return jsonify({'erro': 'Nenhum dado foi enviado'}), 400
    
    # Verifica se usuário existe
    if not buscar_usuario_por_id(id_usuario):
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    if atualizar_usuario(id_usuario, dados):
        return jsonify({'mensagem': 'Usuário atualizado com sucesso!'})
    else:
        return jsonify({'erro': 'Nenhum dado para atualizar'}), 400

@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def deletar_usuario_rota(id_usuario):
    """Rota DELETE para remover um usuário"""
    if deletar_usuario(id_usuario):
        return jsonify({'mensagem': 'Usuário deletado com sucesso!'})
    else:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/saudacao', methods=['GET'])
def saudacao():
    """Rota GET de saudação"""
    return jsonify({
        'mensagem': 'Bem-vindo à API com SQLite!',
        'endpoints': [
            'POST /cadastrar',
            'GET /usuarios',
            'GET /usuarios/<id>',
            'PUT /usuarios/<id>',
            'DELETE /usuarios/<id>',
            'GET /saudacao'
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
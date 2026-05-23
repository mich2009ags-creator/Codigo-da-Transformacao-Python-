from flask import Flask, request, jsonify

app = Flask(__name__)

# Armazenamento temporário (lista)
usuarios = []
contador_id = 1

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    """Rota POST que recebe dados do usuário via JSON"""
    global contador_id
    
    # Obtém os dados da requisição
    dados = request.get_json()
    
    # Valida se os dados foram enviados
    if not dados:
        return jsonify({'erro': 'Nenhum dado foi enviado'}), 400
    
    # Valida campos obrigatórios
    campos_obrigatorios = ['nome', 'email', 'idade']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({'erro': f'Campo "{campo}" é obrigatório'}), 400
    
    # Cria novo usuário
    novo_usuario = {
        'id': contador_id,
        'nome': dados['nome'],
        'email': dados['email'],
        'idade': dados['idade'],
        'profissao': dados.get('profissao', '')  # campo opcional
    }
    
    usuarios.append(novo_usuario)
    contador_id += 1
    
    return jsonify({
        'mensagem': 'Usuário cadastrado com sucesso!',
        'usuario': novo_usuario
    }), 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """Rota GET para listar todos os usuários cadastrados"""
    return jsonify({
        'total': len(usuarios),
        'usuarios': usuarios
    })

@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def buscar_usuario(id_usuario):
    """Rota GET para buscar um usuário específico"""
    usuario = next((u for u in usuarios if u['id'] == id_usuario), None)
    
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
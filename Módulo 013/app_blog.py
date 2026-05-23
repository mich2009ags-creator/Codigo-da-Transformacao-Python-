from flask import Flask, request, jsonify
from models import (
    criar_tabelas_blog, criar_usuario_blog, autenticar_usuario,
    criar_post, listar_posts, buscar_post_por_id,
    adicionar_comentario, listar_comentarios_por_post
)

app = Flask(__name__)

# Inicializa as tabelas
criar_tabelas_blog()

# Armazenamento simples de token (apenas para demonstração)
sessoes = {}

@app.route('/blog/registrar', methods=['POST'])
def registrar():
    """Registra um novo usuário"""
    dados = request.get_json()
    
    campos = ['username', 'senha', 'email']
    for campo in campos:
        if campo not in dados:
            return jsonify({'erro': f'Campo {campo} obrigatório'}), 400
    
    try:
        usuario_id = criar_usuario_blog(
            username=dados['username'],
            senha=dados['senha'],
            email=dados['email'],
            nome=dados.get('nome')
        )
        return jsonify({'mensagem': 'Usuário criado com sucesso!', 'id': usuario_id}), 201
    except Exception as e:
        return jsonify({'erro': 'Username ou email já existe'}), 409

@app.route('/blog/login', methods=['POST'])
def login():
    """Autentica um usuário"""
    dados = request.get_json()
    
    if not dados or 'username' not in dados or 'senha' not in dados:
        return jsonify({'erro': 'Username e senha obrigatórios'}), 400
    
    usuario = autenticar_usuario(dados['username'], dados['senha'])
    
    if usuario:
        token = f"token_{usuario['id']}_{dados['username']}"
        sessoes[token] = usuario['id']
        return jsonify({
            'mensagem': 'Login realizado com sucesso!',
            'token': token,
            'usuario': {'id': usuario['id'], 'username': usuario['username']}
        })
    else:
        return jsonify({'erro': 'Credenciais inválidas'}), 401

@app.route('/blog/posts', methods=['POST'])
def criar_post_route():
    """Cria um novo post (requer autenticação)"""
    token = request.headers.get('Authorization')
    
    if not token or token not in sessoes:
        return jsonify({'erro': 'Não autorizado'}), 401
    
    dados = request.get_json()
    
    if not dados or 'titulo' not in dados or 'conteudo' not in dados:
        return jsonify({'erro': 'Título e conteúdo são obrigatórios'}), 400
    
    post_id = criar_post(
        titulo=dados['titulo'],
        conteudo=dados['conteudo'],
        autor_id=sessoes[token]
    )
    
    return jsonify({'mensagem': 'Post criado!', 'id': post_id}), 201

@app.route('/blog/posts', methods=['GET'])
def listar_posts_route():
    """Lista todos os posts"""
    posts = listar_posts()
    return jsonify({'posts': posts, 'total': len(posts)})

@app.route('/blog/posts/<int:post_id>', methods=['GET'])
def ver_post(post_id):
    """Visualiza um post específico com seus comentários"""
    post = buscar_post_por_id(post_id)
    
    if not post:
        return jsonify({'erro': 'Post não encontrado'}), 404
    
    comentarios = listar_comentarios_por_post(post_id)
    post['comentarios'] = comentarios
    
    return jsonify(post)

@app.route('/blog/posts/<int:post_id>/comentarios', methods=['POST'])
def adicionar_comentario_route(post_id):
    """Adiciona um comentário a um post"""
    token = request.headers.get('Authorization')
    
    if not token or token not in sessoes:
        return jsonify({'erro': 'Não autorizado'}), 401
    
    dados = request.get_json()
    
    if not dados or 'conteudo' not in dados:
        return jsonify({'erro': 'Conteúdo do comentário é obrigatório'}), 400
    
    comentario_id = adicionar_comentario(
        conteudo=dados['conteudo'],
        post_id=post_id,
        autor_id=sessoes[token]
    )
    
    return jsonify({'mensagem': 'Comentário adicionado!', 'id': comentario_id}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
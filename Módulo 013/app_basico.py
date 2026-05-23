from flask import Flask, jsonify

# Cria a aplicação Flask
app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    """Rota GET que retorna uma mensagem de saudação"""
    return jsonify({
        'mensagem': 'Olá! Bem-vindo à API Flask!',
        'status': 'sucesso'
    })

@app.route('/saudacao/<nome>', methods=['GET'])
def saudacao_personalizada(nome):
    """Rota GET com parâmetro personalizado"""
    return jsonify({
        'mensagem': f'Olá, {nome}! Seja bem-vindo(a)!',
        'status': 'sucesso'
    })

# Rota inicial para teste
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'api': 'API Flask',
        'versao': '1.0',
        'rotas_disponiveis': ['GET /saudacao', 'GET /saudacao/<nome>']
    })

if __name__ == '__main__':
    # Executa o servidor em modo debug
    app.run(debug=True, host='localhost', port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/somar', methods=['POST'])
def somar():
    dados = request.get_json()
    
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({'erro': 'Parâmetros a e b são obrigatórios'}), 400
    
    try:
        a = float(dados['a'])
        b = float(dados['b'])
        resultado = a + b
        return jsonify({'resultado': resultado}), 200
    except (ValueError, TypeError):
        return jsonify({'erro': 'Os valores devem ser números'}), 400

@app.route('/dividir', methods=['POST'])
def dividir():
    dados = request.get_json()
    
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({'erro': 'Parâmetros a e b são obrigatórios'}), 400
    
    try:
        a = float(dados['a'])
        b = float(dados['b'])
        
        if b == 0:
            return jsonify({'erro': 'Divisão por zero não permitida'}), 400
        
        resultado = a / b
        return jsonify({'resultado': resultado}), 200
    except (ValueError, TypeError):
        return jsonify({'erro': 'Os valores devem ser números'}), 400

@app.route('/saudacao/<nome>', methods=['GET'])
def saudacao(nome):
    return jsonify({'mensagem': f'Olá, {nome}!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
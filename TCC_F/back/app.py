from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS  # Adicionado

app = Flask(__name__, static_folder='../')
CORS(app)  # Adicionado para permitir requisições do front-end

@app.route('/')
def index():
    return send_from_directory('../', 'index.html')

@app.route('/contatos')
def contatos():
    return send_from_directory('../', 'contatos.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../', path)

# Nova rota para receber os dados do formulário
@app.route('/contact', methods=['POST'])
def contact():
    dados = request.json
    print("Dados recebidos:", dados)
    return jsonify({"mensagem": "Mensagem recebida com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)

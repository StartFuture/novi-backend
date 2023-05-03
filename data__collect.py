from flask import Flask, request

app = Flask(__name__)

@app.route('/coleta', methods=['POST'])
def coletar_dados():
    dados = request.get_json()
    return 'Dados recebidos com sucesso!'

if __name__ == '__main__':
    app.run()
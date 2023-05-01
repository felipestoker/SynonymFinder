from flask import Flask, render_template, request, jsonify
from datamuse import Datamuse
import os

app = Flask(__name__)
api = Datamuse()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synonyms', methods=['POST'])
def synonyms():
    data = request.get_json()
    word = data['word']

    synonyms_data = api.words(rel_syn=word, max=10)
    print("Dados brutos da API Datamuse:", synonyms_data)  # Linha de depuração
    synonyms = [item['word'] for item in synonyms_data]

    print("Lista de sinônimos:", synonyms)  # Linha de depuração

    return jsonify(synonyms)

if __name__ == '__main__':
    app.run()

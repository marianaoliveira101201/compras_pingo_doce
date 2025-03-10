from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


precos = {
    'azeite': 5.69,
    'óleo': 2.02,
    'massa nero': 1.84,
    'massa macarrão': 0.84,
    'tomate': 1.21,
    'tomate pelado': 1.38,
    'atum': 0.88,
    'salsicha': 0.95,
    'batata palha': 1.09,
    'ovos dúzia': 2.39,
    'açúcar': 1.09,
    'farinha': 0.75,
    'limão': 0.58,
    'alho em pó': 0.99,
    'orégãos': 0.69,
    'natas': 0.72,
    'bechamel': 1.59,
    'cereais': 2.19,
    'leite 6': 4.92,
    'café': 2.49,
    'barritas': 1.29,
    'arroz basmati': 1.99,
    'arroz agulha': 1.39,
    'cebolas 4': 0.85,
    'batatas': 1.52,
    'alho': 0.83,
    'alface': 0.86,
    'queijo fresco': 0.39,
    'abacate': 2.00,
    'lima': 0.53,
    'sopa embalada': 1.64,
    'nabo 2': 0.94,
    'amêndoa': 1.49,
    'manteiga': 1.99,
    'bolachas sal': 1.69,
    'palmeires': 1.19,
    'bolachas': 1.69,
    'iogurtes líquidos 8': 2.59,
    'chocolate culinária': 1.89,
    'papel alumínio': 2.39,
    'pão de cachorro': 0.98,
    'pão de hambúrguer': 0.98,
    'pão de forma': 0.98,
    'tortilha': 1.19,
    'bacon': 2.17,
    'fiambre': 1.69,
    'queijo': 1.76,
    'mozzarella': 0.99,
    'guardanapos': 0.59,
    'desodorizante tommy': 2.64,
    'shampoo': 3.99,
    'escovas': 2.99,
    'elixir': 1.35,
    'massa folhada': 0.99,
    'papel higiénico': 2.37,
    'sacos': 0.89,
    'amaciadores': 1.85,
    'feijão preto': 1.19,
    'feijão frade': 1.02,
    'grão de bico': 1.19,
    'bloco sanitária': 1.64,
    'queijinhos': 2.14,
    'congelado bruxelas': 0.78,
    'congelado legumes': 0.66,
    'snack amêndoa': 1.49,
    'morango': 2.99,
    'paio': 1.75,
    'bolachas de chocolate': 1.19,
    'pensos': 1.99,
    'maionese': 1.15,
    'ketchup': 1.89,
    'água com gás': 1.39,
    'legumes': 0.89,
    'coxinhas': 3.29,
    'bacalhau paloco': 2.29,
    'bifes de peru': 4.68,
    'carne picada': 5.99,
    'espetadas': 3.23,
    'douradinhos': 3.19,
    'couves': 0.65,
    'ervilhas': 0.78,
    'vinho tempero': 0.85,
    'preparado para frango': 0.89,
    'vinha de alho': 0.89,
    'rolo cozinha': 0.99,
}


# Lista para armazenar os itens, cada item terá nome, preço e quantidade
itens = []

# Função para calcular o total e quanto falta para os 100€
def calcular_total():
    total = sum(item['preco'] * item['quantidade'] for item in itens)
    falta = 100 - total
    return total, falta

@app.route('/', methods=['GET', 'POST'])
def index():
    global itens
    
    if request.method == 'POST':
        # Recebe os dados do item via AJAX (JSON)
        if request.is_json:
            data = request.get_json()
            nome = data['nome']
            preco = data['preco']
            quantidade = data['quantidade']
            
            # Adiciona o item à lista
            itens.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})
            
            # Retorna o total e quanto falta para os 100€
            total, falta = calcular_total()
            return jsonify({'itens': itens, 'total': total, 'falta': falta})
    
    total, falta = calcular_total()
    return render_template('index.html', itens=itens, total=total, falta=falta, precos= precos)

@app.route('/sugerir_preco', methods=['POST'])
def sugerir_preco():
    # Recebe o nome do item enviado pelo frontend
    data = request.get_json()
    nome_item = data.get('nome', '').lower()

    # Procura o preço no dicionário de preços
    preco = precos.get(nome_item, 0.00)  # Se não encontrar, retorna 0.00
    
    return jsonify({'preco': preco})

if __name__ == '__main__':
    app.run(debug=True)

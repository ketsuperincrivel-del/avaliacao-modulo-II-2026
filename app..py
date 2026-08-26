from flask import Flask, jsonify, request

app = Flask(__name__)

# Jogos que já começam cadastrados
jogos = [
    {
        "id": 1,
        "titulo": "Minecraft",
        "genero": "Sandbox",
        "plataforma": "PC",
        "ano": 2011
    },
    {
        "id": 2,
        "titulo": "Super Mario Odyssey",
        "genero": "Plataforma",
        "plataforma": "Nintendo Switch",
        "ano": 2017
    },
    {
        "id": 3,
        "titulo": "Rocket League",
        "genero": "Esporte",
        "plataforma": "Multiplataforma",
        "ano": 2015
    }
]


# Rota para listar todos os jogos
@app.route("/api/jogos", methods=["GET"])
def listar_jogos():
    return jsonify(jogos), 200


# Rota para buscar um jogo pelo ID
@app.route("/api/jogos/<int:id>", methods=["GET"])
def buscar_jogo(id):

    for jogo in jogos:
        if jogo["id"] == id:
            return jsonify(jogo), 200

    return jsonify({
        "erro": "Jogo não encontrado"
    }), 404


# Rota para cadastrar um novo jogo
@app.route("/api/jogos", methods=["POST"])
def cadastrar_jogo():

    dados = request.get_json()

    # Verifica se os dados foram enviados
    if not dados:
        return jsonify({
            "erro": "Todos os campos são obrigatórios"
        }), 400

    # Verifica se todos os campos necessários existem
    if (
        "titulo" not in dados or
        "genero" not in dados or
        "plataforma" not in dados or
        "ano" not in dados
    ):
        return jsonify({
            "erro": "Todos os campos são obrigatórios"
        }), 400

    # Cria um novo ID
    novo_id = 1

    if len(jogos) > 0:
        novo_id = jogos[-1]["id"] + 1

    novo_jogo = {
        "id": novo_id,
        "titulo": dados["titulo"],
        "genero": dados["genero"],
        "plataforma": dados["plataforma"],
        "ano": dados["ano"]
    }

    jogos.append(novo_jogo)

    return jsonify(novo_jogo), 201


# Rota para atualizar um jogo
@app.route("/api/jogos/<int:id>", methods=["PUT"])
def atualizar_jogo(id):

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Dados não enviados"
        }), 400

    for jogo in jogos:

        if jogo["id"] == id:

            jogo["titulo"] = dados["titulo"]
            jogo["genero"] = dados["genero"]
            jogo["plataforma"] = dados["plataforma"]
            jogo["ano"] = dados["ano"]

            return jsonify(jogo), 200

    return jsonify({
        "erro": "Jogo não encontrado"
    }), 404


# Rota para excluir um jogo
@app.route("/api/jogos/<int:id>", methods=["DELETE"])
def excluir_jogo(id):

    for jogo in jogos:

        if jogo["id"] == id:

            jogos.remove(jogo)

            return jsonify({
                "mensagem": "Jogo excluído com sucesso"
            }), 200

    return jsonify({
        "erro": "Jogo não encontrado"
    }), 404


# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)

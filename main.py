from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


coche = {
    "encendido": False,
    "velocidad": 0,
    "intermitentes": "off"
}

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route('/accion', methods=['POST'])
def action():
    data = request.json
    comando = data.get("comando")
    incremento = int(data.get("incremento", 10))
    
    # Lógica de encendido/apagado
    if comando == "arrancar_apagar":
        coche["encendido"] = not coche["encendido"]
        if not coche["encendido"]:
            coche["velocidad"] = 0
            coche["intermitentes"] = "off"
        return jsonify(coche)

    # Restricción: Si está apagado, no hace nada (salvo intentar encenderlo)
    if not coche["encendido"]:
        return jsonify({"error": "Coche apagado"}), 403

    # Acciones con coche encendido
    if comando == "acelerar":
        coche["velocidad"] += incremento
        coche["intermitentes"] = "off"
    
    elif comando == "frenar":
        coche["velocidad"] = max(0, coche["velocidad"] - incremento)
        coche["intermitentes"] = "off"
    
    elif comando == "intermitente_izq":
        coche["intermitentes"] = "izq"
    
    elif comando == "intermitente_der":
        coche["intermitentes"] = "der"

    return jsonify(coche)

if __name__ == "__main__":
    app.run(debug=True)
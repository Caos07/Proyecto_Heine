from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("rutas/index.html")

@app.route('/menu',methods=["POST","GET"])
def menu():
    Productos=[
        {
        "nombre":"Coffee of the Day",
        "precio":1000,
        "categoria":"COFFEE",
        "Calificacion":4.7

        },
        {
        "nombre":"Cafe Au Lait",
        "precio":3000,
        "categoria":"COFFEE",
        "Calificacion":4.7
        },
        {
        "nombre":"Red Eye",
        "precio":4000,
        "categoria":"COFFEE",
        "Calificacion":4.7
        },
        {
        "nombre":"Cold Brew Iced Coffee",
        "precio":2000,
        "categoria":"COFFEE",
        "Calificacion":4.7
        },
        {
        "nombre":"Fair Trade Mayan Mocha",
        "precio":2000,
        "categoria":"SIGNATURE DRINKS",
        "Calificacion":4.7
        },
        {
        "nombre":"Beekeeper",
        "precio":3000,
        "categoria":"SIGNATURE DRINKS",
        "Calificacion":4.7
        },
        {
        "nombre":"Vint Julep",
        "precio":1000,
        "categoria":"SIGNATURE DRINKS",
        "Calificacion":4.7
        },
        {
        "nombre":"Salty Turtle Mocha",
        "precio":3000,
        "categoria":"SIGNATURE DRINKS",
        "Calificacion":4.7
        },
        {
        "nombre":"Turmeric Chai",
        "precio":4000,
        "categoria":"SIGNATURE DRINKS",
        "Calificacion":4.7
        },
        {
        "nombre":"Creme BruLatte",
        "precio":2000,
        "categoria":"SIGNATURE DRINKS",
        "Calificacion":4.7
        },
        {
        "nombre":"Loose-Leaf Tea",
        "precio":2000,
        "categoria":"TEA",
        "Calificacion":4.7
        },
        {
        "nombre":"Tea Au Lait",
        "precio":3000,
        "categoria":"TEA",
        "Calificacion":4.7
        },
        {
        "nombre":"Iced Tea",
        "precio":3000,
        "categoria":"TEA",
        "Calificacion":4.7
        },
        {
        "nombre":"Matcha Latte",
        "precio":3000,
        "categoria":"TEA",
        "Calificacion":4.7
        },
    ]

    #ORDENO PRIMERO POR CATEGORÍA? Y ENVIÓ LOS DATOS ORDENADOS????
    #OBTENGO LAS CATEGORÍAS Y ORDENO EN EL FRONTEND?
    Categorias=[]
    for producto in Productos:
        if producto["categoria"] not in Categorias:
            Categorias.append(producto["categoria"])
    
    # if request.method == 'POST':
    #     productosFiltrados=[]
    #     if len(request.form["buscar_bebida"])>0:
    #         for producto in Productos:
    #             if request.form["buscar_bebida"] in producto["nombre"]:
    #                 productosFiltrados.append(producto)

    #         return render_template("menu.html",productos=productosFiltrados)

    return render_template("rutas/menu.html",productos=Productos,categorias=Categorias)

if __name__=="__main__":
    app.run(debug=True)
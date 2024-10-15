from flask import Flask, render_template,request,redirect,url_for
app=Flask(__name__)
#app=Flask(__name__,static_url_path='',static_folder='static')
#app=Flask("my-first-website-in-python")

@app.route("/")
def principal():#buscara ese archivo en la carpeta templates(plantillas)
    return render_template("index.html")

@app.route("/quienesSomos")
def qsomos_route():
    return render_template("quienesSomos.html")
@app.route("/noticias")
def noti_route():
    return render_template("noticias.html")
@app.route("/contactos")
def contac_route():
    coordenadas=(40.7128,-78.0060)
    return render_template("contacto.html",coordenadas=coordenadas)


@app.route("/proceso", methods=['POST'])
def proceso():
                            #name de los input
    nombre=request.form.get('name')
    email=request.form.get('email')
    mensaje=request.form.get('message')
    return render_template("salida.html",nombre=nombre,email=email,mensaje=mensaje)
 
 
@app.route("/servicio")
def serv_route():
    return render_template("servicios.html")



if __name__=="__main__":
    app.run(debug=True,port='5017')
            #estamos en desarollo y que actualice cada cambio (app.run()->los cambio no toma en cuenta)
    # host='0.0.0.0', port='5017' ->podemos cambiar de puerto

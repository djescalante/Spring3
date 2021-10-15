from flask import Flask, flash, request
from flask import render_template as render
from werkzeug.utils import redirect # importamos el render para poder utilijar jinja y plantillas html
from forms import Formulario_Login
app = Flask(__name__)

#vamos a simular una lista de usuarios para aplicar la logica de nuestra pagina


lista_de_usuarios = ["empleado","administrador","superad"]
lista_de_noticias = {
    101:"Noticia 1",
    102:"Noticia 2",
    103:"Noticia 3",
    104:"Noticia 4",
    105:"Noticia 5",
}


@app.route('/', methods=["GET", "POST"]) #usamos un get porque solo estamos consultando la pagina principal no le estamos mandando informacion al servidor
def inicio():
    try:
        if request.method == 'POST':
            usuario = request.form['usuario']
            password = request.form['password']   

            error = None
            if not usuario:
                error = "usuario incorrecto"
                flash(error)
            if not password:
                error = 'La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)       

            if error is not None:
                return redirect("InicioSesion") 
            else:                           
                if usuario == "administrador":
                    return redirect ("administrador")
                elif usuario =="superad":
                    return redirect ("superadministrador")
                else:
                    return redirect ("empleado")
            
    except:
        flash("Se generó un error en el proceso.")
    
    return render("InicioSesion.html") 
    
       
@app.route('/empleado', methods=["GET"])
def empleado():
    return render("empleado.html") 

@app.route('/administrador', methods=["GET", "POST"])
def administrador():
    return render("administrador.html") 

@app.route('/superadministrador', methods=["GET", "POST"])
def superadministrador():
    return render ("superadministrador.html")

@app.route('/editar', methods=["GET", "POST"])
def editar():
    return render ("editar.html")

@app.route('/CrearEmpleado', methods=["GET", "POST"])
def CrearEmpleado():
    return render("CrearEmpleado.html")

@app.route('/retroalimentacion', methods=["GET", "POST"]) #podria varias si solo es de consulta o si puede actulizar sus datos
def perfil():

    return render("retroalimentacion.html")


if __name__ == "__main__":
    app.run(debug = True)
    

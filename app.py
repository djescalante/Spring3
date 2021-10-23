from flask import Flask, flash, request, redirect, url_for
from flask import render_template as render
from flask_wtf import form
from werkzeug.utils import redirect
from wtforms.form import Form # importamos el render para poder utilijar jinja y plantillas html
from forms import flogin, fempleado, feditar
from flask import flash
import os
import sqlite3 as sql
from werkzeug.exceptions import RequestTimeout
from db import get_db, close_db
from flask import g

app = Flask(__name__)


app.secret_key = os.urandom(24)


@app.route('/', methods=["GET", "POST"])
def inicio():
    form = flogin(request.form)
    if request.method == 'POST':



        usuario = request.form['usuario']
        password = request.form['password']
        perfil = request.form['perfil']

        error = None
        db = get_db()
        
        if not usuario:
            error = "Usuario requerido."
            flash( error )
        if not password:
            error = "Contraseña requerida."
            flash( error )

        if error is not None:
            # SI HAY ERROR:
            return render("inicioSesion.html", form=form, titulo='Inicio de sesión')
        else:
            # No hay error:
            user = db.execute(
                'SELECT * FROM usuarios WHERE id_cedula= ? AND password= ? AND id_perfil= ?'
                ,
                (usuario,password,perfil)
            ).fetchone()            
            if user is None:
                error = "Usuario y contraseña no son correctos."
                flash( error )                
                return render ("inicioSesion.html", form=form, titulo='Inicio de sesión')
            else:  
                if perfil == '1':
                    return redirect(url_for('empleado'))
                elif perfil == '2':
                     return redirect(url_for('administrador'))
                else:
                    return redirect(url_for('superadministrador'))

    # GET:
    return render ("inicioSesion.html", form=form, titulo='Inicio de sesión')



       
@app.route('/empleado', methods=["GET" , "POST"])
def empleado():

    con = sql.connect("empleados.db")
    
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute('SELECT id_cedula, nombre, apellido, direccion,correo, celular, salario, nombre_cargo, nombre_dependencia, nombre_tipo_contrato, fecha_ingreso,fecha_termino FROM usuarios JOIN cargo on cargo.id_cargo = usuarios.id_cargo JOIN dependencia on dependencia.id_dependencia = usuarios.id_dependencia JOIN tipo_contrato on tipo_contrato.id_tipo_contrato = usuarios.id_tipo_contrato JOIN perfil on perfil.id_perfil = usuarios.id_perfil WHERE id_cedula= ?',
    (usuario))


    rows = cur.fetchall()
    return render ("empleado.html",rows=rows)





@app.route('/administrador', methods=["GET", "POST"])
def administrador():
    con = sql.connect("empleados.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT id_cedula, nombre, apellido, direccion,correo, celular, salario, nombre_cargo, nombre_dependencia, nombre_tipo_contrato, nombre_perfil,password, fecha_ingreso,fecha_termino FROM usuarios JOIN cargo on cargo.id_cargo = usuarios.id_cargo JOIN dependencia on dependencia.id_dependencia = usuarios.id_dependencia JOIN tipo_contrato on tipo_contrato.id_tipo_contrato = usuarios.id_tipo_contrato JOIN perfil on perfil.id_perfil = usuarios.id_perfil")

    rows = cur.fetchall()
    return render ("administrador.html",rows=rows)





@app.route('/superadministrador', methods=["GET", "POST"])
def superadministrador():
    con = sql.connect("empleados.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT id_cedula, nombre, apellido, direccion,correo, celular, salario, nombre_cargo, nombre_dependencia, nombre_tipo_contrato, nombre_perfil,password, fecha_ingreso,fecha_termino FROM usuarios JOIN cargo on cargo.id_cargo = usuarios.id_cargo JOIN dependencia on dependencia.id_dependencia = usuarios.id_dependencia JOIN tipo_contrato on tipo_contrato.id_tipo_contrato = usuarios.id_tipo_contrato JOIN perfil on perfil.id_perfil = usuarios.id_perfil")

    rows = cur.fetchall()
    return render ("superadministrador.html",rows=rows)
    




@app.route('/editar', methods=["GET", "POST"])
def editar():
    form = feditar( request.form )
    if request.method == 'POST':        
        flash( form.enombre.data)
        flash( form.eapellidos.data)
        flash( form.ecorreo.data )
        flash( form.eidentificacion.data)
        flash( form.edireccion.data )
        flash( form.etelefono.data )
        flash( form.efechaingreso.data)
        flash( form.etipocontrato.data)
        flash( form.efechaterminacion.data )
        flash( form.ecargo.data)
        flash( form.edependencia.data )
        flash( form.esalario.data )
        return render("editar.html", form=form)
    return render ("editar.html", form=form)

@app.route('/CrearEmpleado', methods=["GET", "POST"])
def CrearEmpleado():
    return render("CrearEmpleado.html")

@app.route('/retroalimentacion', methods=["GET", "POST"]) #podria varias si solo es de consulta o si puede actulizar sus datos
def perfil():

    return render("retroalimentacion.html")






if __name__ == "__main__":

    app.run(debug = True)
    

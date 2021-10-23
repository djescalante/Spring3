from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, email, length


class flogin(FlaskForm):
    usuario = StringField('Usuario', validators =[
        DataRequired(),
        length(max=30, min=1)
    ])
    password = PasswordField('Contraseña', validators =[
        DataRequired(),
        length(max=30, min=1)
    ])
    perfil = SelectField("perfil  ",choices=[("1","Empleado"),("2","Administrador"),("3","SuperAdmin")])

    submit = SubmitField('Iniciar sesion')
    
class fempleado(FlaskForm):
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    correo = StringField('Correo')
    identificacion = StringField('Identificacion')
    direccion = StringField('Direccion')
    telefono = StringField('Telefono')
    fechaingreso = StringField('Fecha de Ingreso')
    tipocontrato = StringField('Tipo de Contrato')
    fechaterminacion = StringField('Fecha de Terminacion')
    cargo = StringField('Cargo')
    dependencia = StringField('Dependencia')
    salario = StringField('Salario')
    retroalimentacion = TextAreaField('Retroalimentacion')
    puntaje = StringField('Puntaje')
    submit = SubmitField('Cerrar sesion')

class feditar(FlaskForm):
    enombre = StringField('Nombre')
    eapellidos = StringField('Apellidos')
    ecorreo = StringField('Correo')
    eidentificacion = StringField('Identificacion')
    edireccion = StringField('Direccion')
    etelefono = StringField('Telefono')
    efechaingreso = StringField('Fecha de Ingreso')
    etipocontrato = StringField('Tipo de Contrato')
    efechaterminacion = StringField('Fecha de Terminacion')
    ecargo = StringField('Cargo')
    edependencia = StringField('Dependencia')
    esalario = StringField('Salario')
    egsubmit = SubmitField('Guardar')
    ecsubmit = SubmitField('Cancelar')
    evubmit = SubmitField('Volver')
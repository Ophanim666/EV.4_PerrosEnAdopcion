// objeto.metodo(json)

$("#formulario1").validate({
    rules: {
        "nombre": {
            required: true,
            nombre: true
        },
        "usuario": {
            required: true,
            usuario: true
        },
        "txtEmail": {
            required: true,
            email: true
        },
        "txtContrasena": {
            required: true,
            minlength: 5
        },
        "txtRepetirContrasena": {
            required: true,
            equalTo: '#id_txtContrasena'
        }
    }, // --> Fin de reglas
    messages: {
        "txtNombre": {
            required: 'Ingrese su nombre!!!',
            nombre: 'No cumple formato'
        },
        "txtUsuario": {
            required: 'Ingrese su nombre de usuario!!!',
            usuario: 'No cumple formato'
        },
        "txtEmail": {
            required: 'Ingrese email!!!',
            email: 'No cumple formato'
        },
        "txtContrasena": {
            required: 'Ingrese Password!!!',
            minlength: 'Min. 5 caract'
        },
        "txtRepetirContrasena": {
            required: 'Repita el Password!!',
            equalTo: ' deben ser iguales!!!!'
        }
    } //-->Fin de mensajes

});

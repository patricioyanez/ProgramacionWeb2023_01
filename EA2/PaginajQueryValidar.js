$(function()
{
    // codigo jQuery o JS
    let numeros = '0123456789';
    let letras  = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÍÓÚáéíóú';
    // validación campos vacios
    $('.btnEnviar').click(function()
    {
        if(!$('.txtRut').val())
        {
            alert("Falta especificar el rut");
            $('.txtRut').focus();
        }
        else if(!$('.txtDv').val())
        {
            alert("Falta especificar el dv")
            $('.txtDv').focus();
        }
        else if(!$('.txtNombre').val())
        {
            alert("Falta especificar el nombre")
            $('.txtNombre').focus();
        }
        else if(!$('.txtEmail').val())
        {
            alert("Falta especificar el email")
            $('.txtEmail').focus();
        }
    })
})
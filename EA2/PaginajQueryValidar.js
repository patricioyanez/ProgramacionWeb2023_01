$(function()
{
    // codigo jQuery o JS

    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/

    $('.btnLimpiar').click(function()
    {
        $('.txtRut, .txtDv, .txtNombre, .txtEmail').val('');
        $('.txtRut').focus();
    })

    let numeros = '0123456789';
    let letras  = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÍÓÚáéíóú';

    $('.txtRut').keypress(function(e)
    { 
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    });

    $('.txtDv').keypress(function(e)
    { 
        let patron = numeros + 'kK';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    });
    
    $('.txtNombre').keypress(function(e)
    { 
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;
    });
    $('.txtEmail').keypress(function(e)
    { 
        let patron = numeros + letras + '-_.@';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    });
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
        else if(! esValidoElRut($('.txtRut').val(),$('.txtDv').val()))
        {
            alert("El rut no es válido")
            $('.txtRut').focus();
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
        else if(! emailRegex.test($('.txtEmail').val()))
        {
            alert("El formato del correo no es válido")
            $('.txtEmail').focus();
        }
    })

    function esValidoElRut(Rut,Digito)
    {
		let contador= Rut.length-1;
		let factor  = 2;
		let suma    = 0;
		let caracter= 0;
 
		for( ; contador>=0 ; contador--)
		{
			caracter = Rut.charAt(contador);
			suma += (factor * caracter);
			if (++factor > 7)
				factor=2;		
		}
        return "-123456789K0".charAt(11-(suma % 11)) == Digito.toUpperCase();            
    }  
})
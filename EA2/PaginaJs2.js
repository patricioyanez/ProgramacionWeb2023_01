function sumar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    let total = parseInt("0" + n1) +  parseInt("0" + n2);
    document.getElementById("resultado").value = total;
}
function limpiar()
{
    document.getElementById("numero1").value = "";
    document.getElementById("numero2").value = "";
    document.getElementById("resultado").value = "";
}


// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero
// y que no esten vacios).
function restar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    let total = parseInt("0" + n1) -  parseInt("0" + n2);
    document.getElementById("resultado").value = total;
}

function multiplicar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    let total = parseInt("0" + n1) *  parseInt("0" + n2);
    document.getElementById("resultado").value = total;
    // NaN
}

function dividir()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    n1 = parseInt("0" + n1);
    n2 = parseInt("0" + n2);

    if(n2 == 0)
    {
        alert("No se puede dividir por cero");
        return;
    }
    let total = n1 /  n2;
    document.getElementById("resultado").value = total;
}2

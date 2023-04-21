function sumar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    let total = parseInt(n1) +  parseInt(n2);
    document.getElementById("resultado").value = total;
}


// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero
// y que no esten vacios).
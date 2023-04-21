function sumar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    let total = parseInt(n1) +  parseInt(n2);
    document.getElementById("resultado").value = total;
}
function sumar(numUno, numDos) {
    return numUno + numDos;
}
function restar(numUno, numDos) {
    return numUno - numDos;
}
function multiplicar(numUno, numDos) {
    return numUno * numDos;
}
function dividir(numUno, numDos) {
    return numUno / numDos;
}
function main() {
    calculadora();
}
function calculadora() {
    var operacion = prompt('Selecciona una operacion: "suma-1", "resta-2", "multiplicacion-3", "division-4","terminamos-5"');
    var esSuma = operacion == 'suma' ||
        operacion == '1' ||
        operacion == 'suma-1';
    var esResta = operacion == 'resta' ||
        operacion == '2' ||
        operacion == 'resta-2';
    var esMultiplicacion = operacion == 'multiplicacion' ||
        operacion == '3' ||
        operacion == 'multiplicacion-3';
    var esDivision = operacion == 'divivison' ||
        operacion == '4' ||
        operacion == 'division-4';
    var esTerminamos = operacion == 'terminamos' ||
        operacion == '5' ||
        operacion == 'terminamos-5';
    var estaValida = esSuma || esResta || esMultiplicacion || esDivision;
    if (estaValida) {
        var numUno = +prompt("Numero 1");
        var numDos = +prompt("Numero 2");
        var resultado = 0;
        if (esSuma) {
            resultado = sumar(numUno, numDos);
        }
        if (esResta) {
            resultado = restar(numUno, numDos);
        }
        if (esMultiplicacion) {
            resultado = multiplicar(numUno, numDos);
        }
        if (esDivision) {
            resultado = dividir(numUno, numDos);
        }
        console.log(resultado);
        calculadora();
    }
    else {
        if (setermino) {
            console.log("Adios:´(");
        }
        else {
            calculadora();
        }
    }
}

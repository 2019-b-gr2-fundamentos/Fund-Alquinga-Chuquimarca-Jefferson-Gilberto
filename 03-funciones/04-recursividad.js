function imprimirMensajeNVeces(mensaje, numeroVeces) {
    if (numeroVeces == 0) {
        console.log("Se termino");
    }
    else {
        console.log("mensaje");
        var nuevoNumeroVeces = numeroVeces - 1;
        imprimirMensajeNVeces(mensaje, nuevoNumeroVeces);
    }
}
function main() {
    imprimirMensajeNVeces("hola", 3);
}
main();
 
/* utilizar la funcion recursiva para imprimir todo el arreglo com lo hago en typescript y python 
analizar eso en casa*/ 
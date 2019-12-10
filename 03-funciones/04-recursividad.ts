function imprimirMensajeNVeces(
    mensaje:string,
    numeroVeces:number
):void{ 
    if(numeroVeces == 0){
        console.log("Se termino");
    }else{
        console.log("mensaje");
        const nuevoNumeroVeces = numeroVeces -1;
        imprimirMensajeNVeces(mensaje,nuevoNumeroVeces);
    }
}

function main(){
    imprimirMensajeNVeces("hola",3);
}

main();


const arregloNumero: number[] = [1,2,3];
const arregloString: string[] = [´a´, ´b ´, ´c´];
const arregloBoolean:boolean[true, false, false];

function imprimir(arreglo: number[]){


}
/*utilizar el indice y el tamaño*/

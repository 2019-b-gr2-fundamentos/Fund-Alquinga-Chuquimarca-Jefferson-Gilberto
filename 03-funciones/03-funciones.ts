function sumar(numUno:number, numDos:number): number{
    return numUno + numDos;
}
function restar(numUno:number, numDos:number): number{
    return numUno - numDos;
}
function multiplicar(numUno:number, numDos:number): number{
    return numUno * numDos;
}
function dividir(numUno:number, numDos:number): number{
    return numUno / numDos;
}
 
function main(){
 
}
function calculadora(){
    const operacion:string = prompt('Selecciona una operacion: "suma-1", "resta-2", "multiplicacion-3", "divivison-4"');
    const esSuma:boolean = operacion == 'suma' ||
     operacion == '1' || 
     operacion == 'suma-1';
     const esResta:boolean = operacion == 'resta' ||
     operacion == '2' || 
     operacion == 'resta-2';
     const esMultiplicacion:boolean = operacion == 'multiplicacion' ||
     operacion == '3' || 
     operacion == 'multiplicacion-3';
     const esDivision:boolean = operacion == 'divivison' ||
     operacion == '4' || 
     operacion == 'divivison-1';
 
    const estaValida:boolean = esSuma || esResta || esMultiplicacion || esDivision;
 
    if(estaValida){
        const numUno:number = +prompt("Numero 1");
        const numDos:number = +prompt("Numero 2");
        let resultado = 0;
        if(esSuma){
            sumar(numUno, numDos);
        }
        if(esResta){
            restar(numUno, numDos);
        }
        if(esMultiplicacion){
            multiplicar(numUno, numDos);
        }
        if(esDivision){
            dividir(numUno, numDos);
        }
    }
 
}





 
/*
1) Seleccionar operacion
2.1) La seleccion no es VALIDA
    2.1.1) Vuelve a seleccionar la operacion 
2.2) La seleccion es VALIDA
    2.2.1) Ingresar primer numero
    2.2.2) Ingresar segundo numero
    2.2.3) Ejecutar la operacion
 
*/

//hacer una la igualdad de 2 dos matrices de orden n x m 
//  condiciones    que n=m  las matrcies no aceptan a n!=m

function compararMatriz(
      matrizUno: number[][],
      matrizDos: number[][]
): boolean{
    return true;

}
compararMatriz([[2,3],[3,4]],[[2,3],[3,4]])
    console.log("row 1 , row 2  ")

import* as fs from 'fs';

export function escribirtArchivo(contenido: string){
    fs.writeFileSync(
        './ejemplo.txt', // Path
        'NUEVO CONTENIDO :D ' + contenido, // CONTENIDO
        'utf8'  // CODIFICACION)
    
}
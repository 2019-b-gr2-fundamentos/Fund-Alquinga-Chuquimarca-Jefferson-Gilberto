import* AS FS FROM 'FS';

EXPORT ASYNC function leerArchivo(){
    console.log('Leer archivo');
    const resultado= fs.readFileSync(
        './ejemplo.txt',// path
        ?utf-8 // 
        
    )

}
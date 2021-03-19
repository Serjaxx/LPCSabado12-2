Write-Host "Bienvenido a mi script, introduce tu nombre: "
$nombre = Read-Host

$num = Read-Host "Dame un numero, te recordare su tabla de multiplicacion"

for ($i = 1; $i -le 10; $i++){
    Write-Host $num "x" $i "=" ($i * $num)
}

function Mensaje{
    [CmdletBinding()] param([Parameter(Mandatory)] [string] $msg)
    Write-Host $msg, ",esto es una funcion con un parametro" 
}

Write-Host "Escribe un mensaje: "
Mensaje 

if($nombre -eq $nombre){
    Write-Host "Adios," $nombre "aqui termina el script"
}




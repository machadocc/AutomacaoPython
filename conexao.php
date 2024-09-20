<?php

$hostname = "localhost";
$bancodedaos = "bancodedados"; 
$usuario = "usuario";
$senha = "senha";

$mysqli = new mysqli($hostname, $usuario, $senha, $bancodedaos);
if ($mysqli_connect_errno) {

    echo "falha no banco: (" . $mysqli->connect_errno . ") ". $mysqli->connect_error;
}

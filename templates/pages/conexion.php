<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "inter_bd";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

// Función para cerrar la conexión
function cerrarConexion($conn) {
    $conn->close();
    echo "Disconnected successfully";
}
?>
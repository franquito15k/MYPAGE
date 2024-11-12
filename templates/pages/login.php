<?php
include 'conexion.php';
session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        html,
        body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow-x: hidden;
            color: #8b1a32;
            background-color: #461220;
        }

        main {
            margin: 0px;
            padding: 0px;
            width: 100%;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        header {
            background-color: #ce796b;
            margin-bottom: 10px;
            padding: 10px 0;
        }

        .flex {
            display: flex;
            width: 100%;
            justify-content: center;
            align-items: center;
        }

        .row {
            flex-direction: row;
        }

        .buttom-style {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 12px 30px;
            margin: 5px 5px;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 2.5px;
            font-weight: 500;
            color: #000;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 25%;
            text-decoration: none;
        }

        .buttom-style:hover {
            background-color: crimson;
            border-radius: 20px;
            box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
            color: #fff;
            transform: translateY(-7px);
        }

        .video-button:hover {
            background-color: #f7a072;
            font-size: 20px;
            box-shadow: 0px 15px 20px rgba(194, 54, 54, 0.4);
            color: #fff;
            transform: translateY(-5px);
        }

        .audio-button:hover {
            background-color: turquoise;
            font-size: 20px;
            color: #fff;
            transform: translateY(-5px);
            box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
        }

        /* Estilo del formulario */
        section {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            background-color: #6a1b2a;
            color: #fff;
            border-radius: 10px;
            text-align: left;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label,
        input {
            margin-bottom: 10px;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 8px;
            border-radius: 5px;
            border: none;
            font-size: 16px;
        }

        button {
            padding: 10px;
            background-color: #ce796b;
            border: none;
            color: #fff;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #d97979;
        }

        a {
            color: #f1c2b1;
            text-decoration: none;
            margin-top: 10px;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <header>
        <div class="flex row">
            <div class="flex row" id="nav" style="visibility: visible;">
                <a class="buttom-style" href="http://127.0.0.1:5000/" id="home">Instant Download</a>
                <div class="flex row" id="button-nav">
                    <a href="http://127.0.0.1:5000/" class="buttom-style video-button">Descargar Video de Youtube</a>
                    <a href="http://localhost/MYPAGE/templates/pages/register.php" class="buttom-style">Registro</a>
                    <a href="http://localhost/MYPAGE/templates/pages/login.php" class="buttom-style">Login</a>
                </div>
            </div>
        </div>
    </header>

    <section id="login" class="section">
        <h2>Iniciar Sesión</h2>
        <form action="login.php" method="POST">
            <label for="login-username">Nombre de Usuario:</label>
            <input type="text" id="nombre" name="nombre" required>

            <label for="login-password">Contraseña:</label>
            <input type="password" id="clave" name="clave" required>

            <button type="submit">Iniciar Sesión</button>
            <a href="http://127.0.0.1:5000/">Volver al inicio</a>
        </form>
    </section>
</body>

</html>


<?php
if (isset($_GET['salir'])) {
    session_destroy();
    echo "<script>window.location='http://127.0.0.1:5000/';</script>";
}

//iniciar sesion
if (isset($_POST['nombre']) && isset($_POST['clave'])) {
    $sql = "SELECT * FROM usuarios WHERE nombre='" . $_POST['nombre'] . "'";
    $sql = mysqli_query($conn, $sql);
    if (mysqli_num_rows($sql) != 0) {
        $r = mysqli_fetch_array($sql);
        if (password_verify(addslashes($_POST['clave']), $r['clave'])) {
            //crear las vbles. de sesion
            $_SESSION['id'] = $r['id'];
            $_SESSION['nombre_usuario'] = $r['nombre'];

            // Insertar el ID y el nombre del usuario en la tabla de sesiones
            $session_id = session_id();
            $usuario_id = $r['id'];
            $last_activity = date('Y-m-d H:i:s');
            $insert_session_sql = "INSERT INTO sesiones (session_id, usuario_id, username, last_activity) VALUES ('$session_id', '$usuario_id', '" . $r['nombre'] . "', '$last_activity')";
            mysqli_query($conn, $insert_session_sql);
            
            echo "<script>alert('Bienvenido: " . $_SESSION['nombre_usuario'] . " (ID: " . $_SESSION['id'] . ")');</script>";
        } else {
            echo "<script>alert('Clave incorrecta.');</script>";
        }
    } else {
        echo "<script>alert('Verifique los datos.');</script>";
    }
    echo "<script>window.location='http://127.0.0.1:5000/';</script>";
}

<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Instant Download</title>
  <link rel="stylesheet" href="../static/css/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Nunito:wght@200..1000&display=swap"
    rel="stylesheet" />
  <!--mmenu.js jquery-->
  <script src="https://markcell.github.io/jquery-tabledit/assets/js/jquery.tabledit.min.js"></script>
</head>

<body>
  <header>
    <div class="flex row">
        <div class="flex row" id="nav" style="visibility: visible;">
            <a class="buttom-style" href="{{ url_for('index') }}" id="home">Instant Download</a>
            <div class="flex row" id="button-nav">
                <a href="{{ url_for('index') }}" class="buttom-style video-button">Descargar Video de Youtube</a>
                {% if nombre_usuario %}
                <h2>Bienvenido, {{ nombre_usuario }}!</h2>
                <!-- Formulario para cerrar sesión -->
                <form action="{{ url_for('logout') }}" method="POST" style="display: inline;">
                    <button type="submit" class="buttom-style" style="border: none; background-color:#ce796b">Cerrar sesión</button>
                </form>
                {% else %}
                    <a href="http://localhost/MYPAGE/templates/pages/register.php" class="buttom-style">Registro</a>
                    <a href="http://localhost/MYPAGE/templates/pages/login.php" class="buttom-style">Login</a>
                {% endif %}
            
            </div>
        </div>
        <nav id="menu" style="visibility: hidden;">
            <ul>
                <li><a href="{{ url_for('index') }}">Instant Download</a></li>
                <li><a href="{{ url_for('index') }}">Descargar Video de Youtube</a></li>
            </ul>
        </nav>
    </div>
  </header>



  <div class="content-wrapper">
    <main>
      <div class="recuadros">
        <section class="flex column align-items-center">
          <h3>Descargar Video de Youtube</h3>
          <form class="flex row justify-row" id="downloadForm">
            <div>
              <label for="url">Pegar alado la URL: </label>
            </div>
            <div>
              <input type="text" name="url" id="url" placeholder="Pegar el enlace aquí..." required>
            </div>
            <div>
              <button type="submit">Obtener el video del enlace</button>
            </div>
          </form>
        </section>
        <img src="/loadingcat.jpg" alt="loading gif" id="loadingGif" style="display: none;">
        <section class="flex column align-items-center justify-content-center">
          <h2>Instant Download - El mejor descargador de mp4 de Youtube 202</h2>
          <p>"Youtube to Video" es una herramienta que permite descargar videos de Youtube rápidamente y en diversos formatos, como MP4, sin necesidad de conversión de audio.</p>
        </section>

        <section class="flex column align-items-center justify-content-center">
          <h2>Cómo descargar mp3 de Youtube más rápido</h2>
          <div class="flex row justify-content-center" id="tablet-query">
            <div class="flex row" id="text-img">
              <img src="/static/img/link-solid.png" alt="link-image" width="32" height="32">
              <div>Pegue el enlace convertir YouTube a MP3 en el cuadro de búsqueda</div>
            </div>
            <div class="flex row" id="text-img">
              <img src="/static/img/settings.png" alt="configurator-image" width="32" height="32">
              <div>Haga clic en el botón "Obtener video del enlace"</div>
            </div>
            <div class="flex row" id="text-img">
              <img src="/static/img/download.png" alt="download-image" width="32" height="32">
              <div>Espere unos segundos a que se complete la conversión de YouTube a MP4 y se descargara automaticamente en su carpeta de "DESCARGAS/DOWNLOADS"</div>
            </div>
          </div>
        </section>
      </div>
    </main>
    <aside class="top10-songs">
      <h2>Top 10 Canciones Más Descargadas</h2>
      <ol>
        <li>Blinding Lights - The Weeknd</li>
        <li>Dance Monkey - Tones and I</li>
        <li>Shape of You - Ed Sheeran</li>
        <li>Levitating - Dua Lipa</li>
        <li>Peaches - Justin Bieber</li>
        <li>Save Your Tears - The Weeknd</li>
        <li>Rockstar - Post Malone</li>
        <li>Don't Start Now - Dua Lipa</li>
        <li>Bad Guy - Billie Eilish</li>
        <li>Good 4 U - Olivia Rodrigo</li>
      </ol>
    </aside>
  </div>

  <footer></footer>
  <script src="/static/JS/python.js"></script>
  <script src="/static/JS/inc_global.js"></script>
</body>

</html>

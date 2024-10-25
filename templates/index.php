<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instant Download</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Nunito:wght@200..1000&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="/static/css/styles.css">
    <!--mmenu.js jquery-->
    <link href="../static/css/" rel="stylesheet" />
    <script src="mmenu.js"></script>

  </head>

  <body>
    <header >
      <div class="flex row">
        <div class="flex row" id="nav" style="visibility: visible;"><!--row-->
          <a class="buttom-style" href="{{url_for('index')}}" id="home">Instant Download</a>
          <div class="flex row" id="button-nav">
            <a href="{{url_for('index')}}" class="buttom-style video-button">Descargar Video de Youtube</a>
            <!--<a href="{{url_for('index')}}" class="buttom-style audio-button">Descargar Audio de Youtube</a>-->
          </div>
        </div>
        <nav id="menu" style="visibility: hidden;">
          <ul>
              <li><a href="{{url_for('index')}}">Instante Download</a></li>
              <li><a href="{{url_for('index')}}">Descargar Video de Youtube</a></li>
          </ul>
        </nav>
        <!--  
          <div class="flex column" id="login">column
            <a class="buttom-style" href="{{url_for('register')}}">Registrate</a>
            <a class="buttom-style" href="{{url_for('login')}}">Ingresar</a>
          </div>
        -->
      </div>
    </header>

    <main>
      <div class="recuadros" ><!--main flex column -->
        <section class="flex column align-items-center "><!--flex descarga video url column  -->  
          <h3><!--texto-->
            Descargar Video de Youtube
          </h3>

          <form class="flex row justify-row" id="downloadForm">
            <div>
              <label for="url">Pegar alado la URL: </label>
            </div>
            <div>
              <input type="text" name="url" id="url" placeholder="Pegar el enlace aquí..." required>
            </div>
            <div><!--buttom-->
              <button type="submit">Obtener el video del enlace</button> 
            </div>
          </form><!--input url-->
        </section>
        <img src="/static/img/loadingcat.jpg" alt="loading gif" id="loadingGif" style="display: none;">
 

      </div>
    </main>

    <footer></footer>
    <script src="/static/JS/python.js"></script>
    <script src="/static/JS/inc_global.js"> </script>
  </body>
</html>

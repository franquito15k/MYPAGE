// mini funcion que me permite validar el form para que no incremente el global.json
function validateAndDownload() {
    const videoUrl = document.getElementById('url').value;
    if (!videoUrl) {
        alert("Por favor, introduce la URL del video.");
        return; 
    }
    sum_download();
}

// funcion que hjace la solicitud post para la suma del json
function sum_download() {
    fetch('/sumar_descarga', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message); 
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
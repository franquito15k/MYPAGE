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
function startDownload() {
    const url = document.getElementById('videoUrl').value;

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            checkProgress();
        }
    });
}

function checkProgress() {
    fetch('/progress')
    .then(response => response.json())
    .then(data => {
        const progressBar = document.getElementById('progressBar');
        progressBar.value = data.progress;
        if (data.status === 'downloading') {
            setTimeout(checkProgress, 1000);
        } else if (data.status === 'finished') {
            alert('¡Descarga completa!');
        }
    });
}
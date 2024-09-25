// obtego el formulario y el gif
const downloadForm = document.getElementById('downloadForm');
const loadingGif = document.getElementById('loadingGif');
const submitButton = downloadForm.querySelector('button[type="submit"]');

// muestro el gif, cambio el cursor y deshabilito el formulario
function showLoadingGif() {
  loadingGif.style.display = 'block'; 
  document.body.style.cursor = 'wait'; 
  submitButton.disabled = true; 
  Array.from(downloadForm.elements).forEach(el => el.disabled = true); 
}

// oculto el gif, restauro el cursor y habilito el formulario
function hideLoadingGif() {
  loadingGif.style.display = 'none'; 
  document.body.style.cursor = 'default'; 
  submitButton.disabled = false; 
  Array.from(downloadForm.elements).forEach(el => el.disabled = false); 
}

document 
  .getElementById("downloadForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    showLoadingGif();

    const urlInput = document.getElementById("url").value;
    
    //envia una solicitud post a /download con la url proporcionada por el usuario
    try {
      const response = await fetch("/download", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: urlInput }),
      });

      if (response.ok) {
        // obetengo el nombre del header para crear el nombre del archivo
        const disposition = response.headers.get("Content-Disposition");
        const filename = disposition.match(/filename="(.+)"/)[1];
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        // Crea un enlace temporal para descargar el archivo
        const a = document.createElement("a");
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        a.remove();

        // limpia el formulario al finalizar la solicitud
        document.getElementById("downloadForm").reset();
        hideLoadingGif();

      } else {
        const errorData = await response.json();
        alert(`Error: ${errorData.error}`);
        hideLoadingGif();
      }
    } catch (error) {
      console.error("Error al descargar el video:", error);
      alert("Hubo un problema, volve a intentarlo.");
      hideLoadingGif();
    }
  });

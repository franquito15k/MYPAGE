document.getElementById('downloadForm').addEventListener('submit', async function (e) {
    e.preventDefault(); // Evita que el formulario se envíe de la forma tradicional

    const urlInput = document.getElementById('url').value;
    const statusElement = document.getElementById('status');

    if (!urlInput) {
      statusElement.innerText = 'Por favor, ingresa una URL válida.';
      return;
    }

    statusElement.innerText = 'Descargando video...';

    try {
      // Enviar solicitud al servidor con la URL del video
      const response = await fetch('/download_video', {
        method: 'POST',
        body: new URLSearchParams({ url: urlInput })
      });

      if (!response.ok) {
        const errorData = await response.json();
        statusElement.innerText = `Error: ${errorData.error}`;
        return;
      }

      // Extraer el nombre del archivo del encabezado Content-Disposition
      const disposition = response.headers.get('Content-Disposition');
      let filename = 'video_descargado.mp4';
      if (disposition && disposition.includes('filename=')) {
        filename = disposition.split('filename=')[1].replace(/"/g, '');
      }

      // Crear un enlace de descarga
      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = downloadUrl;
      a.download = filename;
      document.body.appendChild(a);
      a.click();

      // Limpiar el enlace temporal
      window.URL.revokeObjectURL(downloadUrl);
      a.remove();

      statusElement.innerText = 'Video descargado con éxito.';
    } catch (error) {
      statusElement.innerText = `Error al descargar el video: ${error.message}`;
    }
  });
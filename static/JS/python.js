document
  .getElementById("downloadForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

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
      } else {
        const errorData = await response.json();
        alert(`Error: ${errorData.error}`);
      }
    } catch (error) {
      console.error("Error al descargar el video:", error);
      alert("Hubo un problema, volve a intentarlo.");
    }
  });

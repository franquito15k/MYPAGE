function createCarousel(carouselSelector, prevButtonSelector, nextButtonSelector) {
    let currentIndex = 0;

    const carousel = document.querySelector(carouselSelector);
    const container = carousel.querySelector('.carousel-container');
    const slides = container.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;
    const slideWidth = slides[0].offsetWidth + 10; // Añadimos el margen derecho
    const containerWidth = container.offsetWidth;

    const prevButton = document.querySelector(prevButtonSelector);
    const nextButton = document.querySelector(nextButtonSelector);

    function moveSlide(direction) {
        currentIndex += direction;

        // Evitar que el índice se salga de los límites
        if (currentIndex < 0) {
            currentIndex = totalSlides - Math.floor(containerWidth / slideWidth);
        } else if (currentIndex > totalSlides - Math.floor(containerWidth / slideWidth)) {
            currentIndex = 0;
        }

        const offset = -currentIndex * slideWidth;
        container.style.transform = `translateX(${offset}px)`;
    }

    function checkOverflow() {
        if (container.scrollWidth > carousel.offsetWidth) {
            prevButton.style.display = 'block';
            nextButton.style.display = 'block';
        } else {
            prevButton.style.display = 'none';
            nextButton.style.display = 'none';
        }
    }

    // Event listeners para los botones prev y next
    prevButton.addEventListener('click', () => moveSlide(-1));
    nextButton.addEventListener('click', () => moveSlide(1));

    // Ajustar cuando se cambie el tamaño de la ventana
    window.addEventListener('resize', checkOverflow);
    window.addEventListener('load', checkOverflow);

    // Llama a la verificación inicial
    checkOverflow();
}

// Ejemplo de uso para múltiples carruseles
createCarousel('#carousel1', '#carousel1-prev', '#carousel1-next');
createCarousel('#carousel2', '#carousel2-prev', '#carousel2-next');
createCarousel('#carousel3', '#carousel3-prev', '#carousel3-next');
createCarousel('#carousel4', '#carousel4-prev', '#carousel4-next');

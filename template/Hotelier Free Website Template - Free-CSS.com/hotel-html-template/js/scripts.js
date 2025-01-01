let currentSlide = 0;
const slides = document.querySelectorAll('.slider-image');
const totalSlides = slides.length;

// Function to show the slide at the given index
function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.remove('active');
        if (i === index) {
            slide.classList.add('active');
        }
    });
}

// Function to change the slide every 3 seconds
function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    showSlide(currentSlide);
}

// Initializing the first slide
showSlide(currentSlide);

// Automatically change the slide every 3 seconds
setInterval(nextSlide, 3000);

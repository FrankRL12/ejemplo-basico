const slider = document.querySelector('.slider');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const slideWidth = slider.clientWidth;

let slideIndex = 0;

function slideTo(index) {
  slider.style.transform = `translateX(-${index * slideWidth}px)`;
}

function prevSlide() {
  slideIndex--;
  if (slideIndex < 0) {
    slideIndex = slider.childElementCount - 1;
  }
  slideTo(slideIndex);
}

function nextSlide() {
  slideIndex++;
  if (slideIndex >= slider.childElementCount) {
    slideIndex = 0;
  }
  slideTo(slideIndex);
}

prevBtn.addEventListener('click', prevSlide);
nextBtn.addEventListener('click', nextSlide);

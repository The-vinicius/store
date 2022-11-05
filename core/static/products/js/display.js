let slideIndex = 1;
let count = 0;

setInterval(showSlides, 3000);


function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < 3; i++) {
    slides[i].style.display = "none";
  }
  slides[count].style.display = "grid";
  count++;
  if (count >= 3) {
    count = 0;
  }
}



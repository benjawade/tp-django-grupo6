document.addEventListener("DOMContentLoaded", function() {
  const images = document.querySelectorAll(".image-gallery img");

  images.forEach((img, index) => {
    img.style.opacity = 0;
    img.style.transform = "scale(0.8)";
    img.style.transition = "opacity 0.5s ease-in-out, transform 0.5s ease-in-out";
    setTimeout(() => {
      img.style.opacity = 1;
      img.style.transform = "scale(1)";
    }, index * 200);
  });

  const backButton = document.querySelector(".button-container a");
  backButton.addEventListener("mouseover", function() {
    backButton.style.backgroundColor = "#ff6f61";
    backButton.style.transition = "background-color 0.3s ease-in-out";
  });

  backButton.addEventListener("mouseout", function() {
    backButton.style.backgroundColor = "";
  });
});

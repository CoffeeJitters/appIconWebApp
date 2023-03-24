/* Add this to your main.js file */

// Show/hide navigation menu on mobile devices
const menuButton = document.querySelector('.menu-button');
const navMenu = document.querySelector('nav ul');

menuButton.addEventListener('click', () => {
  navMenu.classList.toggle('show');
});

// Display uploaded image in form
const imageInput = document.querySelector('#image');
const imagePreview = document.querySelector('.image-preview');

imageInput.addEventListener('change', () => {
  const file = imageInput.files[0];
  const reader = new FileReader();

  reader.addEventListener('load', () => {
    imagePreview.src = reader.result;
  });

  reader.readAsDataURL(file);
});

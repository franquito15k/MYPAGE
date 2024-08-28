const toggleButton = document.getElementById('toggleButton');
const productList = document.querySelector('.product-list');

toggleButton.addEventListener('click', () => {
  productList.classList.toggle('visible');
});

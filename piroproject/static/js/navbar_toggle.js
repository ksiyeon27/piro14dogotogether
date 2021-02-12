const toggleBtn = document.querySelector('.navbar_toggleBtn');
const menu = document.querySelector('.menu');

toggleBtn.addEventListener('click',function(e){
    menu.classList.toggle('active');
    e.preventDefault();
});

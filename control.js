const menu = document.getElementById('menu')
const button2 = document.getElementById('closeMenu');
const button = document.getElementById('openMenu');

function showMenu(){
    menu.style.display = 'block';
    button.style.display = 'none'
}

function hideMenu(){
    menu.style.display = 'none';
    button.style.display = 'block'
}

button.addEventListener('click', showMenu);
button2.addEventListener('click', hideMenu);
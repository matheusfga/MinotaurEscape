const minotaur = document.getElementById('minotaur-container');
const maze = document.getElementById('maze-container');

let minotaurX = 0;
let minotaurY = 0;
const step = 10;

document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'w':
            minotaurY -= step;
            break;
        case 's':
            minotaurY += step;
            break;
        case 'a':
            minotaurX -= step;
            break;
        case 'd':
            minotaurX += step;
            break;
    }

    minotaur.style.transform = `translate(${minotaurX}px, ${minotaurY}px)`;
});
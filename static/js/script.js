const minotaur = document.getElementById('minotaur-container');
const maze = document.getElementById('maze-container');

let minotaur_x = -640; //  -640 560
let minotaur_y = -320; // -320 240
const step = 40;

var start_position = start_position;
minotaur_x += (start_position.x * 40)
minotaur_y += (start_position.y * 40)
minotaur.style.transform = `translate(${minotaur_x}px, ${minotaur_y}px)`

console.log(start_position)

document.addEventListener('keydown', async (event) => {
    let new_x = minotaur_x;
    let new_y = minotaur_y;
    let arg_x = 0;
    let arg_y = 0;
    
    switch (event.key) {
        case 'w':
            new_y -= step;
            arg_y = -1;
            break;
        case 's':
            new_y += step;
            arg_y = 1;
            break;
        case 'a':
            new_x -= step;
            arg_x = -1;
            break;
        case 'd':
            new_x += step;
            arg_x = 1;
            break;
    }

    const response = await validate_step(arg_x, arg_y);
    if(response.success) {
        minotaur_x = new_x;
        minotaur_y = new_y;
        minotaur.style.transform = `translate(${minotaur_x}px, ${minotaur_y}px)`;
        if(response.final) {
            alert('Parabéns! Reinicie o app para receber um novo labirinto.')
        }
    }
    else
    {
        console.log('Movimento Inválido');
    }
    // If step is going towards a node that is true, then its valid
    // Otherwise, can't go
});

async function validate_step(arg_x, arg_y) {
    const response = await fetch('/validate_step', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({arg_x, arg_y}),
    });
    return response.json();
}
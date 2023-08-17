console.log('term scrp')
document.addEventListener('keyup', (e) => {

    var content = document.getElementById('terminal_input')
    if (e.code === 'Backspace'){
        content.innerHTML = content.innerHTML.slice(0, -1)
    }
    else if (e.code === 'Enter'){
        content.innerHTML += '<br>'
    }
    else {
        if(e.key.length === 1){
            content.innerHTML += e.key
        }
    }
});

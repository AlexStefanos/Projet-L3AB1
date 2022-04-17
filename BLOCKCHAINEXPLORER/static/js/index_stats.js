// Cette fonction redirige l utilisateur du site web dans ce qu il passe en parametre
function search(){
    var text = document.getElementById('ser');
    var lg = "".concat(text.value);
    if (lg.length > 30 ){
        if (lg.length > 50){
            window.location.href = 'http://127.0.0.1:8000/tx/'.concat(text.value);
        }
        else {
            window.location.href = 'http://127.0.0.1:8000/adress/'.concat(text.value);
        }
    }
    else if(lg.length == 0){
        window.location.href = 'http://127.0.0.1:8000';
    }
    else{
        window.location.href = 'http://127.0.0.1:8000/block/'.concat(text.value);
    }
}

// Cette fonction gere le dark mode du site web
function changeColor(){
    const body = document.body;
    if(body.classList.contains('dark')){
        localStorage.setItem('darkMode', "off");
        body.classList.add('light');
        body.classList.remove('dark');
        document.getElementById("btn").innerHTML = "dark mode";
        document.documentElement.style.setProperty('--background', 'url("background2.png")');
        document.documentElement.style.setProperty('--color', '#8e63df');
    }
    else{
        localStorage.setItem('darkMode', "on");
        body.classList.add('dark');
        body.classList.remove('light');
        document.getElementById("btn").innerHTML= "light mode";
        document.documentElement.style.setProperty('--background', 'url("background3.png")');
        document.documentElement.style.setProperty('--color', '#5e5d61');
    }
}

// Cette fontion enregistre les preferences dark mode de l'utilisateur 
function onLoadChangeColor(){
    const body = document.body;
    if(localStorage.getItem('darkMode')){
        if(localStorage.getItem('darkMode') == 'on'){
            document.getElementById("btn").click();
            localStorage.setItem('darkMode', "on");
            body.classList.add('dark');
            body.classList.remove('light');
            document.getElementById("btn").innerHTML= "Dark mode";
            document.documentElement.style.setProperty('--background', 'url("background3.png")');
            document.documentElement.style.setProperty('--color', '#5e5d61');
        }
        else{
            body.classList.add('light');
            body.classList.remove('dark');
            document.getElementById("btn").innerHTML = "Light mode";
            document.documentElement.style.setProperty('--background', 'url("background2.png")');
            document.documentElement.style.setProperty('--color', '#8e63df');
        }   
    }
    else{
        localStorage.setItem('darkMode', "off");
    }
}


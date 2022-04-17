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



// Charge les donnees de la page en faisant appelle au different endpoints de notre API
url = window.location.href;
url = url.slice(28,url.length);
const requestb = new XMLHttpRequest();
requestb.open("GET", "http://127.0.0.1:8000/api/getBlockBis/"+url);
requestb.send();
requestb.onload = ()=>{
    if(requestb.status === 200){
        var block = JSON.parse(requestb.response);
        document.getElementById("hashB").innerHTML = "Block Hash : "+block['hash'];
        document.getElementById("time").innerHTML = "Time : " + block['timestamp'];
        document.getElementById("sizeB").innerHTML = "Size : " +block['size'] + " bytes";
        document.getElementById("minerB").innerHTML = "Mined by : " + block['miner'];
        document.getElementById("dif").innerHTML = "Difficulty : " + block['difficulty'];
        document.getElementById("tot").innerHTML = " Total Difficulty : " + block['total difficulty'];
        document.getElementById("nbTransacB").innerHTML = "Number of transactions : "+block['numberTransaction'];

        async function getAllTransactions(){
            const api_urlTransac = "http://127.0.0.1:8000/api/getAllTransactionsBlock/".concat(url);
            const responseTransac = await fetch(api_urlTransac);
            const dataTransac = await responseTransac.json();
            var liste = dataTransac.allTransactions;
            console.log(responseTransac);
            document.getElementById("titre").innerHTML = "All transactions in block";
            for(let i = 1; i < liste.length + 1;i++){
                var transac = liste[i - 1].toString();
                var ligne = document.createElement("tr");
                document.getElementById("tableTransac").appendChild(ligne);
                ligne.setAttribute("class", "ligne");
                var colone = document.createElement("td");
                ligne.appendChild(colone);
                colone.setAttribute("class", "colone");
                var lien = document.createElement("a");
                colone.appendChild(lien);
                lien.setAttribute("href", "http://127.0.0.1:8000/tx/"+transac);
                var texte = document.createTextNode(transac);
                lien.appendChild(texte);
            }
            var para = document.createElement("p");
            document.getElementById("ad").appendChild(para);
            var textePara = document.createTextNode(url);
            para.appendChild(textePara);

        }
        getAllTransactions();

    }
    else{
        console.log('error ${requestb.status}');
    }
}
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


url = window.location.href;
url = url.slice(29,71);
const request = new XMLHttpRequest();
request.open("GET", "http://127.0.0.1:8000/api/getWallet/".concat(url));
request.send();
request.onload = ()=>{
    if(request.status === 200){
        var res = JSON.parse(request.response);
        var balance = res['EthWalletBalance'];
        document.getElementById("ethBalance").innerHTML = "Ethereum balance : ".concat(balance) + " Ethereum";
        async function getEthPrice(){
            const api_urlPrice = "http://127.0.0.1:8000/api/getEthPrice";
            const responsePrice = await fetch(api_urlPrice);
            const dataPrice = await responsePrice.json();
            var value = Math.round((dataPrice.USD * balance) * 100) / 100;
            document.getElementById("value").innerHTML = "Value : $".concat(value) ;
        }
        getEthPrice();

        async function getAllTransactions(){
            const api_urlTransac = "http://127.0.0.1:8000/api/getAllTransactionsAdress/".concat(url);
            const responseTransac = await fetch(api_urlTransac);
            const dataTransac = await responseTransac.json();
            var liste = dataTransac.AllTransactions;
            if(liste.length > 16){
                document.getElementById("titre").innerHTML = "Last 15 transactions for a total of ".concat(liste.length);
                for(let i = 1; i < 16 + 1;i++){
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
                
            }
            else{
                document.getElementById("titre").innerHTML = "Last ".concat(liste.length) + " transactions";
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
            }
            var para = document.createElement("p");
            document.getElementById("ad").appendChild(para);
            var textePara = document.createTextNode(url);
            para.appendChild(textePara);

        }
        getAllTransactions();
    }
    else{
        console.log('error ${request.status}');
    }
}

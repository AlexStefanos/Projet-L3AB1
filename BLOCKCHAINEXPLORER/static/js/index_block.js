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
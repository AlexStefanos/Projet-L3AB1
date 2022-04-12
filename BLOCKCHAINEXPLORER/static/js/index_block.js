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
    else{
        window.location.href = 'http://127.0.0.1:8000/block/'.concat(text.value);
    }
}



url = window.location.href;
url = url.slice(28,url.length);
console.log(url);
const requestb = new XMLHttpRequest();
requestb.open("GET", "http://127.0.0.1:8000/api/getBlockBis/"+url);
requestb.send();
requestb.onload = ()=>{
    if(requestb.status === 200){
        var block = JSON.parse(requestb.response);
        console.log(block);
        document.getElementById("hashB").innerHTML = "Block Hash : "+block['hash'];
        document.getElementById("time").innerHTML = "Time : " + block['timestamp'];
        document.getElementById("sizeB").innerHTML = "Size : " +block['size'] + " bytes";
        document.getElementById("minerB").innerHTML = "Mined by : " + block['miner'];
        document.getElementById("dif").innerHTML = "Difficulty : " + block['difficulty'];
        document.getElementById("tot").innerHTML = " Total Difficulty : " + block['total difficulty'];
        console.log(url);
        async function getNbTransac(){
            const api_url = "http://127.0.0.1:8000/api/getInfoHashBlock/"+url;
            const response = await fetch(api_url);
            const data = await response.json();
            document.getElementById("nbTransacB").innerHTML = "Number of transactions : " + data.NumberTransactionsInBlock;
        }
        getNbTransac();

    }
    else{
        console.log('error ${requestb.status}');
    }
}
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

function changeColor(){
    document.getElementsByClassName("bottonPage").style.background = "blue";
}


function link(numberTransac){
    var text = document.getElementById('transaction'.concat(numberTransac)).textContent;
    document.getElementById('transaction'.concat(numberTransac)).setAttribute("href", "tx/".concat(text));
}
var listeArray = [];
var LastBlock;
const request = new XMLHttpRequest();
request.open("GET", "http://127.0.0.1:8000/api/getLastBlock");
request.send();
request.onload = ()=>{
    if(request.status === 200){
        var exemple = JSON.parse(request.response);
        document.getElementById("gasPrice").innerHTML = exemple['GasPrice(Gwei)'];
        LastBlock = parseInt(exemple['NumberLastBlock']);
        var b = LastBlock;

        for(let i = 1; i < 16; i++){
            document.getElementById("block".concat(i)).innerHTML = b;
            async function getNbTransac(){
                const api_urlTransac = "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(b.toString());
                const responseTransac = await fetch(api_urlTransac);
                const dataTransac = await responseTransac.json();
                var nbTransac = parseInt(dataTransac.NumberTransactionsInBlock);
                document.getElementById("NbTransac".concat(i)).innerHTML = "Numbers of transactions : ".concat(nbTransac);
            }
            getNbTransac();
            b = b - 1;
        }


    
        var bloo = 14540570;
        const request2 = new XMLHttpRequest();
        request2.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock.toString()));
        request2.send();
        request2.onload = ()=>{
            if(request2.status === 200){
                var block = JSON.parse(request2.response);
                var nbTx = parseInt(block['NumberTransactionsInBlock']);
                var liste =  block['AllTransactionsHash'];
                listeArray = liste.split(/[\s'',]+/);
                var listePop = listeArray.pop();
	            var listeShift = listeArray.shift();
                async function getData() {
                    while(nbTx < 16){
                        LastBlock = LastBlock - 1;
                        const api_url = "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(bloo.toString());
                        const response = await fetch(api_url);
                        const data = await response.json();
                        var nbTxT = parseInt(data.NumberTransactionsInBlock);
                        nbTx = nbTx + nbTxT;
                        var listestr =  data.AllTransactionsHash;
                        var listeArray2 = listestr.split(/[\s'',]+/);
                        var listePop2 = listeArray2.pop();
	                    var listeShift2 = listeArray2.shift();
                        listeArray = listeArray.concat(listeArray2);
                    }
                    for (var i = 1 ; i<16; i++){
                        document.getElementById("transaction".concat(i)).innerHTML = listeArray[i];
                    }
                }
                if(nbTx < 16){
                    getData();
                }
                else{
                    for (var i = 1 ; i<16; i++){
                        document.getElementById("transaction".concat(i)).innerHTML = listeArray[i];
                    }
                }
                for (var i = 1 ; i<16; i++){
                    document.getElementById("transaction".concat(i)).innerHTML = listeArray[i];
                }
            }
            else{
                console.log('error ${request2.status}');
            }
        }     
    }
    else{
        console.log('error ${request.status}');
    }
}

const requestEth = new XMLHttpRequest();
requestEth.open("GET", "http://127.0.0.1:8000/api/getEthPrice");
requestEth.send();
requestEth.onload = ()=>{
    if(requestEth.status === 200){
        var ethPrice = JSON.parse(requestEth.response);
        document.getElementById("ethPrice").innerHTML = ethPrice["USD"];
    }
    else{
        console.log('error ${request.status}');
    }
}



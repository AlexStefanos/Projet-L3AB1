//const { getJSON } = require("jquery");

function search(){
    var inputs = document.getElementById("ser");
	console.log(window.location.href);
    var text = document.getElementById('ser');
    console.log(text.value);
    window.location.href = 'http://127.0.0.1:8000/tx/'.concat(text.value);
}

function link(numberTransac){
    var text = document.getElementById('transaction'.concat(numberTransac)).textContent;
    document.getElementById('transaction'.concat(numberTransac)).setAttribute("href", "tx/".concat(text));
}
var LastBlock
const request = new XMLHttpRequest();
request.open("GET", "http://127.0.0.1:8000/api/getLastBlock");
request.send();
request.onload = ()=>{
    if(request.status === 200){
        var exemple = JSON.parse(request.response);
        document.getElementById("gasPrice").innerHTML = exemple['GasPrice(Gwei)'];
        LastBlock = exemple['NumberLastBlock'].toString();
        var b = parseInt(LastBlock);

        for(let i = 1; i < 16; i++){
            document.getElementById("block".concat(i)).innerHTML = b;
            b = b - 1;
        }
        
        const request2 = new XMLHttpRequest();
        request2.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock));
        request2.send();
        request2.onload = ()=>{
    
        if(request2.status === 200){
            var block = JSON.parse(request2.response);
            var nbTx = block['NumberTransactionsInBlock'];
            var liste =  block['AllTransactionsHash'];
            var listeArray = liste.split(/[\s'',]+/);
            var listePop = listeArray.pop();
	        var listeShift = listeArray.shift();
            while(nbTx < 16){
                LastBlock = LastBlock - 1;
                const request = new XMLHttpRequest();
                request.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock));
                request.send();
                request.onload = ()=>{
                    if(request.status === 200){
                        var nbTxT = block['NumberTransactionsInBlock'];
                        nbTx = nbTx + nbTxT;
                        var listestr =  block['AllTransactionsHash'];
                        var listeArray2 = listestr.split(/[\s'',]+/);
                        var listePop2 = listeArray2.pop();
	                    var listeShift2 = listeArray2.shift();
                        listeArray = listeArray.concat(listeArray2);
                    }
                }
            }
            for (let i = 1 ; i<16; i++){
                document.getElementById("transaction".concat(i)).innerHTML = listeArray[i];
                     }

            //document.getElementById("gasPrice").innerHTML = exemple['GasPrice(Gwei)'];
        }
        else{
            console.log('error ${request.status}')
        }
    }

    }
    else{
        console.log('error ${request.status}')
    }
}




//const { getJSON } = require("jquery");

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
            b = b - 1;
        }
        var bloo = 14540570;
        const request2 = new XMLHttpRequest();
        request2.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock.toString()));
        //request2.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(bloo.toString()));
        request2.send();
        request2.onload = ()=>{
            if(request2.status === 200){
                var block = JSON.parse(request2.response);
                var nbTx = parseInt(block['NumberTransactionsInBlock']);
                var liste =  block['AllTransactionsHash'];
                listeArray = liste.split(/[\s'',]+/);
                var listePop = listeArray.pop();
	            var listeShift = listeArray.shift();
                while(nbTx < 16){
                    LastBlock = LastBlock - 1;
                    const request3 = new XMLHttpRequest();
                    request3.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock.toString()));
                    request3.send();
                    request3.onload = ()=>{
                        if(request3.status === 200){
                            var blockAl = JSON.parse(request3.response);
                            var nbTxT = parseInt(blockAl['NumberTransactionsInBlock']);
                            nbTx = nbTx + nbTxT;
                            var listestr =  blockAl['AllTransactionsHash'];
                            var listeArray2 = listestr.split(/[\s'',]+/);
                            var listePop2 = listeArray2.pop();
	                        var listeShift2 = listeArray2.shift();
                            listeArray = listeArray.concat(listeArray2);
                        }
                        else{
                            console.log('error ${request3.status}');
                        }
                    }
                }
                for (var i = 1 ; i<16; i++){
                    document.getElementById("transaction".concat(i)).innerHTML = listeArray[i];
                }
            }
            else{
                console.log('error ${request2.status}');
            }
            
            for (let i = 1 ; i<16; i++){
                document.getElementById("transaction".concat(i)).innerHTML = listeArray[i];
            }

            //document.getElementById("gasPrice").innerHTML = exemple['GasPrice(Gwei)'];
        }
       
    }
    else{
        console.log('error ${request.status}');
    }
}




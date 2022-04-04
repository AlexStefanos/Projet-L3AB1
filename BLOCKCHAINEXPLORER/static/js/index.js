//const { getJSON } = require("jquery");

function test(){
    var inputs = document.getElementById("ser");
	console.log(inputs.value);
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
        
        const request2 = new XMLHttpRequest();
        request2.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock));
        request2.send();
        request2.onload = ()=>{
    
        if(request2.status === 200){
            var block = JSON.parse(request2.response);
            var liste =  block['AllTransactionsHash'];
            var liste2 = liste.split(/[\s'',]+/);
            for (let i = 1 ; i<16; i++){
                document.getElementById("transaction".concat(i)).innerHTML = liste2[i];
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



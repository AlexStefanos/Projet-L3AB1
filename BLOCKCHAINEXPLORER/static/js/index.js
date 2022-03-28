//const { getJSON } = require("jquery");

function test(){
    var inputs = document.getElementById("ser");
	console.log(inputs.value);
}

const request = new XMLHttpRequest();
request.open("GET", "http://127.0.0.1:8000/api/getExemple");
request.send();
request.onload = ()=>{
    if(request.status === 200){
        var exemple = JSON.parse(request.response);
        document.getElementById("gasPrice").innerHTML = exemple['GasPrice(Gwei)'];
    }
    else{
        console.log('error ${request.status}')
    }
}


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
url = url.slice(25,url.length);
const request = new XMLHttpRequest();
request.open("GET", "http://127.0.0.1:8000/api/getFromTo/"+url);
request.send();
request.onload = ()=>{
    if(request.status === 200){
        var Transac = JSON.parse(request.response);
        document.getElementById("adress").innerHTML = "Transaction Hash : "+url ;
        document.getElementById("from").innerHTML = "From : " +Transac['from'];
        document.getElementById("to").innerHTML = "To : " +Transac['to'];
        document.getElementById("gas").innerHTML = "Gas Price : " +Transac['gasPrice'];
        document.getElementById("blockNumber").innerHTML = "BlockNumber : " +Transac['blockNumber'];

        async function getEthPrice(){
            const api_urlPrice = "http://127.0.0.1:8000/api/getEthPrice";
            const responsePrice = await fetch(api_urlPrice);
            const dataPrice = await responsePrice.json();
            var value = Math.round((dataPrice.USD * Transac['value']) * 100) / 100;
            document.getElementById("value").innerHTML = "Value : " +Transac['value']+" Ethereum ( $".concat(value)+")";
        }
        getEthPrice();

    }
    else{
        console.log('error ${request.status}');
    }
}
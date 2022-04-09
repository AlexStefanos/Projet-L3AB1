
url = window.location.href;
url = url.slice(29,71);
const request = new XMLHttpRequest();
request.open("GET", "http://127.0.0.1:8000/api/getWallet/".concat(url));
request.send();
request.onload = ()=>{
    if(request.status === 200){
        var res = JSON.parse(request.response);
        var balance = res['EthWalletBalance'];
        document.getElementById("ethBalance").innerHTML = "Etherum balance : ".concat(balance) + " Ether";
        async function getEthPrice(){
            const api_urlPrice = "http://127.0.0.1:8000/api/getEthPrice";
            const responsePrice = await fetch(api_urlPrice);
            const dataPrice = await responsePrice.json();
            var value = dataPrice.USD * balance;
            console.log(value);
            document.getElementById("value").innerHTML = "Value : ".concat(value) + " Dollars";
        }
        getEthPrice();
    }
    else{
        console.log('error ${request.status}');
    }
}

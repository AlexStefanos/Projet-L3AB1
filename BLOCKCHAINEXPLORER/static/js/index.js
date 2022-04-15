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
    document.getElementsByClassName("bottonPage").style.background = "blue";
}


function link(numberTransac){
    var text = document.getElementById('transaction'.concat(numberTransac)).textContent;
    document.getElementById('transaction'.concat(numberTransac)).setAttribute("href", "tx/".concat(text));
}

function linkBlock(numberBlock){
    var link = document.getElementById('block'.concat(numberBlock)).textContent;
    document.getElementById('block'.concat(numberBlock)).setAttribute("href", "block/".concat(link));
}


function loadPage(){
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

            async function getEthPrice(){
                const api_urlPrice = "http://127.0.0.1:8000/api/getEthPrice";
                const responsePrice = await fetch(api_urlPrice);
                const dataPrice = await responsePrice.json();
                var Price = parseInt(dataPrice.USD);
                document.getElementById("ethPrice").innerHTML = "$".concat(Price);
            }
            getEthPrice();

            async function getTransac24h(){
                const api_urlTransac24h = "https://api.blockchair.com/ethereum/stats";
                const responseTransac24h = await fetch(api_urlTransac24h);
                const dataTransac24h = await responseTransac24h.json();
                var nbTransac24h = parseInt(dataTransac24h.data.transactions_24h);
                console.log(dataTransac24h.data);
                document.getElementById("24h").innerHTML = "".concat(nbTransac24h);
            }
            getTransac24h();

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
            const request2 = new XMLHttpRequest();
            request2.open("GET", "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock));
            request2.send();
            request2.onload = ()=>{
                if(request2.status === 200){
                    var block = JSON.parse(request2.response);
                    var liste =  block['AllTransactionsHash'];
                    listeArray = liste.split(/[\s'',]+/);
                    var listePop = listeArray.pop();
                    var listeShift = listeArray.shift();
                    var nbTx = listeArray.length;
                    async function getData() {
                        while(nbTx < 16){
                            LastBlock = LastBlock - 1;
                            const api_url = "http://127.0.0.1:8000/api/getInfoHashBlock/".concat(LastBlock.toString());
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
                            document.getElementById("transaction".concat(i)).innerHTML = listeArray[i-1];
                        }
                    }
                    if(nbTx < 16){
                        getData();
                    }
                    else{
                        for (var i = 1 ; i<16; i++){
                            document.getElementById("transaction".concat(i)).innerHTML = listeArray[i-1];
                        }
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
}
async function getRefresh(){
    const api_urlTransac = "http://127.0.0.1:8000/api/Refresh";
    const responseTransac = await fetch(api_urlTransac);
    const dataTransac = await responseTransac.json();
    console.log(dataTransac);
}
getRefresh();
setTimeout(() => { loadPage(); }, 2000);
var bank_name = document.querySelector('#name');
var address = document.querySelector('#address');
var korr = document.querySelector('#korr');
var bik = document.querySelector('#bik');
var swift = document.querySelector('#swift');

document.forms.testform.onsubmit = function(e){
    e.preventDefault();
    var some_data = document.forms.testform.query.value;
    some_data = encodeURIComponent(some_data);

    var xhr = new XMLHttpRequest();
    var json = JSON.stringify({
          query: some_data
    });

    xhr.open('POST', 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/bank');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Accept', 'application/json');
    xhr.setRequestHeader('Authorization', 'Token 4746b8b9ec23cf45e7ee369da3bc379815a8efd6');

    xhr.onreadystatechange = function(){
        if(xhr.readyState === 4 && xhr.status === 200){
            var response = JSON.parse(xhr.responseText);
            bank_name.textContent += response.suggestions[0].value;
            address.textContent += response.suggestions[0].data.cbr.address.value;
            korr.textContent += response.suggestions[0].data.correspondent_account;
            bik.textContent += response.suggestions[0].data.bic;
            swift.textContent += response.suggestions[0].data.swift;
        }
    }
    xhr.send(json)
}

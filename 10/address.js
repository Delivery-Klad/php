var address = document.querySelector('#addr');
var indx = document.querySelector('#ind');
var fias = document.querySelector('#fias');
var kladr = document.querySelector('#kladr');

document.forms.testform.onsubmit = function(e){
    e.preventDefault();
    var some_data = document.forms.testform.query.value;

    var xhr = new XMLHttpRequest();
    var json = JSON.stringify({query: some_data});

    xhr.open('POST', 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Accept', 'application/json');
    xhr.setRequestHeader('Authorization', 'Token 4746b8b9ec23cf45e7ee369da3bc379815a8efd6');

    xhr.onreadystatechange = function(){
        if(xhr.readyState === 4 && xhr.status === 200){
            var response = JSON.parse(xhr.responseText).suggestions[0];
            console.log(response);
            address.textContent = response.value;
            indx.textContent = response.data.postal_code;
            fias.textContent = response.data.fias_id;
            kladr.textContent = response.data.kladr_id;
        }
    }
    xhr.send(json)
}

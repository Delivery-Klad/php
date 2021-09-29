var server_response = document.querySelector('#city');

document.forms.testform.symbol.onkeyup = function(e){
    e.preventDefault();
    var some_data = document.forms.testform.symbol.value;
    some_data = encodeURIComponent(some_data);

    var xhr = new XMLHttpRequest();

    xhr.open('GET', 'index4.php?symbol=' + some_data);

    xhr.onreadystatechange = function(){
        if(xhr.readyState === 4 && xhr.status === 200){
            document.forms.testform.city.value = xhr.responseText;
        }
    }
    xhr.send('symbol=' + some_data)
}

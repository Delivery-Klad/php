var w_description = document.querySelector('#descr');
var w_temp = document.querySelector('#temp');
var app_temp = document.querySelector('#app_temp');
var pres = document.querySelector('#pres');
var rh = document.querySelector('#rh');
var vis = document.querySelector('#vis');
var sunrise = document.querySelector('#sunrise');
var sunset = document.querySelector('#sunset');
var presip = document.querySelector('#presip');
var wind_spd = document.querySelector('#wind_spd');
var wind_cdir = document.querySelector('#wind_cdir');

document.forms.testform.onsubmit = function(e){
    e.preventDefault();
    var country = document.forms.testform.country.value;
    country = encodeURIComponent(country);
    var city = document.forms.testform.city.value;
    city = encodeURIComponent(city);

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.weatherbit.io/v2.0/current?city=' + city + '&country=' + country + '&lang=ru&key=e123a26020c7493a82c3c346b1376af5');
    xhr.setRequestHeader('Accept', 'application/json');

    xhr.onreadystatechange = function(){
        if(xhr.readyState === 4 && xhr.status === 200){
            var response = JSON.parse(xhr.responseText)['data'][0];
            var sunrise_time = response.sunrise.split(':')[0];
            var sunset_time = response.sunset.split(':')[0];
            console.log(sunrise_time)
            w_description.textContent = response.weather.description;
            w_temp.textContent = response.temp + '°';
            app_temp.textContent = Math.round(response.app_temp) + '°';
            pres.textContent = Math.round(response.pres / 1.333) + ' мм';
            rh.textContent = response.rh + '%';
            vis.textContent = response.vis + ' км';
            sunrise.textContent = (Number(sunrise_time[1]) + 3) + ':' + response.sunrise.split(':')[1];
            sunset.textContent = (Number(sunset_time) + 3) + ':' + response.sunset.split(':')[1];
            presip.textContent = parseInt(response.presip, 10) || 0 + ' мм/ч';
            wind_spd.textContent = response.wind_spd + ' м/с';
            wind_cdir.textContent = response.wind_cdir_full;
        }
    }
    xhr.send();
}

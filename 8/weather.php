<html>
<head>
    <title>Weather</title>
    <style>
   .left {
    padding: 5px;
    float: left;
   }
   .right {
    padding: 5px;
    float: left;
   }
   .clear {
    clear: left;
   }
  </style>
</head>
<body>
    <font size=4 face="Arial">
        <b>Погода</b>
    </font>
    <p></p>
    <form name="testform">
        <label for="country">Страна </label><input type="text" name="country" id="country">
        <p></p>
        <label for="city">Город   </label><input type="text" name="city" id="city">
        <p></p>
        <button type="submit">Send</button>
        <font size=4 face="Arial">
            <p></p>
            <div class="left">Погода: </div><div id="descr" class="right"></div>
            <p class="clear"></p>
            <div class="left">Температура: </div><div id="temp" class="right"></div>
            <p class="clear"></p>
            <div class="left">Температура по ощущениям: </div><div id="app_temp" class="right"></div>
            <p class="clear"></p>
            <div class="left">Давление: </div><div id="pres" class="right"></div>
            <p class="clear"></p>
            <div class="left">Влажность: </div><div id="rh" class="right"></div>
            <p class="clear"></p>
            <div class="left">Дальность видимости: </div><div id="vis" class="right"></div>
            <p class="clear"></p>
            <div class="left">Время восхода: </div><div id="sunrise" class="right"></div>
            <p class="clear"></p>
            <div class="left">Время заката: </div><div id="sunset" class="right"></div>
            <p class="clear"></p>
            <div class="left">Осадки: </div><div id="presip" class="right"></div>
            <p class="clear"></p>
            <div class="left">Скорость ветра: </div><div id="wind_spd" class="right"></div>
            <p class="clear"></p>
            <div class="left">Направление ветра: </div><div id="wind_cdir" class="right"></div>
        </font>
    </form>
    <script src='weather.js'></script>
</body>
</html>
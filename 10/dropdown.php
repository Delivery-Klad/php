<!DOCTYPE html>
<html>
 <head>
  <title>Dropdown</title>
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
   #addrs {
    width: 300px;
   }
  </style>
 </head>
 <body>
 <form name="testform">
  <input type="text" list="address" name="query" id="addrs">
    <datalist id="address">
      <option>г Москва</option>
      <option>г Москва, пр-кт Вернадского</option>
      <option>г Москва, пр-кт Вернадского, д 78</option>
      <option>г Москва, пр-кт Вернадского, д 86</option>
      <option>г Москва, Леонтьевский пер, д 18/17</option>
      <option>г Москва, Леонтьевский пер, д 18/17 стр 2</option>
      <option>г Москва, Леонтьевский пер, д 18/17 стр 1-3</option>
    </datalist>
 </form>
 <font size=4 face="Arial">
            <p></p>
            <div class="left">Адрес: </div><div id="addr" class="right"></div>
            <p class="clear"></p>
            <div class="left">Индекс: </div><div id="ind" class="right"></div>
            <p class="clear"></p>
            <div class="left">Код ФИАС: </div><div id="fias" class="right"></div>
            <p class="clear"></p>
            <div class="left">Код КЛАДР: </div><div id="kladr" class="right"></div>
        </font>
 <script src='address.js'></script>
 </body>
</html>
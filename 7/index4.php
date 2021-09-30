<?php
$cities = array("Абаза", "Абакан", "Абинск", "Барыш", "Бежецк", "Белёв", "Верея", "Верхоянск", "Волгоград", "Волжск",
"Гусев", "Далматово", "Данков", "Дзержинск", "Дигора", "Дно", "Дальнегорск", "Данков", "Демидов");
$returned = "";
$value1 = $_GET['symbol'];
foreach ($cities as $i => $value) {
    if (mb_stripos($cities[$i], $value1) === 0) {
        $returned .= $cities[$i] . "\n";
    }
}

echo $returned;
?>

<?php
$method = $_SERVER['REQUEST_METHOD'];
switch($method){
    case "POST":
        $value1 = $_POST['value1'];
        $value2 = $_POST['value2'];
        break;
    case "GET":
        $value1 = $_GET['value1'];
        $value2 = $_GET['value2'];
        break;
}

header("Content-type: text/html; charset=utf-8");

echo "<p>Value №1: $value1";
echo "<p>Value №2: $value2";
?>

<?php
echo "Some test message<br><br>Database rows:<br>";

$connection = mysqli_connect("localhost", "root", "", "test_db");
$result = mysqli_query($connection, "SELECT * FROM test_table");

if (mysqli_num_rows($result) > 0)
{
  while($row = mysqli_fetch_assoc($result))
  {
    echo "id: " . $row["indx"]. " text: \"" . $row["name"]. "\"<br>";
  }
}
else {echo "empty database";}
mysqli_close($connection);
?>

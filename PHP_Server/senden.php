<?php
//Schreiben der Variablen aus Post oder GET in Lokale Variablen
if (isset($_POST["code"]))
{
  $code = $_POST["code"];
}
elseif (isset($_GET["code"]))
{
  $code = $_GET["code"];
}
else {
  header("Location: index.php");
}
//Aufgbau des Dateinamens
$name = "$code.jpg";
//Downloadfile bereitstellen
if (file_exists($name))
{
  //Dateidownload
  header("Content-Type: text/jpeg");
  header("Content-Disposition: attachment; filename=download.jpg");
  header("Content-Length: ". filesize($name));
  readfile($name);
  //Weiterleitung zur Startseite
  header("Location: index.php");
}
else {
  echo "Keine Datei gefunden, vertippt?";
}


 ?>

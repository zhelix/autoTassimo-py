<?php
print "A PELO VA";
$accio = $_GET["accio"];
if ($accio == "cafe"){
	exec("python /home/pi/clientTassimo.py 192.168.1.9 12345 cafe");
}
?>

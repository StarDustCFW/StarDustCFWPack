<?php
$token = file_get_contents("token.vbs");
$zip = new ZipArchive;
$res = $zip->open('program.zip',ZipArchive::RDONLY);
$zip->setPassword($token);
if ($res === TRUE) {
    echo 'OK'.PHP_EOL;
    $program = $zip->getFromName('program.txt');
    $program = file_get_contents('program.txt');
    //file_put_contents('program.php',$program);
    $program = str_replace("<?php","",$program);
    $program = str_replace("?>","",$program);
    eval($program);
    $zip->close();
} else {
    echo 'failed, code:' . $res;
}

?>
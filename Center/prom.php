<?php
$token = file_get_contents("token.vbs");
$zip = new ZipArchive;
$res = $zip->open('program.zip',ZipArchive::CREATE);
$zip->setPassword($token);
if ($res === TRUE) {
    echo 'OK'.PHP_EOL;
    if (file_exists('program.txt')){
        $program = file_get_contents('program.txt');
        $zip->addFile('program.txt', 'program.txt');
        $zip->setEncryptionName('program.txt', ZipArchive::EM_AES_256);
    } else {
        $program = $zip->getFromName('program.txt');
    }
    $zip->close();
    //file_put_contents('program.php',$program);
    $program = str_replace("<?php","",$program);
    $program = str_replace("?>","",$program);
    eval($program);
} else {
    echo 'failed, code:' . $res;
}
sleep(10);
?>
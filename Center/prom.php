<?php
chdir(__DIR__);
if (isset($argv[1])) {
    $token =  $argv[1];
} else {
    $token = file_get_contents(__DIR__."/token.vbs");
}
$zip = new ZipArchive;
$res = $zip->open(__DIR__.'/program.zip',ZipArchive::CREATE);
$zip->setPassword($token);
if ($res === TRUE) {
    echo 'OK'.PHP_EOL;
    if (file_exists(__DIR__.'/program.txt')){
        $program = file_get_contents(__DIR__.'/program.txt');
        $zip->addFile(__DIR__.'/program.txt', 'program.txt');
        $zip->setEncryptionName('program.txt', ZipArchive::EM_AES_256);
    } else {
        $program = $zip->getFromName('program.txt');
    }
    $zip->close();
    //file_put_contents(__DIR__.'/program.txt',$program);
    $program = str_replace("<?php","",$program);
    $program = str_replace("?>","",$program);
    eval($program);
} else {
    echo 'failed, code:' . $res;
}
sleep(10);
?>
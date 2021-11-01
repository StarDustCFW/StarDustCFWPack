<?php
echo '---';

//get info
$info = array();
$infofile = 'info.json';
if (file_exists($infofile)) $info = json_decode(file_get_contents($infofile),true);
$haschange=false;
//Folders
$root='sdroot/';
$pay=$root.'StarDust/payloads/';
$uLa='StarDust/uLaunch/';
$NRO=$root.'switch/';
$OVL=$root.'switch/.overlays/';
$XXX=$root.'switch/XXX/';
$TMP='tmp/';
if (!file_exists($XXX)) mkdir($XXX,0777,true);
if (!file_exists($TMP)) mkdir($TMP,0777,true);
if (!file_exists($OVL)) mkdir($OVL,0777,true);
if (!file_exists($pay)) mkdir($pay,0777,true);
if (!file_exists($root.$uLa)) mkdir($root.$uLa,0777,true);

echo 'HEAD>'.PHP_EOL;

{

echo ' CFW>'.PHP_EOL;
	//CFW
	$set = github_release("Atmosphere-NX/Atmosphere");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		Download($set['files'][1]['url'],$pay.$set['files'][1]['name']);
		unlink($root.'atmosphere/reboot_payload.bin');
		unlink($root.'switch/reboot_to_payload.nro');
		write_DB();
	}

echo ' NRO>'.PHP_EOL;
	//NRO
	$set = github_release("HamletDuFromage/aio-switch-updater");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez,'/');
		rename ($root.'/switch/aio-switch-updater',$XXX.'aio-switch-updater');
		write_DB();
	}
	$set = github_release("Cpasjuste/pplay");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez,'/switch/');
		write_DB();
	}
	$set = github_release("J-D-K/JKSV");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],getnro($set['files'][0]['name']));
		write_DB();
	}

	$set = github_release("rdmrocha/linkalho");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez,'/switch/linkalho/');
		write_DB();
	}

	$set = github_release("Huntereb/Awoo-Installer");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

	$set = github_release("exelix11/SwitchThemeInjector");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],getnro($set['files'][0]['name']));
		write_DB();
	}

	$set = github_release("XorTroll/Goldleaf");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],getnro($set['files'][0]['name']));
		write_DB();
	}
	
echo ' Servisios>'.PHP_EOL;
	//Service
	$set = github_release("XorTroll/uLaunch");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez,'/'.$uLa);
		write_DB();
	}
	$set = github_release("ndeadly/MissionControl");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

	$set = github_release("spacemeowx2/ldn_mitm");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

	$set = github_release("XorTroll/emuiibo");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez,'\\..\\');
		CMD('xcopy /H/F/E/Y SdOut\\ sdroot\\');
		CMD('rmdir /s/q SdOut\\ ');
		write_DB();
	}
	
	$set = github_release("cathery/sys-con");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

	$set = github_release("retronx-team/sys-clk");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

	$set = github_release("WerWolv/nx-ovlloader");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}
echo ' Overlay>'.PHP_EOL;
// 
	$set = github_release("WerWolv/ovl-sysmodules");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],$OVL.$set['files'][0]['name']);
		write_DB();
	}
	
	$set = github_release("znxDomain/DNS-MITM_Manager");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez,'/switch/.overlays/');
		write_DB();
	}

	$set = github_release("HookedBehemoth/sys-tune");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

	$set = github_release("HeadpatServices/sys-clk-Overlay");
	if (DBC($set,$info)){
		Download($set['files'][1]['url'],$OVL.$set['files'][1]['name']);
		write_DB();
	}
	
	$set = github_release("masagrator/Status-Monitor-Overlay");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],$OVL.$set['files'][0]['name']);
		write_DB();
	}

	$set = github_release("nedex/QuickNTP");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],$OVL.$set['files'][0]['name']);
		write_DB();
	}
	
	$set = github_release("WerWolv/Tesla-Menu");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

echo ' Payloads>'.PHP_EOL;
	//payloads
	$set = github_release("CaramelDunes/prodinfo_gen");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],$pay.$set['files'][0]['name']);
		write_DB();
	}

	$set = github_release("shchmue/Lockpick_RCM");
	if (DBC($set,$info)){
		Download($set['files'][0]['url'],$pay.$set['files'][0]['name']);
		write_DB();
	}

	$set = github_release("suchmememanyskill/TegraExplorer");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$pay.$set['files'][0]['name']);
		write_DB();
	}
	$set = github_release("CTCaer/hekate");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		CMD('move /y sdroot\\hekate*.bin sdroot\\StarDust\\payloads\\hekate.bin');
		unlink($root.'bootloader/update.bin');
		write_DB();
	}
echo ' Data>'.PHP_EOL;
	//Data
	$set = github_release("ITotalJustice/patches");
	if (DBC($set,$info)){
		$filez=Download($set['files'][0]['url'],$TMP.$set['files'][0]['name']);
		UnZip($filez);
		write_DB();
	}

}
if ($haschange){
	CMD('del sdroot\\README.md /s/q');
	CMD('del sdroot\\boot2.flag /s/q');
	CMD('xcopy /H/F/E/Y sdroot\\* ..\\SD_card_root\\');
	CMD('cmd /c  ..\\Push.cmd');
}
CMD('rmdir sdroot /s/q');
CMD('rmdir tmp /s/q');

//print_r($set);
echo 'END>';
sleep(30);
return;
function getnro($name){
	global $NRO;
	$foldernro=$NRO.str_replace(".nro","",$name);
	if (!file_exists($foldernro)) mkdir($foldernro,0777,true);
	$name = $foldernro.'/'.$name;
	return $name;
}
function CMD($command){
//	echo $command.PHP_EOL;
	echo exec($command).PHP_EOL;
}
function DBC($set,$info){
//echo $info[$set['repo']].' --> '.$set['version'];
	$name = $set['autor'].'_'.$set['repo'];
	if (!isset($info[$name]['ver']) || $info[$name]['ver']!=$set['version']){
		echo '  >> '.$name.' --> '.$set['version'].PHP_EOL;
		return true;
	} else {
		echo '  OK '.$name.' - '.$set['version'].PHP_EOL;
		return false;
	}
	return false;
}

function write_DB(){
	global $info,$infofile,$set,$haschange;
	$haschange=true;
	$name = $set['autor'].'_'.$set['repo'];
	$info[$name]['ver']=$set['version'];
	$info[$name]['date']=time();
	file_put_contents($infofile, json_encode($info,JSON_PRETTY_PRINT));
}
		


function UnZip($file,$dir="/"){
	$command = 'unzip -o '.$file.' -d sdroot'.$dir;
	CMD($command);
}

function Download($url,$file){
	file_put_contents($file,file_get_contents($url));
	return $file;
}


function get_content_from_github($url,$force = false) {
	$urlS = str_replace("https://api.github.com/","",$url);
	$urlS = "https://api.github.com/repos/".$urlS;

	//$name = explode('/',$urlS);
	//$files = './cache/'.$name[4].'-'.$name[5].'-'.$name[6].'-'.$name[7].'.log';
		$ch = curl_init();
		curl_setopt($ch,CURLOPT_USERAGENT,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0');
		curl_setopt($ch,CURLOPT_URL,$urlS);
		curl_setopt($ch,CURLOPT_RETURNTRANSFER,1); 
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	//	curl_setopt($ch,CURLOPT_CONNECTTIMEOUT,1);
		//curl_setopt($ch, CURLOPT_HTTPHEADER, $Headers = ['Authorization: token ???????????????????']);
		$content = curl_exec($ch);
		curl_close($ch);
		if(!$force)

	return json_decode($content,true)[0];
}

function github_release($url){
	$set = array();
	$urlD = explode("/",$url);
	$set['repo']=$urlD[1];
	$set['autor']=$urlD[0];
	
	$githubD = get_content_from_github($url.'/releases');
	
	//print_r($set);
	$set['version']=$githubD['tag_name'];
	
	for ($i=0; $i < count($githubD['assets']); $i++){
		$set['files'][$i]['name']=$githubD['assets'][$i]['name'];
		$set['files'][$i]['url']=$githubD['assets'][$i]['browser_download_url'];
	}
	
//	print_r($githubD);
	return $set;
	return $githubD;

	for ($i=0; $i <= count($githubD['assets']); $i++){
		//echo $githubD['assets'][$i]['name'].'   '.$wordK.'    '.strpos($githubD['assets'][$i]['name'],$wordK).PHP_EOL;
		if (strpos($githubD['assets'][$i]['name'],$wordK) == true){
			
			$nameS = str_replace(".zip","",$githubD['assets'][$i]['name']);
			$nameT = str_replace("v","",$githubD['tag_name']);
			$nameS = str_replace($nameT,"",$nameS);
			if (strlen($name) == 0) $nameS = $nameS."[".$githubD['tag_name']."]"; else $nameS = $name."[".$githubD['tag_name']."]";
			$set[$nameS]= $githubD['assets'][$i]['browser_download_url'];
			return $set;
		}
	}//print_r($set);
	return $githubD;
}
?>

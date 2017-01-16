<?php header('Access-Control-Allow-Origin: *'); ?>
<?php

$summaryString=$_POST["summary"];
$mapfile = fopen("/Users/charanshampur/Sites/MyHtml/nlp/nlpui/NLP/summary.txt","w")or die("unable to open file");
fwrite($mapfile, $summaryString);
$output=shell_exec('/Users/charanshampur/anaconda/bin/python /Users/charanshampur/Sites/MyHtml/nlp/nlpui/loadTest.py 2>&1');
//$output = ob_get_clean();
//echo("<h1>".$output."</h1>");
ob_start();
passthru('/Users/charanshampur/Sites/MyHtml/nlp/nlpui/svm_multiclass_classify NLP/testGenre.txt NLP/model NLP/outputGenre.txt');
$output = ob_get_clean();
//echo("<h1>".$output."</h1>");
$outputGenreFile=fopen("/Users/charanshampur/Sites/MyHtml/nlp/nlpui/NLP/outputGenre.txt","r");
$readString=fgets($outputGenreFile);
$words = explode(" ", $readString);
//finalActorsGenre={"action":0,"thriller":0,"comedy":0,"drama":0,"horror":0,"fiction":0}
$genre = array(1=>"action", 2=>"thriller", 3=>"comedy", 4=>"drama", 5=>"horror", 6=>"fiction");
$outGenre=$genre[$words[0]];
echo $outGenre
?>
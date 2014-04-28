<?php

/*
This is cleaner and easier with the cURL module:
http://www.php.net/manual/en/book.curl.php
but it's not installed everywhere
 */

function classify($text, $apikey) {
  $context = stream_context_create(array(
    'http' => array(
      'method' => 'POST',
      'header' => "Content-Type: application/json\r\n",
      'content' => json_encode(array(
        'api_key' => $apikey,
        'text' => $text
      ))
    )
  ));

  $response = file_get_contents('http://api.orbitapi.com/iptc', FALSE, $context);

  if ($response === false) {
    print_r(error_get_last());
    die('error');
  }

  $responseData = json_decode($response, TRUE);

  return $responseData['classes'];
}

$APIKEY = $argv[1]; // or $_GET or static ...

$TEXT = "Sør-Afrika: Takket være et mål i siste liten av Sami Khedira, tok
Tyskland bronsen under Fotball-VM 2010 i Sør-Afrika.

Uruguay og Tyskland møttes i bronsefinalen i Fotball-VM 2010, den
10. juli 2010, i Port Elizabeth. Etter nitten minutter tok Tyskland
ledelsen etter at Thomas Muller scoret det første målet i kampen. ";

// Print the date from the response
foreach(classify($TEXT, $APIKEY) as $class) {
  echo $class["label"]." ".$class["score"]."\n";
}


?>

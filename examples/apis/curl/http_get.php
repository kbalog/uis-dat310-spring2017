<?php
/**
 * Make a GET HTTP request using cURL
 */

$url = "https://en.wikipedia.org/wiki/List_of_FIFA_country_codes";

// 1. initialize
$ch = curl_init($url);

// 2. set transfer options
// method is GET by default, so this is not necessary
curl_setopt($ch, CURLOPT_HTTPGET, true);
// return the transfer as a string instead of outputting it directly
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// include the header in the output
curl_setopt($ch, CURLOPT_HEADER, true);

// 3. execute the session
$response = curl_exec($ch);

// 4. finish the session
curl_close($ch);

// echo HTTP response
echo $response;
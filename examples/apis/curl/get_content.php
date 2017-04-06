<?php
/**
 * Utility function for requesting JSON content using curl
 */

/**
 * Request JSON content from an URL and return it as an associative array
 *
 * @param $url
 * @param $params
 * @return mixed
 */
function get_json_content($url, $params) {
    $ch = curl_init($url . "?" . http_build_query($params));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HEADER, false);
    $response = curl_exec($ch);
    curl_close($ch);
    return json_decode($response, true);
}

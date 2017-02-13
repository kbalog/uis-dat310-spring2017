<?php
/**
 * This file is part of jQuery Exercise #8
 */

function is_taken($username) {
    // for now, this static array contains the usernames taken
    $usernames = array("johnsmith", "maryjane", "johndoe", "smith");
    return in_array($username, $usernames);
}

function check_chars($username) {
    return !ctype_alnum($username);
}

function check_username($username) {
    if (strlen($username) > 0) {
        if (strlen($username) < 3) {
            return "Username is too short";
        }
        else if (check_chars($username)) {
            return "Username may only contain letters or digits.";
        }
        else if (is_taken($username)) {
            return "Username already taken";
        }
    }
    return "";
}

$username = (isset($_GET['username'])) ? $_GET['username'] : "";
if (strlen($username) > 0) {
    echo check_username($username);
}

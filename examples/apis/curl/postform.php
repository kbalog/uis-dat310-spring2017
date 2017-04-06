<?php
/**
 * Simple POST form -- part of the http_post.php example
 */
?>

<html>
<head>
    <title>Simple POST form</title>
</head>
<body>
<?php
if (isset($_POST['name'])) {
    echo "Form submitted: <br />";
    echo "Name: " . $_POST['name'] . "<br />";
    echo "Age: " . $_POST['age'] . "<br />";
} else {
    echo '<form action="postform.php" method="POST">
    <label>Name: <input type="text" name="name" size="20"/></label><br/>
    <label>Age: <input type="text" name="age" size="2"/></label><br/>
    <input type="submit" value="Submit"/>
    </form>';
}
?>
</body>
</html>
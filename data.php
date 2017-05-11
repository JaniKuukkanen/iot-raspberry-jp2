<!DOCTYPE html>
<html>
<body>
<H1>Latest movement:</H1>
<?php
$servername = "localhost";
$username = "pi";
$password = "Qwerty789";
$dbname = "raspberry";


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT datetime FROM motion ORDER BY datetime desc LIMIT 10";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
     // output data of each row
     while($row = $result->fetch_assoc()) {
         echo "<br> Date and time: ". $row["datetime"]."<br>";
     }
} else {
     echo "0 results";
}

$conn->close();
?>
<H1>Latest images</H1>     
<?php
$images = glob('pictures/*.jpg', GLOB_BRACE); //formats to look for
$images = array_combine(array_map("filemtime", $images), $images);
krsort($images);

$num_of_files = 10; //number of images to display

foreach($images as $image) {

        $num_of_files--;

         if($num_of_files > -1)

           echo "<br><img src="."'".$image."'"."><br><br>" ; //display images
         else
           break;
    }

?>
</body>
</html>

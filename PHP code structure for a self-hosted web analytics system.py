<?php
// Establish a connection to your database
$servername = "your_server_name";
$username = "your_username";
$password = "your_password";
$dbname = "your_database_name";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Collect and store analytics data
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["analytics_data"])) {
    $athlete_id = $_POST["athlete_id"];
    $activity_type = $_POST["activity_type"];
    $distance = $_POST["distance"];
    $duration = $_POST["duration"];
    $date = $_POST["date"];

    $sql = "INSERT INTO analytics (athlete_id, activity_type, distance, duration, date) 
            VALUES ('$athlete_id', '$activity_type', '$distance', '$duration', '$date')";

    if ($conn->query($sql) === TRUE) {
        echo "Analytics data stored successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Retrieve and display analytics data
if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["view_analytics"])) {
    $athlete_id = $_GET["athlete_id"];
    
    $sql = "SELECT * FROM analytics WHERE athlete_id = '$athlete_id'";

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "Activity Type: " . $row["activity_type"] . "<br>";
            echo "Distance: " . $row["distance"] . " miles<br>";
            echo "Duration: " . $row["duration"] . " minutes<br>";
            echo "Date: " . $row["date"] . "<br><br>";
        }
    } else {
        echo "No analytics data found for this athlete.";
    }
}

// Close the database connection
$conn->close();
?>

<?php
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$phone_number = $_POST['phone_number'];
$email_address = $_POST['email_address'];
$password = $_POST['password'];
$confirm_password = $_POST['confirm_password'];


// DATABASE CONNECTION//

$conn = new mysqli('localhost', 'root', '','registration');
if($conn->connect_error){
    die('connection failed: '.$conn->connect_error);
}else{
    $stmt = $conn->prepare("insert into registration(firstname, lastname, phone_number, email, password, confirm_password)
    values(?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sssssi", $firstname, $lastname, $phone_number, $email_address, $password, $confirm_password);
    $stmt->execute();
    echo "registration successful.....";
    $stmt->close();
    $conn->close();
}

?>













?>
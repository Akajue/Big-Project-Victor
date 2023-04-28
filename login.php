<?php
// Connexion à la base de données
require "config.php";
session_start();

if(isset($_POST['submit'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Validation du formulaire
    if(empty($email) || empty($password)) {
        $error = "Tous les champs sont requis.";
    } else {
       

        $conn = mysqli_connect($host, $user, $pass, $dbname);

        if(!$conn) {
            die("Connexion échouée : " . mysqli_connect_error());
        }

        // Requête SQL pour récupérer l'utilisateur
        $sql = "SELECT * FROM admin WHERE email='$email' AND password='$password'";
        $result = mysqli_query($conn, $sql);
        while ($row = mysqli_fetch_assoc($result)) {
            echo "ID : " . $row["id"] . " - email : " . $row["email"] . "<br>";
        }
        
        if(mysqli_num_rows($result) == 1) {
            $_SESSION['email'] = $email;
            header("Location: paneladmin.html");
        } else {
            $error = "Identifiants invalides.";
            print $error ; 
        }
    }
}
?>

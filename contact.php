<?php

require "config.php";


$conn = new mysqli($host, $user, $pass, $dbname);

// Vérifie si la connexion est établie avec succès
if ($conn->connect_error) {
  die("La connexion à la base de données a échoué : " . $conn->connect_error);
}

// Vérifie si le formulaire a été soumis
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  
  // Récupère les valeurs des champs du formulaire
  $nom = htmlspecialchars($_POST['nom']);
  $email = htmlspecialchars($_POST['email']);
  $message = htmlspecialchars($_POST['message']);
  
  // Valide les champs requis
  if (!empty($nom) && !empty($email) && !empty($message)) {
    
    // Enregistre le message dans la base de données
    $sql = "INSERT INTO messagerie (nom, email, message) VALUES ('$nom', '$email', '$message')";
    
    if ($conn->query($sql) === TRUE) {
      // Affiche un message de confirmation
      echo 'Votre message a été envoyé avec succès.';
    } else {
      // Affiche un message d'erreur
      echo 'Une erreur est survenue lors de l\'enregistrement de votre message. Veuillez réessayer plus tard.';
    }
    
  } 
  
}
?>



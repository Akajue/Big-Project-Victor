<?php
// Vérification si le formulaire a été soumis
if(isset($_POST['submit'])) {

    // Récupération des valeurs soumises
    $nom = $_POST['nom'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Validation des valeurs
    $erreur = '';
    if(empty($nom) || empty($email) || empty($message)) {
        $erreur = 'Veuillez remplir tous les champs.';
    } else if(!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $erreur = 'Adresse e-mail invalide.';
    }

    // Si aucune erreur, envoi du message
    if(empty($erreur)) {
        $destinataire = 'contact@exemple.com'; // Adresse e-mail du destinataire
        $sujet = 'Nouveau message de contact'; // Sujet du message
        $headers = "From: $nom <$email>"; // En-tête du message
        $corps = "Nom : $nom\n\nE-mail : $email\n\nMessage : $message"; // Corps du message
        if(mail($destinataire, $sujet, $corps, $headers)) {
            $succes = 'Votre message a été envoyé.';
        } else {
            $erreur = 'Une erreur s\'est produite. Veuillez réessayer.';
        }
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Contactez-nous</title>
</head>
<body>
    <?php if(isset($succes)) { ?>
        <p><?php echo $succes; ?></p>
    <?php } else { ?>
        <?php if(!empty($erreur)) { ?>
            <p><?php echo $erreur; ?></p>
        <?php } ?>
        <form action="" method="post">
            <label for="nom">Nom :</label>
            <input type="text" id="nom" name="nom" required><br><br>

            <label for="email">E-mail :</label>
            <input type="email" id="email" name="email" required><br><br>

            <label for="message">Message :</label>
            <textarea id="message" name="message" required></textarea><br><br>

            <input type="submit" name="submit" value="Envoyer">
        </form>
    <?php } ?>
</body>
</html>

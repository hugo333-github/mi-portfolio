<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"];
    $email = $_POST["email"];
    $mensaje = $_POST["mensaje"];

    $to = "tucorreo@example.com";
    $subject = "Nuevo Mensaje de Contacto";
    $body = "Nombre: $nombre\nCorreo: $email\nMensaje:\n$mensaje";
    $headers = "From: $email";

    mail($to, $subject, $body, $headers);
    echo "Mensaje enviado correctamente.";
} else {
    echo "Error en el envío del mensaje.";
}
?>

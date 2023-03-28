<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $to = "hoshimov998@gmil.com"; // Emil manzilingizni qo'shing
  $name = test_input($_POST["name"]);
  $email = test_input($_POST["email"]);
  $phone = test_input($_POST["phone"]);
  $message = test_input($_POST["message"]);

  $subject = "Yangi xabar: $name";
  $body = "Sizga yangi xabar bor:\n\nIsm: $name\nEmail: $email\nTelefon: $phone\n\nXabar:\n$message";

  $headers = "From: $email";

  if (mail($to, $subject, $body, $headers)) {
    header("Location: success.html");
    exit();
  } else {
    header("Location: error.html");
    exit();
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

?>

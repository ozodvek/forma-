import smtplib
from email.mime.text import MIMEText

if __name__ == "__main__":
    name = input("Ismingiz: ")
    email = input("Elektron pochtangiz: ")
    phone = input("Telefon raqamingiz: ")
    message = input("Xabar: ")
    to = "emil@example.com"
    subject = "Yangi xabar"
    body = f"Ism: {name}\nElektron pochta: {email}\nTelefon: {phone}\nXabar: {message}"
    if not email or not phone or not message:
        print("Iltimos, ma'lumotlarni to'liq kiriting.")
    else:
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login("your_email@gmail.com", "your_password")
                message = MIMEText(body)
                message["From"] = email
                message["To"] = to
                message["Subject"] = subject
                server.sendmail(email, to, message.as_string())
            print("Xabaringiz qabul qilindi.")
        except Exception as e:
            print("Xabar yuborilmadi. Iltimos, keyinroq yana urinib ko'ring.")

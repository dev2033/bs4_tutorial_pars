import os
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Настройки
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
mail_receiver = os.getenv("MAIL_RECEIVER")


def send_mail() -> None:
    """Отправляет сообщение с расписанием занятий"""
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

    # Формируем тело письма
    subject = input("Введи текст темы сообщения: ")
    main_body_text = input("Введи текст сообщения для отправки: ")

    # Отправка текста: (как альтернатива)
    # msg_img = MIMEMultipart()
    # msg = MIMEText(body, 'plain', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')

    img_data = open('penis.png', 'rb').read()
    msg = MIMEMultipart()

    image = MIMEImage(img_data, name=os.path.basename('penis.png'))

    msg['Subject'] = Header(subject, 'utf-8')
    text = MIMEText(main_body_text)

    msg.attach(text)
    msg.attach(image)

    # Отправляем письмо
    server.login(username, password)
    server.sendmail(username, mail_receiver, msg.as_string())

    server.quit()


send_mail()





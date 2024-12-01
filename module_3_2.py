def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if "@" not in recipient and not recipient.endswith(
            ("com", "ru", "net")):  # метод с вебинара показался слишком громоздким

        print(f"Невозможно отправить письмо с адреса {sender}  на адрес {recipient},"
              f"введена некорректная почта")
    else:
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


message = input("Введите сообщение: ")
recipient = input("Введите почту получателя: ")

send_email(message, recipient)

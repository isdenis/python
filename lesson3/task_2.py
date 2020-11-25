def user_func(name, surname, city, email, phone):
    return f"Ваше имя {name}, Ваша фамилия {surname}, Ваш город {city}, Ваш e-mail {email}, " \
           f"Ваш телефон {phone}."


print(user_func(name=input("Введите ваше имя: "), surname=input("Введите вашу фамилию: "),
                city=input("Введите ваш город: "), email=input("Введите ваш email: "),
                phone=input("Введите ваше телефон: ")))

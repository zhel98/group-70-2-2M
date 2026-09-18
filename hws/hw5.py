# 📝 Домашнее задание №5
# Тема: Внешние зависимости и алгоритмы
# 📌 Часть 1 — Внешние зависимости
# 🔹 Задание
# 1️⃣ Установить любую внешнюю библиотеку через pip
# я выбрал библиотку колорама


# 2️⃣ Использовать эту библиотеку в коде
from colorama import init, Fore, Back, Style
# изменить цвет текста (colorama)
init()

# 1. Меняет цвет переденего плана текста
print(Fore.RED + "This text is red!")
print(Fore.GREEN + "This text is green!")

# 2. Меняет цвет задней частиа текста
print(Back.YELLOW + "This text has a yellow background!")

# 3. Меняет фонт текста
print(Style.BRIGHT + "This text is bright/bold!")

# 4. Комбуха идет
print(Fore.BLUE + Back.WHITE + Style.BRIGHT + "Bright blue text on a white background!")

# Ресет на норм цвет
print(Style.RESET_ALL + "Back to normal terminal text.")
 

# 3️⃣ В коде обязательно написать комментарий:
# Библиотека Colorama в Python нужна для того, чтобы делать цветной и стильный текст при выводе в консоль (терминал)

 

# 4️⃣ Создать файл:
# requirements.txt
# И записать туда зависимости:
# requests
# (или ту библиотеку, которую вы использовали)


# 📌 Часть 2 — GIT
# все сделанное нужн озалить на свой репозиторий в GitHub и прикрепить ссылку а не файл с ДЗ!!!!!!!!!
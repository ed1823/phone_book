# 📒 Телефонный справочник (Django)

Простое веб-приложение для хранения, добавления и просмотра контактов. Поддерживает регистрацию, вход, выход и работу с контактами через защищённый интерфейс.

## 🚀 Функциональность

- Регистрация нового пользователя
- Аутентификация (вход/выход)
- Добавление контактов: имя, телефон, email
- Список всех контактов, добавленных пользователем
- Flash-сообщения об успехе/ошибке
- Простая адаптивная вёрстка с TailwindCSS
- Авторизация: доступ к контактам только после входа

## 🛠️ Стек технологий

- Python 3.13
- Django 5.2.4
- SQLite (по умолчанию)
- TailwindCSS + widget_tweaks (для оформления форм)

## 📁 Структура проекта

phone_book/
├── contacts/
│ ├── models.py # Модель Contact
│ ├── views.py # Обработчики: login, logout, register, list, add
│ ├── forms.py # Кастомная форма регистрации
│ ├── templates/
│ │ └── contacts/
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── contact_list.html
│ │ └── add_contact.html
├── phone_book/
│ └── settings.py
├── manage.py
└── requirements.txt



## 📦 Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/phone_book.git
cd phone_book


python3 -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows


pip install -r requirements.txt


python manage.py migrate


python manage.py runserver


http://127.0.0.1:8000/

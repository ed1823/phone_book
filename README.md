# Телефонный справочник (Django)

Простое веб-приложение для хранения, добавления и просмотра контактов. Поддерживает регистрацию, вход, выход и работу с контактами через защищённый интерфейс.

## Функциональность

- Регистрация нового пользователя
- Аутентификация (вход/выход)
- Добавление контактов: имя, телефон, email
- Список всех контактов, добавленных пользователем
- Flash-сообщения об успехе/ошибке
- Простая адаптивная вёрстка с TailwindCSS
- Авторизация: доступ к контактам только после входа

---

## Стек технологий

- [Python 3.13+](https://www.python.org/)
- [Django 5.2.4](https://www.djangoproject.com/)
- SQLite (по умолчанию)
- TailwindCSS + `widget_tweaks` (для стилизации форм)
- 📦 [uv](https://github.com/astral-sh/uv) — современный пакетный менеджер (альтернатива pip/pip-tools/venv)

---

## ⚙️ Установка и запуск проекта

### 1. Установите [`uv`](https://github.com/astral-sh/uv):

brew install astral-sh/tap/uv

git clone https://github.com/yourusername/phone_book.git
cd phone_book


### 2. Установите зависимости
uv venv  # создаёт и активирует виртуальное окружение
uv pip install --resolve=locked

### 3. Выполните миграции
python manage.py migrate

### 4. Запустите сервер
python manage.py runserver

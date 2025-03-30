# Todo App (Django)

Простой список задач (TODO приложение), реализованный с использованием Django. Пользователи могут добавлять, редактировать, удалять задачи, а также отслеживать их выполнение.

## Возможности

- **Добавление задачи** — добавление задач с указанием названия и описания.
- **Редактирование задачи** — возможность обновления задач.
- **Удаление задачи** — удаление задач из списка.
- **Отслеживание выполнения задачи** — установка статуса задачи как выполненной.

## Установка

1. Клонируйте репозиторий на ваш компьютер:

    ```bash
    git clone https://github.com/Oblivorten/todo.git
    cd todo
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

6. Откройте браузер и перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000), чтобы увидеть приложение в действии.

## Использование

1. **Регистрация и аутентификация**: Для работы с приложением нужно зарегистрироваться или войти в систему с использованием стандартной системы аутентификации Django.
   
2. **Создание задач**: На странице создания задачи укажите название, описание и статус задачи (выполнена или нет).
   
3. **Редактирование задач**: Перейдите на страницу задачи и измените её данные.
   
4. **Удаление задач**: Для удаления задачи перейдите на страницу задачи и подтвердите удаление.

## Структура проекта

- **`todoapp/`** — приложение для управления задачами.
  - **`migrations/`** — миграции базы данных.
  - **`models.py`** — модели данных для задач.
  - **`views.py`** — представления для отображения задач.
  - **`urls.py`** — маршруты для различных страниц приложения.
  - **`forms.py`** — формы для создания и редактирования задач.
  - **`templates/`** — HTML-шаблоны для отображения страниц.

- **`todo/`** — основной проект Django.
  - **`settings.py`** — настройки проекта.
  - **`urls.py`** — основной файл маршрутов для проекта.

## Требования

- Python 3.12.4
- Django 5.1.7 
- Для работы используется база данных SQLite, но её можно настроить в `settings.py`.




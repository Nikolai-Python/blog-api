# **blog-api**
### ***API текстового блога, которое позволяет создавать статьи, читать, редактировать и удалять их, комментировать статьи и ставить им оценки. ***

#### В данном API реализована аутентификация и авторизация, есть эндпоинты для получения, создания, обновления и удаления постов, категорий и комментариев. Также настроены отношения многие-к-одному и многие-ко-многим между этими ресурсами.

## **Руководство пользователя:**

#### Клонируйте репозиторий и перейдите в соответствующий каталог:
    git clone https://github.com/Nikolai-Python/blog-api.git
    cd blog-app
#### Создайте виртуальное окружение:
    pipenv install
    pipenv shell
#### Проведите миграции:
    python manage.py makemigrations
    python manage.py migrate
#### Запустите локальный:
    python manage.py runserver
#### Зарегистрируйтесь в API и сгенерируйте токен для авторизации:
- http://127.0.0.1:8000/api/v1/rest-auth/registration/
- введите Username, Email, Password1 (можно выбрать "Сгенерировать надёжный пароль" и далее "Использовать предложенный пароль")
- жмите Post и при получении ключа снова Post
#### Регистрация выполнена, токен сохранён, можно открыть API:
    http://127.0.0.1:8000/api/v1/rest-auth/login/
    c правами добавления, редактирования или удаления собственных записей

### **Пользуйтесь блогом: редактируйте или удаляйте статьи и заметки, добавляйте к ним комментарии и оценки**
-----
#### Страницы API:
- http://127.0.0.1:8000/api/v1/     список всех статей (Post List)
- http://127.0.0.1:8000/api/v1/id/   страница просмотра/редактирования статьи Post Instance
- http://127.0.0.1:8000/api/v1/comments/ список комментариев (Comment List)
- http://127.0.0.1:8000/api/v1/comments/id/ страница просмотра/редактирования комментария (Comment Instance)
- http://127.0.0.1:8000/api/v1/categories/ список категорий статей (Category List)
- http://127.0.0.1:8000/api/v1/categories/id/ страница просмотра/редактирования категории (Category Instance)
-----
### **При желании можно войти в админ.панель и потестить приложение изнутри**
#### Создайте суперпользователя:
- python manage.py createsuperuser
#### Запустите локальный сервер и перейдите в админ.панель с введёнными учётными данными:
    python manage.py runserver
    http://127.0.0.1:8000/admin/

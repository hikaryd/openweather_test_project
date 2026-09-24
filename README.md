 **OpenWeather** - Проект предоставляющий возможность сбора статистики о погоде в различных городах.
___
### **Что внутри**:
* Добавление города
* Сбор информации о погоде каждый чаc с https://openweathermap.org
___
### **Как запустить проект**:

* Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/hikaryd/openweather_test_project
cd openweather_test_project
```

### Настройка окружения

Скопируйте `.env.example` в `.env`. Задайте уникальный `POSTGRES_PASSWORD` и `DATABASE_URL` для пользователя `test_user` и базы `test_project` с тем же паролем. В URL специальные символы пароля нужно кодировать по правилам percent-encoding. Укажите `OPENWEATHERMAP_KEY`. Файл `.env` не добавляется в Git и в Docker-образ.

Пример формы URL: `postgresql+asyncpg://test_user:<url-encoded-password>@database:5432/test_project`.

### **Как запустит проект**:
* Поднимаем контейнеры:
   ```
   docker-compose up -d --build
   ```
___
### **Документация**:
* Весь список запросов можно посмотреть после запуска проекта:
```
http://127.0.0.1:8000/docs#/
```

* [hikaryd](https://github.com/hikaryd)
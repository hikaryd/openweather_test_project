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

### **Шаблон наполнения env-файла**:
1) Шаблон наполнения .env должен быть расположен по пути infra/.env :
    ```
    SECRET=test
    DATABASE_URL=postgresql+asyncpg://test_user:REDACTED_DB_PASSWORD@database:5432/test_project
    APP_TITLE=OpenWeatheTestProject
    OPENWEATHERMAP_KEY=
   ```


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
### ![[FastAPI](https://fastapi.tiangolo.com/tutorial/) ](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## Building a REST Api based on FastAPI for the brawl-skills's project
### FastAPI Documention on [FastAPI](https://fastapi.tiangolo.com/tutorial/) 

### Using an [ASGI](https://asgi.readthedocs.io/en/latest/) web server : [uvicorn](https://www.uvicorn.org/)


## Подключение к базе данных
1. Подключение к удаленному компьютеру через AnyDesk.
2. В AnyDesk настраиваем TCP-туннели:
- Прокладываем порты для соединения программы с БД (5432).
Теперь можно перейти к самой программе.

## Настройка и запуск сервиса
Для запуска приложения сервиса желательно использовать PyCharm. 
1. Необходимо создать новый проект, желательно использовать venv и выбрать интерпритатор python (там где он у вас установлен)
2. Скачиваем из проекта rest-api, и используем папку db_locally, которую необходимо установить в свой новый проект.
3. Необходимо с помощью терминала через команду 'pip install <библиотека>' загрузить: 
- sqlachemy
- fastapi
- psycopg2
- uvicorn
4. После загрузки библиотек необходимо также в терминале запустить саму программу командой: 'uvicorn db_locally.main:app --reload'
5. Теперь можете перейти по ссылке (локальному адресу), к url приписать '/docs' и получить документацию "Swagger UI".

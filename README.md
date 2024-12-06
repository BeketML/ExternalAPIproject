# External API Integration

## Описание
Это приложение использует FastAPI для взаимодействия с внешними API и предоставляет интерфейс для работы с данными.

## Требования
Перед запуском убедитесь, что у вас установлены следующие компоненты:

- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/BeketML/ExternalAPIproject.git
    cd ExternalAPIproject
    ```

2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

3. Активируйте виртуальное окружение:

    - Для Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - Для macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Локальный запуск

Для локального запуска используйте Docker Compose:

1. Запустите контейнеры:

    ```bash
    docker-compose up --build
    ```

2. Приложение будет доступно по адресу:

    ```
    http://localhost:7777
    ```

## Развертывание

Приложение можно развернуть на следующих бесплатных хостингах:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Vercel](https://vercel.com/)
- [Fly.io](https://fly.io/)

## Примечания

- Для работы с базой данных и других сервисов используйте файлы `.env` и `.env-non-dev` для настройки переменных окружения.
- Для миграции базы данных используйте Alembic командой:

    ```bash
    alembic upgrade head
    ```

## Лицензия

Этот проект лицензируется под MIT License - подробности см. в файле [LICENSE](LICENSE).

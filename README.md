# External API Integration

## Описание
Это приложение использует FastAPI для взаимодействия с внешними API и предоставляет интерфейс для работы с данными. Проект включает в себя CRUD операции для работы с внешним API, доступные только для администраторов.

## Основные функции
1. **Проверка состояния внешнего API**:
   - `/api-status` — проверяет, доступен ли внешний API. Возвращает сообщение о статусе соединения.

2. **Аутентификация и управление администраторами**:
   - Регистрация и вход администраторов с помощью маршрутов `/auth/register` и `/auth/login`.
   - Администраторы получают доступ к CRUD операциям через access token, который хранится в cookie.

3. **Работа с внешним API**:
   - Выполнение CRUD операций с внешним API с использованием авторизации администраторов.
   - Все операции защищены и доступны только для аутентифицированных администраторов.

![image](https://github.com/user-attachments/assets/3fe4d5df-02de-432b-af26-c7a41d30e68b)

## Требования
Перед запуском убедитесь, что у вас установлены следующие компоненты:

- Python 3.9+
- Docker
- Docker Compose

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

    [http://localhost:7777](http://localhost:7777)

## Развертывание
Приложение можно развернуть на следующих бесплатных хостингах:

- Render
- Railway
- Vercel
- Fly.io

Приложение доступно по следующей ссылке: [https://externalapiproject.onrender.com](https://externalapiproject.onrender.com), а для документации API используйте [https://externalapiproject.onrender.com/docs](https://externalapiproject.onrender.com/docs).

## Работа с внешним API
Этот проект предназначен для выполнения CRUD операций с внешним API. Однако доступ к этим операциям имеют только администраторы.

### Основные маршруты
1. **Проверка состояния внешнего API**:
   - Маршрут: `/api-status`
   - Описание: Проверяет доступность внешнего API.
   - Ответ:
     ```json
     {
       "status": "API is connected and working properly"
     }
     ```
   
2. **Регистрация администратора**:
   - Маршрут: `/auth/register`
   - Описание: Регистрация нового администратора.
   - Пример запроса:
     ```json
     {
       "email": "admin@example.com",
       "password": "securepassword"
     }
     ```

3. **Вход администратора**:
   - Маршрут: `/auth/login`
   - Описание: Вход администратора с получением access token.
   - Пример запроса:
     ```json
     {
       "email": "admin@example.com",
       "password": "securepassword"
     }
     ```
   - Ответ:
     ```json
     {
       "access_token": "your_access_token"
     }
     ```

4. **Выход администратора**:
   - Маршрут: `/auth/logout`
   - Описание: Выход администратора, удаляет access token.
   - Ответ:
     ```json
     {
       "message": "Successfully logged out"
     }
     ```

5. **Доступ к API с авторизацией**:
   - После получения access token администратор может использовать его для доступа к CRUD операциям с внешним API.

## Примечания
1. Для работы с базой данных и других сервисов используйте файлы `.env` и `.env-non-dev` для настройки переменных окружения.

2. Для миграции базы данных используйте Alembic командой:

    ```bash
    alembic upgrade head
    ```

## Лицензия
Этот проект лицензируется под MIT License - подробности см. в файле LICENSE.

---

### **Файлы конфигурации**

#### **1. `.env`**
Используется для локальной разработки:

```ini
# Database settings
DB_HOST=localhost             # Host for connecting to the database (use 'localhost' if running locally)
DB_PORT=5432                  # Port for connecting to PostgreSQL (default is 5432)
DB_USER=postgres              # Database username
DB_PASS=your_password_here    # Database user password
DB_NAME=your_database_name    # Name of the database

# Secret key for authentication (JWT, Flask, etc.)
SECRET_KEY="your_secret_key_here"   # Generate a unique and secure secret key for authentication
ALGORITHM=HS256                     # Encryption algorithm used for tokens (e.g., JWT)

# API URL for random users
RANDOM_USER_API_URL="https://randomuser.me/api/"  # URL for fetching random user data

#### **2. `.env-non-dev`**
Используется для развертывания на продакшн-серверах:

```ini
# Database settings
DB_HOST=your_production_db_host      # Host for production database
DB_PORT=5432                          # Port for connecting to PostgreSQL (default is 5432)
DB_USER=production_db_user            # Database username for production
DB_PASS=your_production_password      # Database user password for production
DB_NAME=production_database_name      # Name of the production database

# Secret key for authentication (JWT, Flask, etc.)
SECRET_KEY="your_production_secret_key_here"  # Unique and secure production secret key for authentication
ALGORITHM=HS256                           # Encryption algorithm used for tokens (e.g., JWT)

# API URL for random users (production)
RANDOM_USER_API_URL="https://randomuser.me/api/"  # URL for fetching random user data for production


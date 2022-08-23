# mayak-assignment-bot

## Как развернуть проект:

1. Склонировать проект, настроить .env файл(вписать TOKEN своего телеграм бота):
    ```
    git clone git@github.com:pakodev28/mayak-assignment-bot.git
    ```
    ```
    cd mayak-assignment-bot
    ```
    ```
    cp .env.example .env
    ```
2. Запустить проект через контейнер Docker:
    ```
    docker build -t <create image name> .
    ```
    ```
    docker run --name <create container name> -it <image name>
    ```
3. Остановить контейнер:
    ```
    docker container stop <CONTAINER ID> or <container name>
    ```  


### @mayak_assignment_bot (пишите если нужно запустить бота)
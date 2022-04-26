# Ответ на задание

Можете взять и скопировать в терминал эту команду полностью

```bash
docker run -d \ # запускаем контейнер в фоновом режиме
  --name postgres-13 \ # с именем postgres-13
  --mount type=tmpfs,dst=/var/lib/postgresql/data,tmpfs-size=1G \ # монтируем tmpfs в контейнер по пути /var/lib/postgresql/data и ограничиваем том размером 1G
  -e POSTGRES_PASSWORD=pa55w0rd \ # задаем минимально необходимый параметр - пароль для пользователя postgres
  postgres:13 # из образа postgres:13
```

# Практическая работа

## Смотрим на процессы с точки зрения хостовой ОС

Запускаем несколько контейнеров

```docker run -d nginx```

```docker container ls```

Смотрим на процессы
```ps -axfo pid,ppid,uname,cmd |grep nginx```
и убиваем один из процессов nginx
```kill -9 PID```

```docker container ls``` - видим, что контейнеры пропали

Так же можем посмотреть дерево

## Ограничиваем контейнеры по памяти

Запускаем контейнер с ограничением по памяти
```docker run -d -m=100m --name lowmem100 monitoringartist/docker-killer:latest membomb```

Смотрим причину падения контейнера
```docker inspect lowmem100 |grep OOM```

## Ограничиваем контейнеры по CPU

Запускаем 2 контейнера с разным ограничением по памяти
```docker run -d --cpus=1 --name fast nginx```
и
```docker run -d --cpus=0.01 --name slow nginx```

```docker exec slow sha1sum /etc/hosts``` – работает долго
```docker exec fast sha1sum /etc/hosts``` – работает быстро

## Namespaces

Посмотреть все неймспейсы и процессы в них можно вот так:

```lsns```

## Capabilities

Посмотреть capabilities можно тут:
```cat /proc/XXX/status |grep Cap```

Запустим привилегированный  контейнер
```docker run -d --rm --privileged alpine sleep 10000```
и без привилегий
```docker run -d --rm alpine sleep 20000```

Находим его pid
```ps axfo pid,ppid,uname,cmd |grep sleep```

```cat /proc/XXX/status  |grep Cap```
и видим, что для этих двух контейнеров они различаются

## Запускаем контейнер через RunC

```bash
mdkir demo-bundle
cd demo-bundle 
runc spec – создаёт шаблон config.json
```

Давайте попробуем запустить этот контейнер!
```runc run test```

создадим директорию, которую ищет runc
```mkdir rootfs```

```runc run test``` – другая ошибка, теперь не найден shell.

Создание корня файловой системы – довольно долгий и трудоёмкий процесс, поэтому давайте просто возьмём готовую!

Достаем OCI image
```skopeo copy docker://busybox:latest oci:busybox:latest```

Создаем OCI Runtime Bundle из OCI Image
```umoci unpack --image busybox:latest bundle```

Давайте скопируем rootfs в наш контейнер
```cp -r ./bundle/rootfs/* ./rootfs/```

Теперь у нас есть всё готовое, чтобы запустить контейнер через runc
Но сначала давайте добавим какой-нибудь маркер в нашу файловую систему
```touch ./rootfs/notice_me```

```runc run test```

И мы в shell нашего контейнера!
```ls```
Видим notice_me

Теперь откроем новое окно терминала и выполним
```runc list```

Кстати, у нас же запущено несколько docker контейнеров, почему runc их не видит?
В отличие от докера, у runc нет демона, который бы следил за контейнерами.
Runc хранит состояние своих контейнеров на файловой системе, по умолчанию в `/run/runc/CONTAINER_NAME/state.json`

Так как же нам убедиться, что контейнеры докера тоже могут управляться через runc?
Указать runc в качестве корневой директории ту, где хранятся контейнеры, запущенные докером
```runc --root /run/docker/runtime-runc/moby list```

### Самостоятельная работа

Давайте запустим какое-нибудь приложение непосредственно через containerd?

ContainerD управляется утилитой ctr, синтаксис похож на docker, но есть нюансы

```ctr run -d docker.io/library/nginx:latest ctrnginx``` – получаем ошибку, image не найден.
Containerd не пулит образ автоматически, если его нет – сделать это нужно руками.

```ctr image pull docker.io/library/nginx:latest```

```ctr run -d docker.io/library/nginx:latest ctrnginx```

```ctr tasks exec -exec-id 1006 ctrnginx curl 127.0.0.1```

```docker container ls``` -  не видим наши контейнеры!

Проверка:
```ctr tasks exec -exec-id 1006 ctrnginx curl 127.0.0.1``` на машине

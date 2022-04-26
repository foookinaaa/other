# Стенды для интенсива

Для выполнения практических заданий для каждого студента развернут собственный стенд (небольшая VM в облаке Selectel). Сейчас нам нужно будет зайти туда и проверить, что мы все находимся на старте и готовы бежать в нужную сторону :)

Для доступа к стендам вам понадобятся данные из личного кабинета https://edu.slurm.io, а именно:

- номер студента (он же номер логина, логин студента и т.п.). Выглядит как буква s и шесть цифр, например `s000001`.
- пароль оттуда же, из ЛК - он потребуется для входа на джамп-хост (он же админбокс, он же sbox), а также в наш Gitlab по адресу https://gitlab.slurm.io

## Практическая работа

1. Заходим по SSH на sbox. Не забудьте заменить плейсхолдер на ваш личный номер студента:

```bash
ssh <Ваш номер логина>@sbox.slurm.io
```

2. Заходим с sbox на подготовленный стенд с Docker:

```bash
ssh docker.<Ваш номер логина>
```

3. Становимся root:

```bash
sudo -i
```

4. Проверяем версию Docker, которая там установлена:

```bash
docker version
```

Ответ должен быть примерно таким:

```bash
Client: Docker Engine - Community
 Version:           20.10.3
 API version:       1.41
 Go version:        go1.13.15
 Git commit:        48d30b5
 Built:             Fri Jan 29 14:34:14 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.3
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       46229ca
  Built:            Fri Jan 29 14:32:37 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.3
  GitCommit:        269548fa27e0089a8b8278fc4fc781d7f65a939b
 runc:
  Version:          1.0.0-rc92
  GitCommit:        ff819c7e9184c13b7c2607fe6c30ae19403a7aff
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

Отлично! Мы готовы запускать контейнеры и делать разные крутые штуки.

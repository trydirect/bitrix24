![Alt text](assets/logo.jpg?raw=true "BitrixDock")

# BitrixDock
BitrixDock позволяет легко и просто запускать **Bitrix CMS** на **Docker**.

## Введение
BitrixDock облегчает разработку на Битрикс предоставляя готовые сервисы PHP, NGINX, MySQL и многие другие.

### Начало работы
```
mkdir -p /var/www/bitrix && \
cd /var/www/bitrix && \
wget http://www.1c-bitrix.ru/download/scripts/bitrixsetup.php && \
cd /var/www/ && \
git clone https://github.com/bitrixdock/bitrixdock.git && \
cd /var/ && chmod -R 775 www/ && chown -R root:www-data www/ && \
cd /var/www/bitrixdock
```

- Выполните настройку iptables

```
iptables -A DOCKER-FIREWALL -p tcp -m tcp  -m state --state  NEW -m multiport --dports 8893,8894,8895,8890,8891,5222,5223 -j RETURN
```

- Выполните настройку .env

По умолчнию используется nginx php7, эти настройки можно изменить в файле ```.env```. Также можно задать путь к каталогу с сайтом и параметры базы данных MySQL.


```
PHP_VERSION=php7           # Версия php 
WEB_SERVER_TYPE=nginx      # Веб-сервер nginx/apache
MYSQL_DATABASE=bitrix      # Имя базы данных
MYSQL_USER=bitrix          # Пользователь базы данных
MYSQL_PASSWORD=123         # Пароль для доступа к базе данных
MYSQL_ROOT_PASSWORD=123    # Пароль для пользователя root от базы данных
INTERFACE=0.0.0.0          # На данный интерфейс будут проксироваться порты
SITE_PATH=/var/www/bitrix  # Путь к директории Вашего сайта

```

- Запустите bitrixdock
```
docker-compose up -d
```
Чтобы проверить, что все сервисы запустились посмотрите список процессов ```docker ps```.  
Посмотрите все прослушиваемые порты, ```netstat -plnt```, должны быть:
tcp6       0      0 :::443                  :::*                    LISTEN      19508/docker-proxy  
tcp6       0      0 :::8893                 :::*                    LISTEN      19497/docker-proxy  
tcp6       0      0 :::8894                 :::*                    LISTEN      19486/docker-proxy  
tcp6       0      0 :::8895                 :::*                    LISTEN      19467/docker-proxy  
tcp6       0      0 :::9000                 :::*                    LISTEN      19989/docker-proxy  
tcp6       0      0 :::3306                 :::*                    LISTEN      19768/docker-proxy  
tcp6       0      0 :::11211                :::*                    LISTEN      19450/docker-proxy  
tcp6       0      0 :::80                   :::*                    LISTEN      19519/docker-proxy 
Откройте IP машины в браузере.
 

## Как заполнять подключение к БД
![db](https://raw.githubusercontent.com/bitrixdock/bitrixdock/master/db.png)

## Как активировать push and pull module

В разделе Settings > System settings > Module settings > Push and Pull

- Send PUSH notifications to mobile devices: OK
- Server software: Bitrix Virtual Appliance 4.4 or higher (nginx-push-stream-module 0.4.0)
- Server command publish URL

Message sender path:	http://webserver_container_ip:8895/bitrix/pub/

- Command reading URL for modern browsers

Message listener path (HTTP): http://10.100.0.5:8893/bitrix/sub/

## Примечание
- По умолчанию стоит папка ```/var/www/bitrix/```
- В настройках подключения требуется указывать имя сервиса, например для подключения к mysql нужно указывать "mysql", а не "localhost". Пример [конфига](configs/.settings.php)  с подклчюением к mysql и memcached.
- Для загрузки резервной копии в контейнер используйте команду: ```cat /var/www/bitrix/backup.sql | docker exec -i mysql /usr/bin/mysql -u root -p123 bitrix```
- 

## Отличие от виртуальной машины Битрикс
Виртуальная машина от разработчиков битрикс решает ту же задачу, что и BitrixDock - предоставляет готовое окружение. Разница лишь в том, что Docker намного удобнее, проще и легче в поддержке.

Как только вы запускаете виртуалку, Docker сервисы автоматически стартуют, т.е. вы запускаете свой минихостинг для проекта и он сразу доступен.

Если у вас появится новый проект и поменяется окружение, достаточно скопировать чистую виртуалку (если вы на винде), скопировать папку BitrixDock, добавить или заменить сервисы и запустить.

P.S.
Виртуальная машина от разработчиков битрикс на Apache, а у нас на Nginx, а он работает намного быстрее и кушает меньше памяти.


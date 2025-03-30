Интернет-магазин одежды  
1. создайте файл .env.dev в директории shop   
SECRET_KEY='секретный ключ джанго'  
ALLOWED_HOSTS=localhost 127.0.0.1  
CSRF_TRUSTED_ORIGINS=http://localhost:8001  
POSTGRES_USER=django  
POSTGRES_PASSWORD=password  
POSTGRES_DB=shop  
POSTGRES_PORT=5432  
EMAIL_HOST_USER = email откуда будут приходить коды для регистрации (email.test)  
EMAIL_HOST_PASSWORD = пароль для данного email
DEFAULT_FROM_EMAIL = полностью email (email.test@yandex.ru)

Вышеуказанный email вы можете создать через яндекс, иструкция ниже  
https://yandex.ru/support/yandex-360/customers/mail/ru/mail-clients/others.html  

2. Запускаем приложение
   docker compose up



Для регистрации вам необходимо подключить почту для отправки сообщений,  
так как регистрация реализована через коды подтверждения  
  
Но если вам лень это делать, то   
можете воспользоваться админом (логин и пароль - admin)  

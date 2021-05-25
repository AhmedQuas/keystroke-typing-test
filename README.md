# Project for biometry at WUST

## Getting started

Replace `your_db_name`, `your_db_user`, `your_db_user_passwd` with your own data in below sed's.

```
git clone https://github.com/AhmedQuas/keystroke-typing-test.git

cd keystroke-typing-test

# Set database name & credentials
sed -i -r "s/DATABASE=/DATABASE=your_db_name/g" .env
sed -i -r "s/DB_USER=/DB_USER=your_db_user/g" .env
sed -i -r "s/PASSWD=/PASSWD=your_db_user_passwd/g" .env

sed -i -r "s/user=''/user='your_db_user'/g" app/database.py
sed -i -r "s/passwd=''/passwd='your_db_user_passwd'/g" app/database.py
sed -i -r "s/dbname=''/dbname='your_db_name'/g" app/database.py

docker-compose up
```

Useful links:
- `Swagger UI` - localhost/docs
- `Website` - ./keystroke-typing-test/website/index.html
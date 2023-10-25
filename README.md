# Movieswipe

To run the project

```
docker build -t movieswipe_db_image .
docker run -p 5432:5432 -d movieswipe_db_image
npm run serve  # In order to have the front build at change
python3 manage.py migrate
python3 manage.py runserver  # To start the backend
```

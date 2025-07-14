-----------------Endpoints Overview-------------------





Migrate

python manage.py migrate  


install all the Python packages listed in the requirements.txt


pip install -r requirements.txt

Run the server

python manage.py runserver








Method	URL	Description




POST	/api/news/register/	Register a user


POST	/api/news/token/	Get JWT token


GET	/api/news/latest/	Fetch & summarize latest news


GET	/api/news/search/?q=term	Search and summarize news


POST	/api/news/save/	Save article (JWT required)


GET	/api/news/saved/	Get saved articles for user













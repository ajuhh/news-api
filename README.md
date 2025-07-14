Endpoints Overview
Method	URL	Description
POST	/api/news/register/	Register a user
POST	/api/news/token/	Get JWT token
GET	/api/news/latest/	Fetch & summarize latest news
GET	/api/news/search/?q=term	Search and summarize news
POST	/api/news/save/	Save article (JWT required)
GET	/api/news/saved/	Get saved articles for user










pip install -r requirements.txt


python manage.py migrate  
python manage.py runserver
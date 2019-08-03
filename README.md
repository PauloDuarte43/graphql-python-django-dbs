# graphql-python-django-dbs

### Python version: 3.6.9

1. git clone https://github.com/PauloDuarte43/graphql-python-django-dbs.git
2. pip install -r requirements.txt
3. python manage.py runserver
4. open http://localhost:8000/graphql
5. execute query: 
```
query {
	addresses {
		id
		street
		number
	}
}
```
6. execute query: 
```
query {
	links {
		id
		description
		url
	}
}
```

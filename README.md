### Recruitment task
Attempt on recruitment task for Python Django developer

### Dev environment
To run dev environment preferably use `docker-compose`

```bash
docker-compose up
```

After the successful startup enter container
```bash
docker-compose exec web /bin/bash
```
And here you can use django's `manage.py` command easily such as migrations and creating superuser for admin access

### Task branch with Celery
There's other branch called `feature/celery-background-task-csv` which was supposed to start work on last bullet point of the recruitment task.
Due to lack of time it's unfinished.

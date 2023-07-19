flower:
	guix shell python python-redis python-celery python-flower -- celery --app myapp.tasks --broker=redis://localhost:6379/0 --result-backend=redis://localhost:6379/1  flower --log_file_prefix=./logs

worker1:
	guix shell python python-redis python-celery -- celery -A myapp.tasks worker -Q memory-intensive --concurrency=2 --loglevel=info

worker2:
	guix shell python python-redis python-celery -- celery -A myapp.tasks worker -Q high-performance --concurrency=4 --loglevel=info

pyclient:
	guix shell python python-redis python-celery -- python3 pyclient.py

httpclient:
	guix shell python python-requests python-redis python-celery -- python3 httpclient.py

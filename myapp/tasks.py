from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

@app.task
def process_thumbnail(image_path):
    # Perform thumbnail processing logic here
    return f"GVAF: process_thumbnail {image_path}"

@app.task
def process_resize(image_path):
    # Perform resize processing logic here
    return f"GVAF: process_resize {image_path}"


# Routing Configuration
app.conf.task_routes = {
    'myapp.tasks.process_thumbnail': {'queue': 'high-performance'},
    'myapp.tasks.process_resize': {'queue': 'memory-intensive'},
}

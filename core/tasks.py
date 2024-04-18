from celery import Celery

# Create a Celery instance and configure it to use RabbitMQ as the broker.
# Replace 'localhost' with the name or IP of your RabbitMQ service if it's different.
app = Celery('simple_task', broker='amqp://guest:guest@localhost')

# Define a simple task that adds two numbers
@app.task
def add(x, y):
    return x + y

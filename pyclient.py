from myapp.tasks import process_thumbnail, process_resize

# Submit thumbnail tasks
result = process_thumbnail.delay('path/to/image1.jpg')
print(result.id)
print(result.status)
print(result.get())

# Submit resize tasks
result = process_resize.delay('path/to/image3.jpg')
print(result.id)
print(result.status)
print(result.get())



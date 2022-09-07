
import os


def upload(request, path=r'/tmp'):
    if request.method == 'POST':
        f = request.files.getlist('file')
        for i in f:
            i.save(os.path.join(path, i.filename))

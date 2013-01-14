from cStringIO import StringIO
import Image

THUMB_SIZE = 120, 120


def load_resized(filename):
    io = StringIO()
    _resize_image(filename, io)
    io.seek(0)
    return io


def _resize_image(path, output_handle):
    img = Image.open(path)
    width, height = img.size

    if width > height:
       delta = width - height
       left = int(delta/2)
       upper = 0
       right = height + left
       lower = height
    else:
       delta = height - width
       left = 0
       upper = int(delta/2)
       right = width
       lower = width + upper

    img = img.crop((left, upper, right, lower))
    img.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

    img.save(output_handle, 'JPEG', quality=70)
    return output_handle
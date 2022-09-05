from django.core.exceptions import ValidationError


def validate_file_size(value):
  filesize= value.size
  print(filesize)
  if filesize > 204800:
    raise ValidationError("The maximum file size that can be uploaded is 200KB")
  else:
    return value

def validate_file_extension(value):
  import os
  from django.core.exceptions import ValidationError
  ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
  valid_extensions = ['.jpg', '.png']
  if not ext.lower() in valid_extensions:
    raise ValidationError('Unsupported file extension.')
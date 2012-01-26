from django.contrib.auth.models import User


# Create your views here.

def registerUser(username, password, email):
  user = User.objects.create_user(username, email, password)
  pass

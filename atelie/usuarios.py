from django.contrib.auth.models import User
user = User.objects.create_superuser('Emerson', 'teste', 'e102030')

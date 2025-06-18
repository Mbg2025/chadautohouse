from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='Hasko').exists():
    User.objects.create_superuser('Hasko', 'chadauto.housing@gmail.com', 'Hasko@25')
from django.contrib.auth import get_user_model
User = get_user_model()
try:
    user = User.objects.get(username='admin')
    print(f"Usuario: {user.username}, is_staff: {user.is_staff}, is_superuser: {user.is_superuser}")
    if not user.is_staff:
        user.is_staff = True
        user.save()
        print("Se ha activado is_staff para el usuario 'admin'.")
except User.DoesNotExist:
    print("El usuario 'admin' no existe.")
exit()
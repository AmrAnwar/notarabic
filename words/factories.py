import  factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'myapp.User'  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    username = 'john'
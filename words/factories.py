import  factory
from django.contrib.auth.models import User
from .models import UserWord

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    username = 'john'
    password = '123456Aa'


class UserWordFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserWord

    user = factory.Iterator(User.objects.all())
    description = factory.Sequence(lambda a:
                                           'اهلا بك في في بنرامج البرنامج تادااااااااااااا %d'%a)


    example = factory.Sequence(lambda a:'{0}  لما عم الحج يعدي '
                                           .format(a))


    @factory.post_generation
    def up_vote(self, create, extracted):
        if  create and not extracted:
            # used when u Pass UserWordFactory()

            for user in User.objects.all():
                self.up_vote.add(user)

        if extracted:
            # used when u Pass UserWordFactory(up_vote=(1,2))
            for user in extracted:
                self.up_vote.add(user)

    @factory.post_generation
    def down_vote(self, create, extracted):
        if create and not extracted:
            # used when u Pass UserWordFactory()
            for user in User.objects.all():
                self.down_vote.add(user)

        if extracted:
            # used when u Pass UserWordFactory(down_vote=(1,2))
            for user in extracted:
                self.down_vote.add(user)

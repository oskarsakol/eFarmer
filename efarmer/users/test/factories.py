import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    address = factory.Faker('address')
    city = factory.Faker('city')
    phone = '123456789'

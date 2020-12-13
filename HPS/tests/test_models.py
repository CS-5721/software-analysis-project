from django.test import TestCase
from housemate.models import User, Habits, ShareProfile, Property, RentalProperty, Landlord, MatchedHouseIteratorFactory
import django.db
import random
import pprint

django.db.connection.creation.create_test_db # in memory db

from housemate.hps_logger import *
logger = Logger.instance()

pp = pprint.PrettyPrinter(indent=4)

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username="Victor", email="VictorEmail@gmail.com",phone="3532334566", password="Login@123")

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = User._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_phone_label(self):
        user = User.objects.get(id=1)
        field_label = User._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_email_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_password_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 50)

    def test_password_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEqual(max_length, 60)

    def test_email_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 75)

    def test_phone_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 20)

    def test_object_returns_username(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.username}'
        self.assertEqual(expected_object_name, str(user))

    def test_object_does_not_returns_password(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.password}'
        self.assertNotEqual(expected_object_name, str(user))



class HabitsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Habits.objects.create(traits="clean,organised")

    def test_object_returns_traits(self):
        habit = Habits.objects.get(id=1)
        expected_object_name = f'{habit.traits}'
        self.assertEqual(expected_object_name, str(habit))

class FactoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(username="Mr Rugg", email="rugg@example.com", phone="12345678", password="avarice")
        ll = Landlord.objects.create(uname_id=u.id, rtb_id=666)
        #pp.pprint(ll)
        #print(dir(ll))
        for i in range(100):
            rent = random.randint(800, 2500)
            p = Property.objects.create(ownername_id=ll.uname.id,address="Hovel Avenue", description="A luvverly house")
            r = RentalProperty.objects.create(rentID_id=p.id, rent=rent)


    def test_house_factory(self):
        count = 0
        i = MatchedHouseIteratorFactory({"rent":1500}).getIterator()
        #print(dir(i))
        for h in i: # Python's for can use Iterator instances
            count += 1
            self.assertLessEqual(h.rent, 1500)
        #print(count)
        self.assertGreaterEqual(count, 1)



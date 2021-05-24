from django.test import TestCase
from things.models import Location
from django.core.exceptions import ValidationError

# Create your tests here.


class LocationModelTest(TestCase):

    def test_default_text(self):
        location_ = Location()
        self.assertEqual(location_.name, '')

    def test_cannot_save_blank_item(self):
        location_ = Location(name='')
        with self.assertRaises(ValidationError):
            location_.save()
            location_.full_clean()

    def test_string_representation(self):
        location_ = Location.objects.create(name="text")
        self.assertEqual(str(location_), "text")

    def test_get_url(self):
        location_ = Location.objects.create(name="text")
        self.assertEqual(location_.get_absolute_url(), "/location/1/")
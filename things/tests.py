from django.test import TestCase
from things.models import Location, Container
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


class ContainerModelTest(TestCase):

    def test_default_text(self):
        container_ = Container()
        self.assertEqual(container_.name, '')

    def test_cannot_save_blank_item(self):
        location_ = Location.objects.create(name="test")
        container_ = Container(name='', location=location_)
        with self.assertRaises(ValidationError):
            container_.save()
            container_.full_clean()
        
    def test_string_representation(self):
        location_ = Location.objects.create(name="test")
        container_ = Container.objects.create(name="test", location=location_)
        self.assertEqual(str(container_), "test - 1")

    def test_get_url(self):
        location_ = Location.objects.create(name="test")
        container_ = Container.objects.create(name="test", location=location_)
        self.assertEqual(container_.get_absolute_url(), "/location/1/container/1/")
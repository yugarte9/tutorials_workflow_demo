from tutorials.models import Tutorial
from django.test import TestCase

from django.urls import reverse
import pytest
# Create your tests here.


def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
def test_create_tutorial(tutorial):
    @pytest.fixture
    def new_tutorial(db):
        tutorial = Tutorial.objects.create(
            title='Pytest',
            tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
            description='Tutorial on how to apply pytest to a Django application',
            published=True
        )
        assert tutorial.title == "Pytest"

    def test_search_tutorials(new_tutorial):
        assert Tutorial.objects.filter(title='Pytest').exists()

    def test_update_tutorial(new_tutorial):
        new_tutorial.title = 'Pytest-Django'
        new_tutorial.save()
        assert Tutorial.objects.filter(title='Pytest-Django').exists()

"""Module for test models"""
import pytest
from testapp.models import City, User


@pytest.mark.django_db
def test_create_city():
    """test simply query"""
    city = City.objects.create(name="London")
    assert city.name == "London"


@pytest.mark.django_db
def test_create_user():
    """Test foreignKey"""
    city = City.objects.create(name="London")
    user = User.objects.create(first_name='Bob', last_name='Chan', city=city)
    assert user.city == city
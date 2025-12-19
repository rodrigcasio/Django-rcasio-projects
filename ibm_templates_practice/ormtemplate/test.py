# test.py
# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from standalone.models import Test

# Delete all data
def clean_data():
    Test.objects.all().delete()

# Test Django Model Setup
def test_setup():
    try:
        clean_data()
        
        # Create a new Test object
        test = Test(name="test name")
        test.save()
        
        # Check test table is not empty
        assert Test.objects.count() == 1
        
        print("Django Model setup completed.")
        
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise (exception)
    except:
        print("Unexpected error")

test_setup()

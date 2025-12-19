import os
import sys

if __name__ == '__main__':
    os.environ.setdefault("DJNAGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Could import Django. Are you sure it is installed and "
                "available on your PYTHONPATH enviroment variable? Did you forget "
                " to active a virtual enviroment?"
            )
        raise 
    execute_from_command_line(sys.argv)


"""
This code snippet is the setting module of our orm_template project
and able execute Django built-in commands such as migrations
"""

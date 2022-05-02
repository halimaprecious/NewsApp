from app import create_app
from flask_script import Manager,Server

#creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.command
def test():
    '''runs unit tests'''
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=1).run(test)


if __name__ == '__main__':
    manager.run()
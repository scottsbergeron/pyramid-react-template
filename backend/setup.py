from setuptools import (
    find_packages,
    setup
)

requires = [
    'gunicorn[gevent]',
    'mysqlclient',
    'pylibmc',
    'pyramid',
    'SQLAlchemy'
]

setup(
    name='app',
    fullname='Application API',
    version='0.0.1',
    description='Application API',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = app:main'
        ]
    }
)

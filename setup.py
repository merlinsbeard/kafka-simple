from setuptools import setup, find_packages

setup(
    name="kafCon",
    version="0.0.1",
    description="Simple Kafka Consumer and Producer",
    url="caffeine.dailywarrior.ph",
    author="merlinsbeard",
    author_email="bjpaat@dailywarrior.ph",
    license="MIT",
    packages=['kafsim'],
    install_requires=[
        'fire==0.1.2',
        'kafka-python==1.3.5',
    ],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['kafsim=kafsim.kc:main'],
    }

)


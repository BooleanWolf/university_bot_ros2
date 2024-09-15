from setuptools import find_packages, setup

package_name = 'varsity_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tam1m',
    maintainer_email='tam1m@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello = varsity_bot.hello:main', 
            'main = varsity_bot.bot_main:main',
            'chatter = varsity_bot.answer_back:main',
        ],
    },
)

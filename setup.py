from setuptools import setup, find_packages


with open('README.md') as readme:
    next(readme)  # skip the first line
    long_description = ''.join(readme).strip()

with open('requirements.txt') as requirements:
    install_requires = [line.strip() for line in requirements]


setup(
    name='pastry',
    version='0.8',
    author='Jiangge Zhang',
    author_email='tonyseek@gmail.com',
    url='https://github.com/szulabs/pastry',
    description='The official site of szulabs.',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'pastry-admin = pastry.management:execute_from_command_line',
        ],
    },
    classifiers=[
        'Private :: Do Not Upload',
    ]
)

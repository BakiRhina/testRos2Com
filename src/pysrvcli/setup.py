from setuptools import find_packages, setup

package_name = 'pysrvcli'

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
    maintainer='kyu8',
    maintainer_email='guillemsenabre@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'service = pysrvcli.service_member_function:main',
		'client = pysrvcli.client_member_function:main',
        ],
    },
)

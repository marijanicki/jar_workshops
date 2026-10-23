from setuptools import find_packages, setup

package_name = 'localizacion'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AIR Club UdeSA',
    maintainer_email='rafadiaz71@gmail.com',
    description='Semana 06 del Challenge JAR: Filtro de partículas y localización en el mapa.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'campo_verosimilitud = localizacion.campo_verosimilitud:main',
            'localizador = localizacion.localizador:main',
        ],
    },
)
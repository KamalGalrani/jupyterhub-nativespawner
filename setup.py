from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jupyterhub-nativespawner',
    version='0.0.1',
    description='JupyterHub Native Spawner',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/KamalGalrani/nativespawner',
    author='Kamal Galrani',
    author_email='kamal.galrani@tvarit.com',
    license='3 Clause BSD',
    packages=find_packages(),
    install_requires=['jupyterhub>=0.8'],
    include_package_data=True,
)

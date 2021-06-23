
import os
from setuptools import setup



def package_data(pkg, roots):
  
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='jupyterhub',
    version='1.0',
    description='Jupyterhub',
    license='AGPL v3',
    packages=[
        'jupyterhub',
    ],
    install_requires=[
        'XBlock',
        'requests'
    ],
    entry_points={
        'xblock.v1': [
            'jupyterhub = jupyterhub:JupyterhubXBlock',
        ]
    },
    package_data=package_data("jupyterhub", ["static"]),
)
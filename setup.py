
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
    name='jupyterhub_xblock',
    version='1.0',
    description='Jupyterhub XBlock',
    license='AGPL v3',
    packages=[
        'jupyterhub_xblock',
    ],
    install_requires=[
        'XBlock',
        'requests'
    ],
    entry_points={
        'xblock.v1': [
            'jupyterhub_xblock = jupyterhub_xblock:JupyterhubXBlock',
        ]
    },
    package_data=package_data("jupyterhub_xblock", ["static"]),
)
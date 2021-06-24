# JupyterHub-XBlock
Jupyterhub XBlock for Tutor Jupyter plugin..

This XBlock designed to integrate the JupyterHub plugin(https://github.com/murat-polat/tutor-contrib-jupyter) into the Tutor Open edX. 
After the plugin is installed and tested, it can implement to edX Studio as a Advanced Module. JupyterHub is awesome educational tool. And in this article you can find som exampels about it:

https://docs.google.com/document/d/1WU41WSm-uZ_yprKr1955k3GbCc7Q4F8wHs-3v5XAbuE/edit

### Installation:

`cd .local/share/tutor/env/build/openedx/requirements `
or

`cd "$(tutor config printroot)/env/build/openedx/requirements"`

`git clone https://github.com/murat-polat/jupyterhub-xblock`

`echo "-e ./jupyterhub-xblock" >> private.txt`

`pip3 install -e jupyterhub-xblock `

`tutor images build openedx `

Rebuild of openedx takes same time (apx. 17 minute)

`tutor local quickstart`

### Using in EdX Studio:

- login to studio as a staff or superuser
- Create a course, than settings=>advanced settings=> Advanced Module List add  `"jupyterhub"` and save
- Now you can use JupyterHub as a Unit, for every type of course. But first, you need to edit your JupyterHub (Name, ButtonText, and your JupyterHub URL)

That's it :)


![](/src/jupyterhub.gif)
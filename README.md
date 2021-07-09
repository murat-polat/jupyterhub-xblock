# JupyterHub-XBlock
Jupyterhub,JupyterNotebook, JupyterLab XBlock for Tutor Jupyter plugin..

This XBlock designed to integrate the JupyterHub plugin(https://github.com/murat-polat/tutor-contrib-jupyter) into the Tutor Open edX. 
After the plugin is installed and tested, it can implement to edX Studio as a Advanced Module. JupyterHub/JupyterNotebook is awesome educational tool. And in this article you can find som exampels about it:

https://docs.google.com/document/d/1WU41WSm-uZ_yprKr1955k3GbCc7Q4F8wHs-3v5XAbuE/edit

### Installation:

`cd .local/share/tutor/env/build/openedx/requirements `
or

`cd "$(tutor config printroot)/env/build/openedx/requirements"`

`git clone https://github.com/murat-polat/jupyterhub-xblock`

`echo "-e ./jupyterhub-xblock" >> private.txt`

`pip3 install -e jupyterhub-xblock `

`tutor images build openedx `

Rebuild of openedx takes same time (apx. 20 minute)

`tutor local quickstart`

## Using in EdX Studio:

Jupyterhub XBlock comes with to main users " student (password: solo) " and " teacher (password: soloadmin) ". You can change password and create mulitable users and administrators, which will be explained soon.

- login to studio as a staff or superuser
- Create a course, than settings=>advanced settings=> Advanced Module List add  `"jupyterhub"` and save

![](/src/advanced_module.jpg)
- Now you can use JupyterHub as a Unit, for every type of course. But first, you need to edit your JupyterHub (Name, ButtonText, JupyterHub URL, JupyterNotebook URL(you will create this later) and JupyterLab URL )

![](/src/edit_studio.jpg)

- You need to create a notebook for students view in your course.To do that click to " `Start JupyterHub in new tab`" login as " student " password is "solo". Then New => Python3(ipykernel). dobbel click to "Untitled" and rename it whatever you want.

![](/src/demoNotebook.jpg)

 Copy the URL of your notebook and paste in " Edit=> JupyterNotebook URL" save and refreh your page. Now your notebook is ready to publish.


![](/src/XblockOverview.jpg)

Students can change, edit, share, rename. It may be a good idea to save as a separate notebook, before they start to change it. For eksempel save as "user2_test.ipynb". Doesn't matter all file be located in same folder.

### User administration:


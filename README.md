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

Start new browser and login as a "teacher" which is administrator of JupyterHub/JupyterLab Password is: 'soloadmin'.
Click to 'Control Panel' => 'Admin'

![](/src/adminPanel.jpg)

Here you can add/delete new user, admin, start and stop server. But for changing password or assigning a password for new users, you must go in the contaniner. To do that:

`$  docker exec -it tutor_local_jupyter_1 bash`

`$ passwd teacher` and give new password for this admin user

![](/src/changePass.jpg)



#### For developers:

This XBlock uses default PAM Authenticator(https://jupyterhub.readthedocs.io/en/stable/reference/authenticators.html#the-default-pam-authenticator). That's mean  basic linux/Unix user administartions `$ adduser <user_name>`. If user is system user in docker container, will be JupyterHub and JupyterLab user also. 
First to user(student, and teacher) comes from the Dockerfile(https://github.com/murat-polat/tutor-contrib-jupyter/blob/c957673a40ed4f66b6c2c67794b91213eb7e50ff/tutorjupyter/templates/jupyter/build/jupyter/Dockerfile#L45) and 

the "jupyterhub_config.py" (https://github.com/murat-polat/tutor-contrib-jupyter/blob/master/tutorjupyter/templates/jupyter/build/jupyter/jupyterhub_config.py) you can change, or add more features to the these files. Feel free fork this repository and any idea or PR welcome :)

### JupyterLab:

JupyterLab is great advanced tools for everyone, for more information please visit https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html

To start JupyterLab just click the " Start JupyterLab in new tab " Now all lab ready for every Hub users.

![](/src/JupyterLab.jpg)

Now you can write your entyre course with Jupyter tools :)
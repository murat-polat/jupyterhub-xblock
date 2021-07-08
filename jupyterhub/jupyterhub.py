import logging
import re
import pkg_resources
from xblock.core import XBlock
from xblock.fields import Scope, String, Integer, Boolean
from xblock.fragment import Fragment
from xblock.validation import ValidationMessage
from xblockutils.studio_editable import StudioEditableXBlockMixin
from xblockutils.resources import ResourceLoader


try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


log = logging.getLogger(__name__)


class JupyterhubXBlock(XBlock, StudioEditableXBlockMixin):
   

    display_name = String(
        display_name="Name", default="Jupyterhub",
        scope=Scope.settings,
        help="XBlock name"
    )

    btn_text = String(
        help="Button Text",
        scope=Scope.content,
        display_name="Button Text",
        default="Start JupyterHub in new tab"
    )

  

    jupyterhub_url = String(
        help="Jupyterhub URL",
        display_name="Jupyterhub URL",
        scope=Scope.content,
         ############### Jupyterhub URL ###############
        default= "{{main_url}}"
    )

    notebook_url = String(
        help="JupyterNotebook URL (*.ipynb)",
        display_name="JupyterNotebook URL",
        scope=Scope.content,
         ############### Notebook URL(*.ipynb) ###############
        default="{{main_url}}/user/student/notebooks/demo.ipynb "
    )

    jupyterLab_url = String(
        help="JupyterLab URL",
        display_name="JupyterLab URL",
        scope=Scope.content,
         ############### Notebook URL(*.ipynb) ###############
        default="{{main_url}}/user/hub/lab "
    )

    editable_fields = ('display_name', 'btn_text', 'jupyterhub_url', 'notebook_url', 'jupyterLab_url')

    def resource_string(self, path):
        
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def validate_field_data(self, validation, data):
        
        main_url = data.jupyterhub_url
        if not main_url.startswith('https://') and not main_url.startswith('http://'):
            validation.add(
                ValidationMessage(
                    ValidationMessage.ERROR, 
                    u" Please check your JupyterHub URL, and try it again !"))


    def student_view(self, context=None):
        loader = ResourceLoader('jupyterhub')
        jupyterhub_url = self.jupyterhub_url
        context = dict(
            main_url=jupyterhub_url,
            btn_text=self.btn_text,
            notebook_url=self.notebook_url,
            jupyterLab_url=self.jupyterLab_url
             )
                        
        template = loader.render_django_template(
            'static/html/index.html', context=context)

      
        frag = Fragment(template)
        frag.add_css(self.resource_string('static/css/main.css'))
        return frag

    def main_jupyterhub_url(self, main_url):
        ############### Jupyterhub URL ###############
        main_url = self.main_url
       
        return main_url

    def main_notebook_url(self,notebook_url):
        notebook_url = self.notebook_url
        return notebook_url

    
    def main_jupyterLab_url(self,jupyterLab_url):
        jupyterLab_url = self.jupyterLab_url
        return jupyterLab_url

    
    @staticmethod
    def workbench_scenarios():
        
        return [
            ("JupyterhubXBlock",
             """<jupyterhubxblock/>
             """),
            ("Multiple JupyterhubXBlock",
             """<vertical_demo>
                <jupyterhubxblock/>
                <jupyterhubxblock/>
                <jupyterhubxblock/>
                </vertical_demo>
             """),
        ]

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
        display_name="Name", default="Jupyterhub XBlock",
        scope=Scope.settings,
        help="XBlock name"
    )

    btn_text = String(
        help="Button Text",
        scope=Scope.content,
        display_name="Button Text",
        default="Start JupyterHub"
    )

    description = String(
        help="Optional description",
        scope=Scope.content,
        display_name="description",
        default="",
        multiline_editor='html',
    )

    jupyterhub_url = String(
        help="Jupyterhub url",
        display_name="Notebook URL",
        scope=Scope.content,
        default="{{ JUPYTER_HOST }}"
    )

    editable_fields = ('display_name', 'btn_text', 'jupyterhub_url', 'description')

    def resource_string(self, path):
        
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def validate_field_data(self, validation, data):
        
        main_url = data.jupyterhub_url
        if not main_url.startswith('https://') and not main_url.startswith('http://'):
            validation.add(
                ValidationMessage(
                    ValidationMessage.ERROR, 
                    u" 'http://' or 'https://'"))


    def student_view(self, context=None):
        loader = ResourceLoader('jupyterhub_xblock')
        jupyterhub_url = self._jupyterhub_url(self.jupyterhub_url)
        context = dict(
            main_url=jupyterhub_url,
            btn_text=self.btn_text,
            description=self.description,
        )
                        
        template = loader.render_django_template(
            'static/html/index.html', context=context)

      
        frag = Fragment(template)
        frag.add_css(self.resource_string('static/css/main.css'))
        return frag

    def _jupyterhub_url(self, main_url):
        
        main_url = '{% if ENABLE_HTTPS %}https{% else %}http{% endif %}://{{ JUPYTER_HOST }}'
       
        return main_url

    
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

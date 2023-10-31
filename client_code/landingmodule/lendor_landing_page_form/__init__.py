from ._anvil_designer import lendor_landing_page_formTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import main_form_module

class lendor_landing_page_form(lendor_landing_page_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("landingmodule.user_home")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("landingmodule.main_form")


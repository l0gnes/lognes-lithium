from utils.LithiumCommunityCog import LithiumCommunityCog
from discord import app_commands
from discord import Interaction

class TestCog(LithiumCommunityCog):
  
  def __init__(self, client):
    self.client = client
    
    super().__init__()
    
  @app_commands.command(name="example", description="Hello World!")
  async def test_example_command(self, interaction: Interaction):
    return await interaction.response.send_message("Hello World!")

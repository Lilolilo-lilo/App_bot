from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str = getenv("BOT_TOKEN")
    WEBAPP_URL: str = "https://lilolilo-lilo.github.io/App_bot/index_app.html"
    FIGMA_LINK: str = "https://www.figma.com/proto/T9LISapjTIZdcZfyf6JPCq/Prizo?node-id=1-725&node-type=frame&viewport=979%2C359%2C0.21&t=HG3EDu5frgLhGe7P-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=1%3A725"

config = Config() 
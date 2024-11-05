from dataclasses import dataclass
from environs import Env

@dataclass
class Config:
    token: str
    figma_url: str

def load_config() -> Config:
    env = Env()
    env.read_env()
    
    return Config(
        token=env.str('BOT_TOKEN'),
        figma_url=env.str('FIGMA_PROTOTYPE_URL')
    ) 
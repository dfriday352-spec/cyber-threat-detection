"""Configuration management"""

from pydantic_settings import BaseSettings
from pydantic import BaseModel
from typing import List, Dict, Optional
import yaml
import os


class CORSSettings(BaseModel):
    origins: List[str] = ["*"]
    allow_credentials: bool = True
    allow_methods: List[str] = ["*"]
    allow_headers: List[str] = ["*"]


class APISettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    cors: CORSSettings = CORSSettings()


class DatabaseSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    name: str = "threat_detection"
    user: str = "threat_user"
    password: str = "password"


class RedisSettings(BaseModel):
    host: str = "localhost"
    port: int = 6379


class ThreatDetectionSettings(BaseModel):
    thresholds: Dict[str, float] = {}
    features: Dict[str, any] = {}


class ResponseEngineSettings(BaseModel):
    enabled: bool = True
    actions: Dict = {}
    policies: Dict = {}


class Settings(BaseSettings):
    api: APISettings = APISettings()
    database: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    threat_detection: ThreatDetectionSettings = ThreatDetectionSettings()
    response_engine: ResponseEngineSettings = ResponseEngineSettings()
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Load configuration from YAML
def load_config_from_yaml(config_path: str = "config/config.yaml") -> dict:
    """Load configuration from YAML file"""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}


# Initialize settings
settings = Settings()
config_yaml = load_config_from_yaml()

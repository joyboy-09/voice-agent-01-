"""
Configuration settings for the Voice Agent.
"""

import os
from dataclasses import dataclass, field
from dotenv import load_dotenv


@dataclass
class Config:
    """Configuration for the Voice Agent."""
    
    # Audio settings
    tts_sample_rate: int = 24000          # Kokoro TTS sample rate
    stt_sample_rate: int = 16000          # Whisper expects 16kHz
    record_duration: int = 5              # Seconds to record
    
    # Whisper settings
    whisper_model: str = "base"           # Options: tiny, base, small, medium, large
    whisper_language: str = "en"
    
    # Kokoro TTS settings
    kokoro_voice: str = "af_heart"        # American Female - Heart voice
    kokoro_lang: str = "a"                # 'a' for American English
    
    # LLM settings
    llm_model: str = "sonar"
    llm_temperature: float = 0.1
    
    # System prompt
    system_prompt: str = field(default="""You are a helpful voice assistant. 
Keep your responses concise and conversational since they will be spoken aloud. 
Aim for responses that are 2-3 sentences unless more detail is specifically requested.""")
    
    # API Key (loaded from environment)
    pplx_api_key: str = field(default="", repr=False)
    
    def __post_init__(self):
        """Load environment variables after initialization."""
        load_dotenv()
        self.pplx_api_key = os.getenv("PPLX_API_KEY", "")
    
    def validate(self) -> bool:
        """Validate the configuration."""
        if not self.pplx_api_key:
            raise ValueError(
                "PPLX_API_KEY not found! "
                "Please set it in your .env file or environment variables."
            )
        return True

"""
Voice Agent Package
===================
A streaming voice agent using Kokoro TTS and Perplexity Sonar LLM.
"""

from .agent import VoiceAgent
from .config import Config

__all__ = ["VoiceAgent", "Config"]
__version__ = "0.1.0"

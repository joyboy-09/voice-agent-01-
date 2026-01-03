"""
Text-to-Speech module using Kokoro TTS.
"""

import sounddevice as sd
from kokoro import KPipeline

from .config import Config


class TTSEngine:
    """Kokoro TTS engine for text-to-speech conversion."""
    
    def __init__(self, config: Config):
        """Initialize the TTS engine.
        
        Args:
            config: Configuration object with TTS settings.
        """
        self.config = config
        self.pipeline = None
    
    def load(self) -> None:
        """Load the Kokoro TTS pipeline."""
        print("🔊 Loading Kokoro TTS...")
        try:
            self.pipeline = KPipeline(lang_code=self.config.kokoro_lang)
            print("✅ Kokoro TTS loaded!")
        except Exception as e:
            raise RuntimeError(
                f"Failed to load Kokoro TTS: {e}\n"
                "Make sure espeak-ng is installed!"
            )
    
    def speak(self, text: str) -> None:
        """Convert text to speech and play it.
        
        Args:
            text: The text to speak.
        """
        if not self.pipeline:
            raise RuntimeError("TTS engine not loaded. Call load() first.")
        
        print("🔊 Speaking...")
        
        # Generate and play audio chunks
        generator = self.pipeline(text, voice=self.config.kokoro_voice)
        
        for _, _, audio in generator:
            sd.play(audio, samplerate=self.config.tts_sample_rate)
            sd.wait()
        
        print("✅ Done speaking!")

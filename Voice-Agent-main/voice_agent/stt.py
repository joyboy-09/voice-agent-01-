"""
Speech-to-Text module using OpenAI Whisper.
"""

import numpy as np
import sounddevice as sd
import whisper

from .config import Config


class STTEngine:
    """Whisper-based speech-to-text engine."""
    
    def __init__(self, config: Config):
        """Initialize the STT engine.
        
        Args:
            config: Configuration object with STT settings.
        """
        self.config = config
        self.model = None
    
    def load(self) -> None:
        """Load the Whisper model."""
        print(f"📥 Loading Whisper model ({self.config.whisper_model})...")
        self.model = whisper.load_model(self.config.whisper_model)
        print("✅ Whisper loaded!")
    
    def record(self) -> np.ndarray:
        """Record audio from the microphone.
        
        Returns:
            Audio data as a numpy array.
        """
        print(f"🎤 Recording for {self.config.record_duration} seconds... Speak now!")
        
        audio_data = sd.rec(
            int(self.config.record_duration * self.config.stt_sample_rate),
            samplerate=self.config.stt_sample_rate,
            channels=1,
            dtype=np.float32
        )
        sd.wait()
        
        print("✅ Recording complete!")
        return audio_data.flatten()
    
    def transcribe(self, audio: np.ndarray) -> str:
        """Transcribe audio to text.
        
        Args:
            audio: Audio data as numpy array.
            
        Returns:
            Transcribed text.
        """
        if not self.model:
            raise RuntimeError("STT engine not loaded. Call load() first.")
        
        print("🔄 Transcribing...")
        
        result = self.model.transcribe(
            audio,
            fp16=False,
            language=self.config.whisper_language
        )
        
        text = result["text"].strip()
        print(f"📝 You said: \"{text}\"")
        return text
    
    def listen(self) -> str:
        """Record and transcribe in one step.
        
        Returns:
            Transcribed text from microphone input.
        """
        audio = self.record()
        return self.transcribe(audio)

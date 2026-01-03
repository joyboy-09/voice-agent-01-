"""
Main Voice Agent class that orchestrates all components.
"""

import sys

from .config import Config
from .llm import LLMEngine
from .stt import STTEngine
from .tts import TTSEngine


class VoiceAgent:
    """A streaming voice agent with Kokoro TTS and Perplexity Sonar LLM."""
    
    def __init__(self, config: Config | None = None):
        """Initialize the voice agent.
        
        Args:
            config: Optional configuration object. Uses defaults if not provided.
        """
        self.config = config or Config()
        
        # Initialize engines (not loaded yet)
        self.stt = STTEngine(self.config)
        self.llm = LLMEngine(self.config)
        self.tts = TTSEngine(self.config)
        
        self._initialized = False
    
    def initialize(self) -> None:
        """Load all models and validate configuration."""
        print("🚀 Initializing Voice Agent...")
        
        # Validate configuration
        try:
            self.config.validate()
        except ValueError as e:
            print(f"❌ Configuration Error: {e}")
            sys.exit(1)
        
        # Load all engines
        try:
            self.stt.load()
            self.tts.load()
            self.llm.load()
        except Exception as e:
            print(f"❌ Initialization Error: {e}")
            sys.exit(1)
        
        self._initialized = True
        print("\n✨ Voice Agent initialized successfully!\n")
    
    def process(self, text: str) -> str:
        """Process text input and return spoken response.
        
        Args:
            text: User input text.
            
        Returns:
            The assistant's response.
        """
        if not self._initialized:
            self.initialize()
        
        # Get streaming LLM response
        response = self.llm.get_response(text, print_stream=True)
        
        # Speak the response
        if response:
            self.tts.speak(response)
        
        return response
    
    def listen_and_respond(self) -> str:
        """Listen for voice input and respond.
        
        Returns:
            The assistant's response.
        """
        if not self._initialized:
            self.initialize()
        
        # Listen for voice input
        text = self.stt.listen()
        
        if not text:
            print("❌ Could not understand audio. Please try again.")
            return ""
        
        return self.process(text)
    
    def run(self) -> None:
        """Run the interactive conversation loop."""
        if not self._initialized:
            self.initialize()
        
        print("=" * 50)
        print("🎙️  VOICE AGENT READY")
        print("=" * 50)
        print("Press Enter to start speaking, or type 'quit' to exit.")
        print("=" * 50 + "\n")
        
        while True:
            try:
                user_input = input("Press Enter to speak (or type message, 'quit' to exit): ").strip()
                
                if user_input.lower() == 'quit':
                    print("\n👋 Goodbye!")
                    break
                
                if user_input:
                    # Use typed input
                    print(f"📝 Using typed input: \"{user_input}\"")
                    self.process(user_input)
                else:
                    # Use voice input
                    self.listen_and_respond()
                
                print("-" * 50 + "\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted! Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                continue

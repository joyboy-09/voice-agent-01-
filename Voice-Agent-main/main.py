"""
Voice Agent with Kokoro TTS and Perplexity Sonar LLM
=====================================================

A streaming voice agent that:
1. Listens for voice input via microphone (using Whisper for STT)
2. Processes the input through Perplexity Sonar LLM with streaming
3. Speaks the response using Kokoro TTS

Usage:
    poetry run python main.py

Requirements:
    - espeak-ng must be installed for Kokoro TTS
    - PPLX_API_KEY environment variable must be set
"""

from voice_agent import VoiceAgent, Config


def main():
    """Main entry point."""
    print("\n" + "=" * 50)
    print("  🗣️  Voice Agent with Kokoro TTS & Perplexity Sonar")
    print("=" * 50 + "\n")
    
    # Create configuration (uses defaults + env variables)
    config = Config()
    
    # Create and run the voice agent
    agent = VoiceAgent(config)
    agent.run()


if __name__ == "__main__":
    main()

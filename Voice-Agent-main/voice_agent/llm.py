"""
LLM module using Perplexity Sonar via LangChain.
"""

from typing import Generator

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_perplexity import ChatPerplexity

from .config import Config


class LLMEngine:
    """Perplexity Sonar LLM engine with streaming support."""
    
    def __init__(self, config: Config):
        """Initialize the LLM engine.
        
        Args:
            config: Configuration object with LLM settings.
        """
        self.config = config
        self.llm = None
        self.system_message = SystemMessage(content=config.system_prompt)
    
    def load(self) -> None:
        """Initialize the LLM client."""
        print("🤖 Initializing Perplexity Sonar LLM...")
        
        self.llm = ChatPerplexity(
            temperature=self.config.llm_temperature,
            model=self.config.llm_model,
            pplx_api_key=self.config.pplx_api_key,
            streaming=True
        )
        
        print("✅ Perplexity Sonar ready!")
    
    def stream(self, user_input: str) -> Generator[str, None, None]:
        """Stream a response for the given input.
        
        Args:
            user_input: The user's message.
            
        Yields:
            Chunks of the response as they arrive.
        """
        if not self.llm:
            raise RuntimeError("LLM engine not loaded. Call load() first.")
        
        messages = [
            self.system_message,
            HumanMessage(content=user_input)
        ]
        
        for chunk in self.llm.stream(messages):
            if chunk.content:
                yield chunk.content
    
    def get_response(self, user_input: str, print_stream: bool = True) -> str:
        """Get a complete response, optionally printing as it streams.
        
        Args:
            user_input: The user's message.
            print_stream: Whether to print chunks as they arrive.
            
        Returns:
            The complete response text.
        """
        print("🤔 Thinking...")
        
        if print_stream:
            print("💬 Assistant: ", end="", flush=True)
        
        full_response = ""
        for chunk in self.stream(user_input):
            if print_stream:
                print(chunk, end="", flush=True)
            full_response += chunk
        
        if print_stream:
            print("\n")
        
        return full_response

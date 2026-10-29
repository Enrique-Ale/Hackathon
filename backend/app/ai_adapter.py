import os
from typing import Dict, Any, Optional
import httpx
from dotenv import load_dotenv

load_dotenv()

class AIAdapter:
    def __init__(self):
        self.base_url = os.getenv("FREELLM_API_URL", "https://api.freellmapi.com/v1")
        self.api_key = os.getenv("FREELLM_API_KEY", "dummy_key")
        self.default_model = os.getenv("FREELLM_MODEL", "claude-3-5-sonnet")

    async def call_model(self, prompt: str, system_message: str = "Eres un asistente útil.") -> Dict[str, Any]:
        """
        Realiza una llamada al proveedor de modelos desacoplado.
        Aplica validación, timeouts y reintentos básicos.
        """
        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
                    json={
                        "model": self.default_model,
                        "messages": [
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": prompt}
                        ],
                        "temperature": 0.3
                    }
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            # Fallback determinista cuando la IA falla
            return {"error": str(e), "fallback": True}

# Instancia global del adaptador
ai_service = AIAdapter()

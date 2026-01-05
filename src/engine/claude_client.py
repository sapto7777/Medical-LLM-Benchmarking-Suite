import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

class ClaudeMedicalClient:
    def __init__(self, model_id):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model_id = model_id

    def get_clinical_response(self, prompt):
        """Invoke Claude with system instructions for medical safety."""
        message = self.client.messages.create(
            model=self.model_id,
            max_tokens=1024,
            system="You are a clinical evaluation assistant. Provide evidence-based answers only.",
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

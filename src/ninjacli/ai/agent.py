import re
from openai import OpenAI
from dotenv import load_dotenv
from ninjacli.utils.validators import OutputFormat
from ninjacli.core.message_history import message_history
from pydantic import ValidationError

load_dotenv()

def extract_json(text: str) -> str | None:
    """
    Extracts the first valid JSON object from AI output.
    Handles non-greedy {} and removes ```json``` blocks if present.
    """
    text = re.sub(r"```json|```", "", text, flags=re.IGNORECASE).strip()

    match = re.search(r"\{.*?\}", text, re.DOTALL)
    return match.group(0) if match else None


def agent(ai_option: str, user_input: str):
    """
    Main AI agent loop.
    Yields OutputFormat objects for Ninja CLI to process each step.
    """
    model = None
    api_base_url = None

    if ai_option == "openai":
        model = "gpt-4o"
    elif ai_option == "gemini":
        model = "gemini-3-flash-preview"
        api_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    elif ai_option == "openrouter":
        model = "xiaomi/mimo-v2-flash:free"
        api_base_url = "https://openrouter.ai/api/v1"

    client = OpenAI(base_url=api_base_url)

    message_history.append({"role": "user", "content": user_input})

    task_completed = False

    while not task_completed:
        response = client.chat.completions.create(
            model=model,
            messages=message_history
        )

        raw = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw})

        json_text = extract_json(raw)

        try:
            if json_text:
                parsed = OutputFormat.model_validate_json(json_text)
            else:
                parsed = OutputFormat(step="OUTPUT", content=raw)
        except ValidationError:
            parsed = OutputFormat(
                step="ERROR",
                content=f"Invalid JSON from AI.\nRaw output:\n{raw}"
            )

        yield parsed

        if parsed.step == "OUTPUT":
            task_completed = True

import json, os, re
from openai import OpenAI
from dotenv import load_dotenv
from ninjacli.utils.validators import OutputFormat
from ninjacli.core.message_history import message_history
from ninjacli.cli.tools import available_tools
from ninjacli.cli.commands import EXIT_COMMANDS
from pydantic import ValidationError

load_dotenv()
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

client = OpenAI(base_url=OPENROUTER_BASE_URL)

def extract_json(text: str) -> str | None:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None


def agent(user_input: str):
    message_history.append({"role": "user", "content": user_input})

    task_completed = False

    while not task_completed:
        response = client.chat.completions.create(
            model="xiaomi/mimo-v2-flash:free",
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
                content="Invalid JSON from AI"
            )

        yield parsed

        if parsed.step == "OUTPUT":
            task_completed = True

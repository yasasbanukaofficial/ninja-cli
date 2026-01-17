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

def agent():
    while True:
        user_input = input(">: ")
        message_history.append({"role": "user", "content": user_input})
        
        if user_input.strip().lower() in EXIT_COMMANDS:
            print("Exiting terminal...")
            break
        
        task_completed = False
        
        while not task_completed:
            response = client.chat.completions.create(
                model="xiaomi/mimo-v2-flash:free",
                messages=message_history
            )
            
            raw_result = response.choices[0].message.content
            message_history.append({"role": "assistant", "content": raw_result})
            
            json_text = extract_json(raw_result)
            
            try:
                if json_text:
                    parsed_result = OutputFormat.model_validate_json(json_text)
                else:
                    raise ValidationError("No JSON found")
            except ValidationError:
                parsed_result = OutputFormat(
                    step="ERROR",
                    content='The AI issued content outside of the JSON structure'
                )
            except Exception:
                parsed_result = OutputFormat(step="OUTPUT", content=raw_result)
            
            if parsed_result.step == "START":
                print("🔥: ", parsed_result.content)
                continue
            elif parsed_result.step == "PLAN":
                print("🧠: ", parsed_result.content)
                continue
            elif parsed_result.step == "TOOL":
                tool_to_call = parsed_result.tool
                tool_input = parsed_result.input
                print(f"🔧: Calling tool -> {tool_to_call}({tool_input})")
                
                tool_response = available_tools[tool_to_call](tool_input)
                print(f"🔧: {tool_to_call}({tool_input}) = {tool_response}")
                message_history.append({"role": "assistant", "content": json.dumps(
                    {"step": "OBSERVE", "input": tool_input, "output": tool_response}
                )})
                continue
            elif parsed_result.step == "ERROR":
                print("⛔: ", parsed_result.content)
                continue
            elif parsed_result.step == "OUTPUT":
                print("🤖: ", parsed_result.content)
                task_completed = True
            
        print("\n")

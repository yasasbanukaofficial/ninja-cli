import json
from openai import OpenAI
from dotenv import load_dotenv
from utils.validators import OutputFormat
from core.message_history import message_history
from cli.tools import available_tools

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
)

while True:
    user_input = input(">: ")
    message_history.append({"role": "user", "content": user_input})
    
    while True:
        response = client.chat.completions.parse(
            model="xiaomi/mimo-v2-flash:free",
            response_format=OutputFormat,
            messages=message_history
        )
    
        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        parsed_result = response.choices[0].message.parsed
        
        if parsed_result.step == "START":
            print("🔥: ", parsed_result.content)
            continue
        if parsed_result.step == "PLAN":
            print("🧠: ", parsed_result.content)
            continue
        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"🔧: Calling tool -> {tool_to_call}({tool_input})")
            
            tool_response = available_tools[tool_to_call](tool_input)
            print(f"🔧: {tool_to_call}({tool_input}) = {tool_response}")
            message_history.append({"role": "assistant", "content": json.dumps(
                {"step": "OBSERVE", "input": tool_input, "output": tool_response}
            )})
        
        if parsed_result.step == "OUTPUT":
            print(f"🪄: ", parsed_result.content)
            break
        
    print("\n\n")
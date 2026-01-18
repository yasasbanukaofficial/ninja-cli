import os, json
from dotenv import load_dotenv
from ninjacli.ai.agent import agent
from ninjacli.ui.intro import header_display, prompt_display, api_option_display
from ninjacli.cli.tools import available_tools, file_exists
from ninjacli.core.message_history import message_history
from ninjacli.utils.api_management import is_api_saved
from ninjacli.cli.commands import EXIT_COMMANDS

load_dotenv()

def main():
    header_display()
    if not file_exists(".halo"):
        user_option = api_option_display()
        ai_option = user_option[0]
        api_key = user_option[1]
        api_saved = is_api_saved(ai_option, api_key)
    
        if not api_saved:
            print("API_NOT_SAVED")
    else:
        saved_ai_option = os.getenv("API_OPTION")

    while True:
        user_input = prompt_display()

        if user_input.strip().lower() in EXIT_COMMANDS:
            print("👋 Exiting Ninja CLI")
            break

        for step in agent(saved_ai_option, user_input):
            if step.step == "START":
                print("🔥:", step.content)
            elif step.step == "PLAN":
                print("🧠:", step.content)
            elif step.step == "TOOL":
                tool = step.tool
                tool_input = step.input
                print(f"🔧 Calling {tool}({tool_input})")
                result = available_tools[tool](tool_input)
                message_history.append({
                    "role": "assistant",
                    "content": json.dumps({
                        "step": "OBSERVE",
                        "input": tool_input,
                        "output": result
                    })
                })
            elif step.step == "ERROR":
                print("⛔:", step.content)
            elif step.step == "OUTPUT":
                print("🤖:", step.content)
                break

if __name__ == "__main__":
    main()
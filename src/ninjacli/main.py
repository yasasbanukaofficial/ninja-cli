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
    if not file_exists("../.env"):
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

        message_history.append({"role": "user", "content": user_input})
        
        task_in_progress = True
        while task_in_progress:
            for step in agent(saved_ai_option, message_history):
                message_history.append({"role": "assistant", "content": json.dumps(step.model_dump())})
                if step.step == "PLAN":
                    print("🧠:", step.content)
                elif step.step == "TOOL":
                    tool_name = step.tool
                    tool_input = step.input
                    print(f"🔧 Calling {tool_name}({tool_input})")
                    if tool_name in available_tools:
                        result = available_tools[tool_name](tool_input)
                        message_history.append({
                            "role": "assistant",
                            "content": json.dumps({
                                "step": "OBSERVE",
                                "tool": tool_name,
                                "input": tool_input,
                                "output": result
                            })
                        })
                    else:
                        message_history.append({
                            "role": "assistant",
                            "content": json.dumps({
                                "step": "OBSERVE",
                                "tool": tool_name,
                                "input": tool_input,
                                "output": f"Error: Tool '{tool_name}' not found."
                            })
                        })
                elif step.step == "ERROR":
                    print("⛔:", step.content)
                    task_in_progress = False
                elif step.step == "OUTPUT":
                    print("🤖:", step.content)
                    task_in_progress = False
                else:
                    print(step)

if __name__ == "__main__":
    main()
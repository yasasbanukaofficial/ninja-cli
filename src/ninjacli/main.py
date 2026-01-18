import json
from ninjacli.ai.agent import agent
from ninjacli.ui.intro import header_display, prompt_display, api_option_display
from ninjacli.cli.tools import available_tools
from ninjacli.core.message_history import message_history
from ninjacli.cli.commands import EXIT_COMMANDS

def main():
    header_display()
    api_key = api_option_display()

    while True:
        user_input = prompt_display()

        if user_input.strip().lower() in EXIT_COMMANDS:
            print("👋 Exiting Ninja CLI")
            break

        for step in agent(user_input):
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

if __name__ == "__main__":
    main()
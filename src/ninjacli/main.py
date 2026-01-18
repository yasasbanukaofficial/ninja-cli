from ninjacli.ai.agent import agent
from ninjacli.ui.intro import header_display, prompt_display, api_option_display

def main():
    header_display()
    user_api_key = api_option_display()
    agent(user_api_key)

if __name__ == "__main__":
    main()
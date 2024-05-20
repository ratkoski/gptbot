import openai
import sys

tokens_count = 0
if len(sys.argv) == 3:
    # Assign the arguments to variables
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    openai.api_key = arg1
    gpt_name = arg2
else:
    # Print an error message if the number of arguments is not 3
    print("Error: Exactly two arguments are required.")
    sys.exit(1)  # Exit the script with an error status (1)
messages = [{"role": "system", "content": "Intelligent assistant." }]
print(f"Hi i'm {gpt_name}, how can i help you?")
try:
    while True:
        message = input("You: ")
        
        if message:
            messages.append({"role": "user", "content": message})
            chat = openai.chat.completions.create(
            model = "gpt-3.5-turbo", messages=messages, temperature=0.5
            )
            print(chat)
            tokens_count = tokens_count + chat.usage.total_tokens
            reply = chat.choices[0].message.content
            print(f"{gpt_name}: {reply}")
except (KeyboardInterrupt, EOFError):
    print("\nBye!")
    print("Tokens used: {tokens_count}")
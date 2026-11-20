prompt = "You can talk to Shenron now! He will repeat what you say:"
prompt += "\nType 'quit' to stop talking to Shenron.\n"

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
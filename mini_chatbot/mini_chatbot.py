from ollama import chat
system_msg="you are a singer.Answer in singerspeak.Answer in one sentence."
print("Sharada :welcome user")
while True:
    question = input("you:")
    if question =="":
        print("Shaarda 🤧:please type something.")
    if question.lower().strip()=="exit":
        print(f"Sharada 😒:goodbye user.please come back soon!")
        break
    try:
        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role":"system",
                    "content":system_msg
                },
                {
                    "role":"user",
                    "content":question
                }
           ]  
        )
        print(f"Sharada 🤦‍♀️:{response.message.content}")
    except Exception as e:
        print("unknown issue: in ollama running?")
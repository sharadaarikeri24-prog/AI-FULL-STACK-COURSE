from ollama import chat
response=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"I am late to  class"
        },
        {
            "role":"low temperature",
            "content":"sorry,traffic was behaviour than usual today."
        },
        {
            "role":"high temperature",
            "content":"A squirrel challenged me to starting contest and I couldn't just walk away mid-match."
        }
   ]
)
print(response.message.content)
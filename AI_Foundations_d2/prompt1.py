from ollama import chat
response = chat(
    model= "llama3.2",
    messages={
        {
            "role":"user",
            "content":"Write me a whatsapp messsage to my friend saisri asking her to meet me at the bus stop.keep the answer under 2 lines."
        }
    }
)
print(response.message.content)
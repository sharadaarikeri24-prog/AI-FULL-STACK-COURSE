from ollama import chat

system_msg = "You are a mom. Give me answers how our mom speaks in one line"

history = [{"role": "system", "content": system_msg}]

print("Welcome to CandyyBot❤️")

while True:
    question = input("You: ")

    if question.strip() == "":
        print("Candyy🐶: Ask something!!")
        continue

    if question.lower().strip() == "/history":
        print("---- Your Conversation so far ----")

        if len(history) < 2:
            print("Nothing so far!!")

        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Candyy🐶"

            print(f"{speaker} : {msg['content']}")

        print("-----------------")
        print()
        continue

    if question.lower().strip() == "/clear":
        history = [{"role": "system", "content": system_msg}]
        print("Your history is cleared. Start a fresh conversation.")
        print()
        continue

    if question.lower().strip() == "exit":
        print("Candyy🐶: Byeee Bangarammmmm 🐷😭")
        break

    # Personality command
    if question.lower().strip() == "/personality":

        new_personality = input("You type the personality: ")

        system_msg = new_personality

        # Start a fresh conversation with the new personality
        history = [
            {"role": "system", "content": system_msg}
        ]

        print("Candyy🐶: Personality changed successfully! ❤️")
        print("Candyy🐶: Starting a fresh conversation...")
        print()
        continue

    history.append({"role": "user", "content": question})

    try:
        response = chat(
            model="llama3.2",
            messages=history
        )

        reply = response.message.content

        history.append({
            "role": "assistant",
            "content": reply
        })

        print(f"Candyy🐶: {reply}")
        print()

    except Exception as e:
        print("Unknown issue. Is Ollama running?")
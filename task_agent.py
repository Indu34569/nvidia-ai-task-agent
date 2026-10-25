import os
from datetime import datetime
from openai import OpenAI

MODEL = "openai/gpt-oss-20b"
HISTORY_FILE = "task_history.txt"

client = OpenAI(
    api_key=os.environ["NVIDIA_API_KEY"],
    base_url="https://integrate.api.nvidia.com/v1",
    timeout=180.0,
)

SYSTEM_PROMPT = """
You are a helpful AI task agent.

For every user request:
1. Understand what the user wants.
2. Give a practical, concise answer.
3. If it is a study request, give a structured study plan.
4. If it is an email/message request, provide ready-to-use text.
5. If it is a coding request, provide working code and brief instructions.
6. If it is a project/hackathon request, give clear steps and an MVP.
7. Use headings and numbered lists when helpful.
8. Do not invent personal information.
9. Keep answers focused and beginner-friendly.
"""


def save_task(task, answer):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n[{timestamp}]\n")
        file.write(f"Task: {task}\n")
        file.write(f"Answer: {answer}\n")
        file.write("-" * 60 + "\n")


def show_history():
    print("\n========== TASK HISTORY ==========")

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = file.read().strip()

        if history:
            print(history)
        else:
            print("No previous tasks yet.")

    except FileNotFoundError:
        print("No previous tasks yet.")

    print("==================================\n")


def ask_ai(task):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": task},
            ],
            max_tokens=1000,
        )

        answer = response.choices[0].message.content

        if not answer:
            return "The AI returned an empty response."

        return answer.strip()

    except Exception as error:
        return f"AI request failed: {error}"


def main():
    print("=== NVIDIA AI TASK AGENT ===")
    print(f"Model: nvidia/{MODEL}")
    print("Commands: history | exit | quit")
    print("--------------------------------")

    while True:
        try:
            task = input("\nWhat do you need help with? ").strip()

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

        except EOFError:
            print("\nGoodbye!")
            break

        if not task:
            print("Please enter a task.")
            continue

        if task.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if task.lower() in ["history", "previous"]:
            show_history()
            continue

        print("\nThinking...\n")

        answer = ask_ai(task)

        print(answer)

        save_task(task, answer)


if __name__ == "__main__":
    main()

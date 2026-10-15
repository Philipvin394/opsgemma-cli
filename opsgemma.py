import sys
import ollama

# 1. Get the prompt typed by the user in the command line
if len(sys.argv) < 2:
    print("❌ Usage: python3 opsgemma.py \"<your question here>\"")
    print(
        "💡 Example: python3 opsgemma.py \"How do I list files in Linux with details?\""
    )
    sys.exit(1)

user_query = " ".join(sys.argv[1:])

# 2. System prompt: Teaches Gemma how to act as a Linux/AWS/Git assistant
system_instruction = (
    "You are OpsGemma, a precise command-line assistant for Linux, Git, and AWS CLI. "
    "Provide official, strictly accurate terminal syntax. "
    "Return the exact command first, followed by a 1-sentence explanation."
)

print("\n🚀 OpsGemma is thinking...\n")

try:
    # 3. Send the prompt to the local Gemma model via Ollama
    response = ollama.chat(
        model="gemma2:2b",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_query},
        ],
    )

    # 4. Print the output
    print("----------------------------------------")
    print(response["message"]["content"])
    print("----------------------------------------\n")

except Exception as e:
    print(f"❌ Error communicating with Ollama: {e}")
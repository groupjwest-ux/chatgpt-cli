import sys
import json
from openai import OpenAI

client = OpenAI()

def handle_request(req):
    response = client.chat.completions.create(
        model=req.get("model", "gpt-4.1-mini"),
        messages=req["messages"],
        temperature=req.get("temperature", 0.7),
    )

    return {
        "reply": response.choices[0].message.content
    }

def main():
    for line in sys.stdin:
        if not line.strip():
            continue

        req = json.loads(line)
        res = handle_request(req)

        print(json.dumps(res), flush=True)

if __name__ == "__main__":
    main()


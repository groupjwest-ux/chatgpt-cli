import subprocess
import json
import sys

class ChatBridge:
    def __init__(self):
        self.proc = subprocess.Popen(
            ["python3", "python/chatgpt_client.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        self.history = []

    def handle(self, request):
        if "reset" in request and request["reset"]:
            self.history = []
            return {"status": "ok"}

        if "message" in request:
            self.history.append({
                "role": "user",
                "content": request["message"]
            })

        payload = {
            "messages": self.history,
            "model": request.get("model", "gpt-4.1-mini"),
            "temperature": request.get("temperature", 0.7)
        }

        self.proc.stdin.write(json.dumps(payload) + "\n")
        self.proc.stdin.flush()

        reply = json.loads(self.proc.stdout.readline())
        self.history.append({
            "role": "assistant",
            "content": reply["reply"]
        })

        return reply

def main():
    bridge = ChatBridge()

    for line in sys.stdin:
        if not line.strip():
            continue

        req = json.loads(line)
        res = bridge.handle(req)

        print(json.dumps(res), flush=True)

if __name__ == "__main__":
    main()


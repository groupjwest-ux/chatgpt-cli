import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess
import json

class ChatApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="ChatGPT GTK")
        self.set_default_size(600, 400)

        self.proc = subprocess.Popen(
            ["python3", "../python/chatgpt_client.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        self.view = Gtk.TextView()
        self.buffer = self.view.get_buffer()
        box.pack_start(self.view, True, True, 0)

        self.entry = Gtk.Entry()
        self.entry.connect("activate", self.send)
        box.pack_start(self.entry, False, False, 0)

    def send(self, widget):
        text = self.entry.get_text()
        self.entry.set_text("")

        req = {
            "messages": [{"role": "user", "content": text}]
        }

        self.proc.stdin.write(json.dumps(req) + "\n")
        self.proc.stdin.flush()
        self.proc = subprocess.Popen(
    ["python3", "../python/bridge.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

        reply = json.loads(self.proc.stdout.readline())["reply"]
        self.buffer.insert(self.buffer.get_end_iter(), f"\n> {text}\n{reply}\n")

win = ChatApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


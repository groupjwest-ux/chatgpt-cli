This ChatGPT CLI & GTK Client

A modular, desktop-grade ChatGPT client built with C++, Python, and GTK, designed around a clean IPC architecture using JSON over stdin/stdout.

This project provides:

a fast native CLI

an optional GTK UI

a shared Python backend that handles OpenAI API communication

a fully self-contained build (no external C++ deps)

Features

Native C++ command-line interface

GTK desktop application (Glade-based UI)

Python IPC bridge with persistent conversation state

Header-only JSON (nlohmann/json, vendored)

Single backend shared by CLI and GUI

Portable install layout (Flatpak/AppImage friendly)

Clean separation of UI, logic, and API access



Architecture Overview

C++ CLI / GTK UI
        │
        ▼
   python/bridge.py
        │
        ▼
python/chatgpt_client.py
        │
        ▼
     OpenAI API

All communication is done using newline-delimited JSON over standard input/output.



Directory Layout
chatgpt-cli
chatgpt-cli_source/
├── core/                # C++ CLI + core logic
│   ├── main.cpp
│   ├── chat_engine.cpp
│   ├── chat_engine.h
│   └── json.hpp         # vendored nlohmann/json
├── python/              # backend services
│   ├── chatgpt_client.py
│   └── bridge.py
├── gtk/                 # GTK UI
│   ├── app.py
│   └── ui.glade
├── CMakeLists.txt
└── README.md

Requirements

Build

CMake ≥ 3.16
C++17 compiler (GCC / Clang)
Python 3.9+

Runtime

Python packages:
openai
PyGObject (for GTK UI)
GTK 3.x

Building

mkdir build
cd build
cmake ..
make

Installation

sudo make install



Default install paths:

CLI binary → /usr/bin/chatgpt-cli

Python backend → /usr/share/chatgpt-cli/python

GTK assets → /usr/share/chatgpt-cli/gtk

Running

CLI

chatgpt-cli

GTK UI

python3 /usr/share/chatgpt-cli/gtk/app.py



Environment Variables

Set your OpenAI key before running:

export OPENAI_API_KEY="your-api-key-here"



Design Notes

C++ handles user interaction, history management, and performance-sensitive logic

Python handles API communication and JSON marshaling

GTK UI is layout-only (Glade), with logic kept in Python

No C++ third-party libraries beyond a single vendored header

IPC design allows:

streaming responses

alternate LLM backends

local/offline model substitution

headless or kiosk deployments

Future Extensions

Streaming token output

ncurses TUI

GTK4 + Libadwaita port

Local LLM fallback (GGML / llama.cpp)

Flatpak / AppImage packaging

Conversation persistence

Prompt templates and profiles


License

Project code: MIT

json.hpp: MIT (nlohmann/json)

GTK and Python dependencies retain their respective licenses



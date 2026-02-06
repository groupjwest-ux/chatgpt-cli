cmake_minimum_required(VERSION 3.16)
project(chatgpt_system LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ---------- C++ CLI ----------
add_executable(chatgpt-cli
    core/main.cpp
    core/chat_engine.cpp
)

target_include_directories(chatgpt-cli PRIVATE core)

# ---------- Install Layout ----------
install(TARGETS chatgpt-cli DESTINATION bin)

install(PROGRAMS
    python/chatgpt_client.py
    python/bridge.py
    DESTINATION share/chatgpt-cli/python
)

install(FILES
    gtk/ui.glade
    DESTINATION share/chatgpt-cli/gtk
)

install(PROGRAMS
    gtk/app.py
    DESTINATION bin
)

# ---------- Notes ----------
# Run CLI:
#   chatgpt-cli
#
# Run GTK:
#   python3 /usr/share/chatgpt-cli/gtk/app.py


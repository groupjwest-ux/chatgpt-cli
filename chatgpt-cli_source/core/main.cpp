#include "chat_engine.h"
#include <iostream>

int main() {
    ChatEngine chat;
    std::string input;

    std::cout << "ChatGPT CLI (type 'exit' to quit)\n";

    while (true) {
        std::cout << "\n> ";
        std::getline(std::cin, input);

        if (input == "exit") break;

        std::string reply = chat.send(input);
        std::cout << "\n" << reply << "\n";
    }
}


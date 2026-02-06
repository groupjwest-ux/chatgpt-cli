#pragma once
#include <string>
#include <vector>

struct Message {
    std::string role;
    std::string content;
};

class ChatEngine {
public:
    ChatEngine();
    std::string send(const std::string& user_input);

private:
    std::vector<Message> history;
    FILE* python;
};


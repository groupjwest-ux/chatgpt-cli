#include "chat_engine.h"
#include <cstdio>
#include <iostream>
#include <sstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

ChatEngine::ChatEngine() {
    python = popen("python3 python/chatgpt_client.py", "w+");
}

std::string ChatEngine::send(const std::string& user_input) {
    history.push_back({"user", user_input});

    json req;
    req["messages"] = json::array();
    for (auto& m : history) {
        req["messages"].push_back({
            {"role", m.role},
            {"content", m.content}
        });
    }

    fprintf(python, "%s\n", req.dump().c_str());
    fflush(python);

    char buffer[8192];
    fgets(buffer, sizeof(buffer), python);

    json res = json::parse(buffer);
    std::string reply = res["reply"];

    history.push_back({"assistant", reply});
    return reply;
}


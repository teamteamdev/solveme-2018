#include <iostream>

size_t chars[] = {
    102, 108, 97, 103, 55, 95, 101, 97, 115, 121, 95, 98, 105, 110, 97, 114, 121, 95, 116, 97, 115, 107
};

int main() {
    std::cout << "WOW! You've solved it, congratulations!" << std::endl;
    for (auto& item: chars) {
        std::cout << static_cast<char>(item);
    }
    std::cout << std::endl;
    return 0;
}

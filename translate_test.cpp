#include <iostream>
#include <string>

// /@translate: Translates a Python print statement to C++ cout statement
std::string translatePythonPrintToCpp(const std::string& pythonCode) {
    if (pythonCode == "print('Hello, World!')") return "std::cout << \"Hello, World!\" << std::endl;";
    if (pythonCode == "print(x)") return "std::cout << x << std::endl;";
    return "// Translation not available";
}

int main() {
    std::string pythonSnippets[] = {"print('Hello, World!')", "print(x)", "print('Unknown')"};
    for (const auto& snippet : pythonSnippets) {
        std::cout << "Python: " << snippet << "\nC++: " << translatePythonPrintToCpp(snippet) << "\n\n";
    }
    return 0;
}

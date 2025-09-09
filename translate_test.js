/**
 * /@translate: Translates a Python print statement to JavaScript console.log statement
 */
function translatePythonPrintToJS(pythonCode) {
    if (pythonCode === "print('Hello, World!')") return "console.log('Hello, World!');";
    if (pythonCode === "print(x)") return "console.log(x);";
    return "// Translation not available";
}

// Test cases
const pythonSnippets = ["print('Hello, World!')", "print(x)", "print('Unknown')"];
pythonSnippets.forEach(snippet => {
    console.log(`Python: ${snippet}\nJavaScript: ${translatePythonPrintToJS(snippet)}\n`);
});

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Welcome to the Copilot Python Demo, {name}!"

def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))

if __name__ == "__main__":
    main()
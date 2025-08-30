def main():
    history = []
    while True:
        action = input("Action: ")

        if action == "undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "quit":
            history.clear()
            print("History cleared.")   
            break
        else:
            history.append(action)  # Add the action to the history
        print(history)      # Print the current history

main()

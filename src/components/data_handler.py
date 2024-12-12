class DataHandler:
    """Class to handle data history from chatbot."""

    def __init__(self, history):
        self.history = history

    def get_history(self):
        """Get the history of the chatbot."""
        return self.history

    def save_history(self):
        """Save the history of the chatbot."""
        with open("history.txt", "w") as f:
            for item in self.history:
                f.write(f"{item['role']}: {item['parts'][0]}\n")

    def load_history(self):
        """Load the history of the chatbot from file."""
        try:
            with open("history.txt", "r") as f:
                lines = f.readlines()
                history = []
                for line in lines:
                    role, text = line.strip().split(": ", 1)
                    history.append({"role": role, "parts": [text]})
                self.history = history
        except FileNotFoundError:
            pass

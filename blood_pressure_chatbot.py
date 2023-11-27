import tkinter as tk
from tkinter import scrolledtext

class BloodPressureChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Blood Pressure Chatbot")

        # Set the background color to a soothing color
        master.configure(bg="#87CEEB")  # Sky Blue

        # Create widgets
        self.label = tk.Label(master, text="Enter your blood pressure (mmHg):", bg="#87CEEB", fg="white", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.input_entry = tk.Entry(master, font=("Helvetica", 12))
        self.input_entry.pack(pady=10)

        self.output_text = scrolledtext.ScrolledText(master, width=40, height=10, bg="white", font=("Helvetica", 12))
        self.output_text.pack(pady=10)

        self.button = tk.Button(master, text="Get Recommendation", command=self.get_recommendation, bg="#32CD32", fg="white", font=("Helvetica", 12))
        self.button.pack(pady=10)

    def get_recommendation(self):
        # Get the user's input
        user_input = self.input_entry.get()

        try:
            # Convert input to integer
            blood_pressure = int(user_input)

            # Provide a more detailed recommendation
            if blood_pressure < 90:
                recommendation = "Low blood pressure. It's essential to stay hydrated and consume a balanced diet. If symptoms persist, consult a healthcare professional."
            elif 90 <= blood_pressure <= 120:
                recommendation = "Normal blood pressure. Keep up the good work! Maintain a healthy lifestyle with regular exercise and a balanced diet."
            elif 121 <= blood_pressure <= 139:
                recommendation = "Prehypertension. Consider reducing salt intake, increasing physical activity, and managing stress. Regular monitoring is crucial."
            elif 140 <= blood_pressure <= 159:
                recommendation = "Stage 1 hypertension. Focus on lifestyle changes, including a heart-healthy diet, exercise, and stress management. Consult with a healthcare professional."
            else:
                recommendation = "Stage 2 hypertension. Seek immediate medical attention! Follow medical advice, take prescribed medications, and make significant lifestyle changes."

            # Display the recommendation in the output text area
            self.output_text.insert(tk.END, f"Your blood pressure is {blood_pressure} mmHg.\n")
            self.output_text.insert(tk.END, f"Recommendation: {recommendation}\n")
            self.output_text.insert(tk.END, "\n")

        except ValueError:
            # Handle invalid input
            self.output_text.insert(tk.END, "Invalid input. Please enter a valid blood pressure.\n")
            self.output_text.insert(tk.END, "\n")

        # Clear the input entry
        self.input_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Instantiate the chatbot
chatbot = BloodPressureChatbot(root)

# Run the application
root.mainloop()


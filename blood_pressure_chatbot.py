import tkinter as tk
from tkinter import scrolledtext

class BloodPressureChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Blood Pressure Chatbot")

        # Set the background color to red
        master.configure(bg="red")

        # Create widgets
        self.label = tk.Label(master, text="Enter your blood pressure (mmHg):", bg="red", fg="white")
        self.label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.output_text = scrolledtext.ScrolledText(master, width=40, height=10, bg="white")
        self.output_text.pack()

        self.button = tk.Button(master, text="Get Recommendation", command=self.get_recommendation, bg="white")
        self.button.pack()

    def get_recommendation(self):
        # Get the user's input
        user_input = self.input_entry.get()

        try:
            # Convert input to integer
            blood_pressure = int(user_input)

            # Provide a simple recommendation
            if blood_pressure < 90:
                recommendation = "Low blood pressure. Please consult with a healthcare professional."
            elif 90 <= blood_pressure <= 120:
                recommendation = "Normal blood pressure. Keep up the good work!"
            elif 121 <= blood_pressure <= 139:
                recommendation = "Prehypertension. Consider lifestyle changes and monitor regularly."
            elif 140 <= blood_pressure <= 159:
                recommendation = "Stage 1 hypertension. Consult with a healthcare professional."
            else:
                recommendation = "Stage 2 hypertension. Seek immediate medical attention!"

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

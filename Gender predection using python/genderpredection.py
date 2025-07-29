import tkinter as tk
from tkinter import ttk

def predict_gender(name):
    name = name.lower() 

    boys_names = ["john", "william", "james", "michael", "david", "richard", "joseph", "charles", "thomas",
                  "christopher", "daniel", "matthew", "anthony", "mark", "paul", "steven", "andrew", "kenneth",
                  "george", "jose", "donald", "robert", "brian", "edward", "ronald", "timothy", "gary", "steve",
                  "frank", "dennis", "peter", "raymond", "walter", "harry", "arthur", "jerry", "lawrence", "ralph",
                  "eugene", "samuel", "patrick", "henry", "alfred", "philip", "carl", "roy", "norman", "leroy",
                  "frederick", "louis", "joe", "milton", "clarence", "jack", "ray", "homer", "earl", "ernest",
                  "bernard", "clifford", "leonard", "marvin", "gerald", "adam", "vince", "wayne", "martin", "leo",
                  "floyd", "jimmy", "jackson", "duane", "neil", "max", "gary", "mitchell", "randy", "perry", "rodney",
                  "harold", "hugh", "marty", "victor", "alfredo", "terrence", "jordan", "bobby", "geoffrey", "casey",
                  "brandon", "darren", "jesse"]

    girls_names = ["emma", "olivia", "ava", "isabella", "sophia", "mia", "amelia", "harper", "evelyn", "abigail",
                   "emily", "ella", "scarlett", "grace", "lily", "chloe", "charlotte", "aubrey", "zoey", "hannah",
                   "nora", "layla", "riley", "penelope", "mia", "savannah", "ellie", "aubrey", "scarlett", "madison",
                   "victoria", "ella", "claire", "lillian", "katherine", "grace", "allison", "hazel", "penelope",
                   "aubree", "madelyn", "scarlet", "aria", "audrey", "nova", "amelia", "zoey", "aaliyah", "savannah",
                   "emilia", "hazel", "abigail", "isla", "luna", "mila", "ella", "lily", "aria", "emily", "evelyn",
                   "layla", "olivia", "sophia", "charlotte", "scarlett", "zoe", "mila", "amelia", "aubrey", "genesis",
                   "paisley", "emery", "hazel", "violet", "nova", "nina", "ruby", "luna", "elyse", "sienna", "harmony",
                   "melody", "serenity", "hope", "faith", "amaya", "ariana", "brianna", "zara", "skye", "nadia"]

    if name in boys_names:
        return "male"
    elif name in girls_names:
        return "female"
    elif name and name[-1] == 'a':
        return "female"
    elif name and name[-1] == 'o':
        return "male"
    else:
        return "unknown"

def on_predict_button_click():
    name = name_entry.get()
    gender = predict_gender(name)
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, gender)
    result_entry.config(state="readonly")

def main():
    global name_entry, result_entry  # Declare name_entry and result_entry as global variables
    root = tk.Tk()
    root.title("Gender Predictor")
    root.geometry("1000x600")
    root.configure(bg="black")  # Set background color

    name_label = ttk.Label(root, text="Enter name:", foreground="red", font=("Times New Roman", 30), background="black")
    name_label.place(relx=0.5, rely=0.3, anchor="center")
    
    name_entry = ttk.Entry(root, font=("Times New Roman", 30), background="black", foreground="red")
    name_entry.place(relx=0.5, rely=0.5, anchor="center")

    result_label = ttk.Label(root, text="Predicted gender:", foreground="red", font=("Times New Roman", 30), background="black")
    result_label.place(relx=0.5, rely=0.7, anchor="center")
    
    result_entry = ttk.Entry(root, state="readonly", font=("Times New Roman", 30), background="black", foreground="red")
    result_entry.place(relx=0.5, rely=0.8, anchor="center")

    predict_button = ttk.Button(root, text="Predict", command=on_predict_button_click, width=20, style="TButton")
    predict_button.place(relx=0.5, rely=0.9, anchor="center")

    # Style configuration for the button
    style = ttk.Style()
    style.configure("TButton", font=("Times New Roman", 30), background="black", foreground="red")

    root.mainloop()

if __name__ == '__main__':
    main()


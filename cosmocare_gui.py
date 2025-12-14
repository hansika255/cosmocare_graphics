import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import random
from PIL import Image, ImageTk

# ---------------- DATA ---------------- #

skin_products = {
    'dry': ['HydraBoost Moisturizer', 'Aloe Vera Gel', 'Ceramide Repair Cream'],
    'oily': ['Oil-Free Gel Moisturizer', 'Mattifying Serum', 'Tea Tree Face Wash'],
    'sensitive': ['Fragrance-Free Cream', 'Soothing Lotion', 'Anti-Redness Serum'],
    'normal': ['Daily Hydration Lotion', 'Vitamin C Cream', 'Lightweight Gel Cream']
}

cosmetic_shades = {
    'lipstick': ['Rosewood', 'Ruby Red', 'Nude Pink', 'Berry Blast', 'Coral Crush'],
    'blusher': ['Peach Glow', 'Rose Petal', 'Soft Coral', 'Warm Bronze'],
    'foundation': ['Ivory', 'Beige', 'Warm Sand', 'Caramel', 'Espresso'],
    'concealer': ['Fair', 'Light', 'Medium', 'Tan', 'Deep']
}

purchase_history = pd.DataFrame(
    columns=['Name', 'Product', 'Category', 'Price', 'Rating']
)

# ---------------- ROOT ---------------- #

root = tk.Tk()
root.state("zoomed")
root.title("CosmoCare 💄")
root.configure(bg="#ffe6f0")

user_name = tk.StringVar()

# ---------------- STYLE ---------------- #

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Helvetica", 12, "bold"),
    padding=10
)

# 🔥 FIXED BEAUTIFUL COMBOBOX
style.configure(
    "Pink.TCombobox",
    fieldbackground="#fff0f5",
    background="#ffb6c1",
    foreground="#333333",
    arrowcolor="#ff1493",
    padding=6
)

style.map(
    "Pink.TCombobox",
    fieldbackground=[("readonly", "#fff0f5")],
    background=[("active", "#ff69b4"), ("readonly", "#ffb6c1")]
)

# ---------------- UTILS ---------------- #

def clear_frame():
    for w in root.winfo_children():
        w.destroy()

def validate(func):
    if not user_name.get().strip():
        messagebox.showerror("Error", "Enter your name first 💖")
        return
    func()

# ---------------- HOME ---------------- #

def home_screen():
    clear_frame()

    tk.Label(
        root,
        text="CosmoCare 💄✨",
        font=("Helvetica", 28, "bold"),
        bg="#ffe6f0",
        fg="#ff1493"
    ).pack(pady=20)

    ttk.Entry(root, textvariable=user_name, width=25).pack(pady=10)

    ttk.Button(root, text="🌿 Skin Care Quiz", command=lambda: validate(skin_care_quiz)).pack(pady=5)
    ttk.Button(root, text="💋 Cosmetics Quiz", command=lambda: validate(cosmetics_quiz)).pack(pady=5)
    ttk.Button(root, text="🧾 Purchase History", command=lambda: validate(show_history)).pack(pady=5)
    ttk.Button(root, text="🚪 Exit", command=root.destroy).pack(pady=5)

# ---------------- SKIN QUIZ ---------------- #

def skin_care_quiz():
    clear_frame()

    tk.Label(
        root,
        text="Skin Care Quiz 🌿",
        font=("Helvetica", 24, "bold"),
        bg="#ffe6f0",
        fg="#ff1493"
    ).pack(pady=20)

    frame = tk.Frame(root, bg="white", padx=35, pady=25)
    frame.pack()

    questions = {
        "Skin Type": ["dry", "oily", "normal", "sensitive"],
        "Main Concern": ["acne", "dryness", "redness", "aging"],
        "Climate": ["humid", "dry", "cold"],
        "Sun Exposure": ["low", "medium", "high"],
        "Acne Frequency": ["rare", "sometimes", "often"],
        "Skin Sensitivity": ["low", "medium", "high"]
    }

    entries = {}

    for i, (q, options) in enumerate(questions.items()):
        tk.Label(
            frame,
            text=q,
            font=("Helvetica", 14, "bold"),
            bg="white"
        ).grid(row=i, column=0, sticky="w", pady=10, padx=10)

        cb = ttk.Combobox(
            frame,
            values=options,
            state="readonly",
            style="Pink.TCombobox",
            font=("Helvetica", 13),
            width=25
        )
        cb.grid(row=i, column=1, pady=10, padx=10)
        entries[q] = cb

    def recommend():
        if not all(cb.get() for cb in entries.values()):
            messagebox.showerror("Error", "Please answer all questions 🌸")
            return

        skin = entries["Skin Type"].get()
        concern = entries["Main Concern"].get()
        sensitivity = entries["Skin Sensitivity"].get()

        # 🔥 LOGIC-BASED RECOMMENDATION
        if sensitivity == "high":
            product = "Fragrance-Free Soothing Cream"
        elif skin == "oily" and concern == "acne":
            product = "Tea Tree Acne Control Gel"
        elif skin == "dry":
            product = "Ceramide Repair Moisturizer"
        else:
            product = random.choice(skin_products[skin])

        price = round(np.random.uniform(600, 1800), 2)

        confirm = messagebox.askyesno(
            "Recommendation Ready 💖",
            f"Recommended Product:\n\n{product}\n\nPrice: ₹{price}\n\nDo you want to purchase?"
        )

        if confirm:
            global purchase_history
            purchase_history = pd.concat(
                [purchase_history, pd.DataFrame([{
                    "Name": user_name.get(),
                    "Product": product,
                    "Category": "Skin Care",
                    "Price": price,
                    "Rating": random.randint(4, 5)
                }])],
                ignore_index=True
            )
            summary_screen(product, "Skin Care", price)

    ttk.Button(
        root,
        text="✨ Get Recommendation",
        command=recommend
    ).pack(pady=20)

    ttk.Button(
        root,
        text="⬅ Back",
        command=home_screen
    ).pack()

# ---------------- COSMETICS QUIZ ---------------- #

def cosmetics_quiz():
    clear_frame()

    tk.Label(
        root,
        text="Cosmetics Quiz 💋",
        font=("Helvetica", 24, "bold"),
        bg="#ffe6f0",
        fg="#ff1493"
    ).pack(pady=20)

    frame = tk.Frame(root, bg="white", padx=35, pady=25)
    frame.pack()

    questions = {
        "Makeup Style": ["Natural", "Bold", "Party"],
        "Skin Tone": ["Fair", "Medium", "Deep"],
        "Occasion": ["Daily", "Office", "Wedding"],
        "Coverage Preference": ["Light", "Medium", "Full"],
        "Lip Color Preference": ["Nude", "Pink", "Red", "Berry"]
    }

    entries = {}

    for i, (q, options) in enumerate(questions.items()):
        tk.Label(
            frame,
            text=q,
            font=("Helvetica", 14, "bold"),
            bg="white"
        ).grid(row=i, column=0, sticky="w", pady=10, padx=10)

        cb = ttk.Combobox(
            frame,
            values=options,
            state="readonly",
            style="Pink.TCombobox",
            font=("Helvetica", 13),
            width=25
        )
        cb.grid(row=i, column=1, pady=10, padx=10)
        entries[q] = cb

    def recommend_cosmetics():
        if not all(cb.get() for cb in entries.values()):
            messagebox.showerror("Error", "Please answer all questions 💄")
            return

        skin_tone = entries["Skin Tone"].get()
        style = entries["Makeup Style"].get()
        occasion = entries["Occasion"].get()
        lip_pref = entries["Lip Color Preference"].get()

        # 🎯 LOGIC-BASED RECOMMENDATIONS
        lipstick = {
            "Nude": "Nude Pink",
            "Pink": "Rosewood",
            "Red": "Ruby Red",
            "Berry": "Berry Blast"
        }[lip_pref]

        foundation = {
            "Fair": "Ivory",
            "Medium": "Warm Sand",
            "Deep": "Caramel"
        }[skin_tone]

        blusher = "Peach Glow" if style == "Natural" else "Rose Petal"
        concealer = "Light" if skin_tone == "Fair" else "Medium"

        product_text = f"""
💄 Lipstick: {lipstick}
🎨 Foundation: {foundation}
🌸 Blusher: {blusher}
✨ Concealer: {concealer}
"""

        price = round(np.random.uniform(1800, 4500), 2)

        confirm = messagebox.askyesno(
            "Your Cosmetic Recommendation 💖",
            f"{product_text}\nTotal Price: ₹{price}\n\nDo you want to purchase?"
        )

        if confirm:
            global purchase_history
            purchase_history = pd.concat(
                [purchase_history, pd.DataFrame([{
                    "Name": user_name.get(),
                    "Product": product_text.strip(),
                    "Category": "Cosmetics",
                    "Price": price,
                    "Rating": random.randint(4, 5)
                }])],
                ignore_index=True
            )

            summary_screen(product_text, "Cosmetics", price)

    ttk.Button(
        root,
        text="✨ Get My Recommendation",
        command=recommend_cosmetics
    ).pack(pady=20)

    ttk.Button(
        root,
        text="⬅ Back",
        command=home_screen
    ).pack()

# ---------------- SUMMARY ---------------- #

def summary_screen(product, category, price):
    clear_frame()

    card = tk.Frame(root, bg="white", padx=40, pady=30)
    card.pack(pady=60)

    tk.Label(card, text="✨ Purchase Confirmed ✨", font=("Helvetica", 22, "bold"), fg="#ff1493", bg="white").pack()

    tk.Label(card, text=f"\n{product}", bg="white", font=("Helvetica", 13)).pack()
    tk.Label(card, text=f"\nCategory: {category}\nPrice: ₹{price}", bg="white").pack()

    ttk.Button(card, text="🏠 Home", command=home_screen).pack(pady=10)

# ---------------- HISTORY ---------------- #

def show_history():
    clear_frame()

    tk.Label(root, text="Purchase History 🧾", font=("Helvetica", 20, "bold")).pack(pady=20)

    data = purchase_history[purchase_history['Name'] == user_name.get()]

    if data.empty:
        tk.Label(root, text="No purchases yet").pack()
    else:
        tree = ttk.Treeview(root, columns=("Product", "Category", "Price"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        for _, r in data.iterrows():
            tree.insert("", tk.END, values=(r["Product"], r["Category"], r["Price"]))
        tree.pack(expand=True)

    ttk.Button(root, text="⬅ Back", command=home_screen).pack(pady=10)

# ---------------- START ---------------- #

home_screen()
root.mainloop()


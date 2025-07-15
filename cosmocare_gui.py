import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import numpy as np
import random

# Sample product data
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

# In-memory purchase history
purchase_history = pd.DataFrame(columns=['Name', 'Product', 'Category', 'Price'])

# Initialize GUI
root = tk.Tk()
root.title("CosmoCare 💄")
root.geometry("600x600")
root.configure(bg="#fff5f8")

user_name = tk.StringVar()

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def home_screen():
    clear_frame()
    tk.Label(root, text="Welcome to CosmoCare 💄✨", font=("Arial", 22, 'bold'), bg="#fff5f8").pack(pady=20)
    tk.Label(root, text="Enter your name:", font=("Arial", 14), bg="#fff5f8").pack()
    tk.Entry(root, textvariable=user_name, font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Start Skin Care Quiz", font=("Arial", 12), bg="#f28ca2", command=skin_care_quiz).pack(pady=10)
    tk.Button(root, text="Start Cosmetics Quiz", font=("Arial", 12), bg="#f28ca2", command=cosmetics_quiz).pack(pady=10)
    tk.Button(root, text="View Purchase History", font=("Arial", 12), bg="#f28ca2", command=show_history).pack(pady=10)
    tk.Button(root, text="Exit", font=("Arial", 12), bg="#f28ca2", command=root.destroy).pack(pady=10)

def skin_care_quiz():
    clear_frame()
    tk.Label(root, text="Skin Care Quiz 🌿", font=("Arial", 20, "bold"), bg="#fff5f8").pack(pady=20)
    entries = {}

    options = {
        'Skin Type': ['dry', 'oily', 'normal', 'sensitive'],
        'Allergies': ['yes', 'no'],
        'Sun Exposure': ['low', 'medium', 'high'],
        'Hydration Needed': ['yes', 'no'],
        'Concern': ['acne', 'dryness', 'redness', 'aging']
    }

    for key, vals in options.items():
        tk.Label(root, text=key + ":", font=("Arial", 12), bg="#fff5f8").pack()
        entries[key] = ttk.Combobox(root, values=vals, state="readonly")
        entries[key].pack(pady=5)

    def recommend_skin():
        skin_type = entries['Skin Type'].get()
        product = random.choice(skin_products.get(skin_type, ['Universal Moisturizer']))
        price = round(np.random.uniform(10, 50), 2)
        result = f"🎁 {product} - ₹{price}"

        if messagebox.askyesno("Recommended Product", result + "\n\nWould you like to buy this product?"):
            global purchase_history
            purchase_history = pd.concat([purchase_history, pd.DataFrame([{
                'Name': user_name.get(),
                'Product': product,
                'Category': 'Skin Care',
                'Price': price
            }])], ignore_index=True)
            messagebox.showinfo("Thank You", "Purchase successful! 💖")

    tk.Button(root, text="Get Recommendation", command=recommend_skin, font=("Arial", 12), bg="#f28ca2").pack(pady=20)
    tk.Button(root, text="⬅ Back", command=home_screen, font=("Arial", 10)).pack()

def cosmetics_quiz():
    clear_frame()
    tk.Label(root, text="Cosmetics Quiz 💋", font=("Arial", 20, "bold"), bg="#fff5f8").pack(pady=20)

    labels = [
        "Skin Undertone", "Makeup Preference", "Eye Color", "Hair Color",
        "Makeup Allergies", "Foundation Finish", "Skin Type",
        "Product Type", "Outfit Tone", "Makeup Usage"
    ]
    values = [
        ['cool', 'warm', 'neutral'], ['bold', 'natural'], ['brown', 'blue', 'green', 'other'],
        ['black', 'brown', 'blonde', 'red', 'other'], ['yes', 'no'], ['matte', 'dewy', 'natural'],
        ['oily', 'dry', 'combination'], ['liquid', 'powder'], ['bright', 'pastel', 'dark'], ['daily', 'occasionally']
    ]

    combos = []
    for i in range(len(labels)):
        tk.Label(root, text=labels[i] + ":", font=("Arial", 12), bg="#fff5f8").pack()
        cb = ttk.Combobox(root, values=values[i], state="readonly")
        cb.pack(pady=5)
        combos.append(cb)

    def recommend_cosmetics():
        lipstick = random.choice(cosmetic_shades['lipstick'])
        blusher = random.choice(cosmetic_shades['blusher'])
        foundation = random.choice(cosmetic_shades['foundation'])
        concealer = random.choice(cosmetic_shades['concealer'])
        price = round(np.random.uniform(15, 60), 2)

        result = f"💄 Lipstick: {lipstick}\n🥀 Blusher: {blusher}\n🪞 Foundation: {foundation}\n🖌 Concealer: {concealer}\n\nTotal: ₹{price}"
        if messagebox.askyesno("Recommended Cosmetic Set", result + "\n\nWould you like to buy this set?"):
            global purchase_history
            purchase_history = pd.concat([purchase_history, pd.DataFrame([{
                'Name': user_name.get(),
                'Product': f"Set: {lipstick}, {blusher}, {foundation}, {concealer}",
                'Category': 'Cosmetics',
                'Price': price
            }])], ignore_index=True)
            messagebox.showinfo("Purchase Confirmed", "You look fabulous! 💅")

    tk.Button(root, text="Get Cosmetic Recommendation", font=("Arial", 12), bg="#f28ca2", command=recommend_cosmetics).pack(pady=20)
    tk.Button(root, text="⬅ Back", command=home_screen, font=("Arial", 10)).pack()

def show_history():
    clear_frame()
    tk.Label(root, text="Purchase History 🧾", font=("Arial", 20, "bold"), bg="#fff5f8").pack(pady=20)

    frame = tk.Frame(root, bg="#fff5f8")
    frame.pack(fill=tk.BOTH, expand=True)

    user_data = purchase_history[purchase_history['Name'] == user_name.get()]
    if user_data.empty:
        tk.Label(frame, text="No purchases yet.", font=("Arial", 14), bg="#fff5f8").pack()
    else:
        tree = ttk.Treeview(frame, columns=('Product', 'Category', 'Price'), show='headings')
        tree.heading('Product', text='Product')
        tree.heading('Category', text='Category')
        tree.heading('Price', text='Price')

        for _, row in user_data.iterrows():
            tree.insert('', tk.END, values=(row['Product'], row['Category'], f"₹{row['Price']}"))

        tree.pack(fill=tk.BOTH, expand=True)

    tk.Button(root, text="⬅ Back", command=home_screen, font=("Arial", 10)).pack(pady=10)

# Start the app
home_screen()
root.mainloop()

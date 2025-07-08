import tkinter as tk
from tkinter import ttk, messagebox

# Static exchange rates
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'INR': 74.0,
    'GBP': 0.75
}

def convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_cb.get()
        to_currency = to_currency_cb.get()

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            raise ValueError("Invalid currency selected.")
        
        usd_amount = amount / exchange_rates[from_currency]
        converted_amount = usd_amount * exchange_rates[to_currency]

        result_label.config(text=f"{converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount and select currencies.")

# GUI Window
window = tk.Tk()
window.title("Currency Converter")

tk.Label(window, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="From:").grid(row=1, column=0, padx=10, pady=10)
from_currency_cb = ttk.Combobox(window, values=list(exchange_rates.keys()))
from_currency_cb.grid(row=1, column=1, padx=10, pady=10)
from_currency_cb.set("USD")

tk.Label(window, text="To:").grid(row=2, column=0, padx=10, pady=10)
to_currency_cb = ttk.Combobox(window, values=list(exchange_rates.keys()))
to_currency_cb.grid(row=2, column=1, padx=10, pady=10)
to_currency_cb.set("INR")

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Converted Amount")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()

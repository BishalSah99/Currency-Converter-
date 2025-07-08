# Currency-Converter-
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'INR': 74.0,
    'GBP': 0.75
}
These are hardcoded currency exchange rates, using USD as the base currency (USD → USD = 1.0).

🧮 Conversion Logic
python
Copy
Edit
def convert():
    try:
        amount = float(amount_entry.get())  # Get amount input by user
        from_currency = from_currency_cb.get()  # Get source currency
        to_currency = to_currency_cb.get()  # Get target currency

        # Check if selected currencies are valid
        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            raise ValueError("Invalid currency selected.")

        # Convert to USD first, then to target currency
        usd_amount = amount / exchange_rates[from_currency]
        converted_amount = usd_amount * exchange_rates[to_currency]

        result_label.config(text=f"{converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount and select currencies.")
Step 1: Get and validate user input.

Step 2: Convert the input currency to USD.

Step 3: Convert from USD to the target currency.

Step 4: Display the result.

🖼️ GUI Components
1. Main Window Setup
python
Copy
Edit
window = tk.Tk()
window.title("Currency Converter")
2. Input Fields
Amount label and entry

python
Copy
Edit
tk.Label(window, text="Amount:").grid(...)
amount_entry = tk.Entry(window)
From Currency Combobox

python
Copy
Edit
from_currency_cb = ttk.Combobox(window, values=list(exchange_rates.keys()))
from_currency_cb.set("USD")
To Currency Combobox

python
Copy
Edit
to_currency_cb = ttk.Combobox(window, values=list(exchange_rates.keys()))
to_currency_cb.set("INR")
3. Convert Button
python
Copy
Edit
convert_button = tk.Button(window, text="Convert", command=convert)
This button runs the convert() function when clicked.

4. Result Display
python
Copy
Edit
result_label = tk.Label(window, text="Converted Amount")
5. Run the Application
python
Copy
Edit
window.mainloop()
This keeps the GUI window open and responsive.

 Example Use Case
Enter 100
Select From = USD, To = INR
Click Convert
Output = 7400.00 INR

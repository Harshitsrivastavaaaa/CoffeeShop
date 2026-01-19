# ☕ CharBucks Enterprise POS System: A modern, high-performance Point of Sale (POS) application built with Python and CustomTkinter. This system features a tabbed menu interface, dynamic cart calculation, live digital receipts, and integrated UPI QR code generation for payments.

## ✨ Features

* **Modern Dark UI:** Professional "Zinc & Emerald" color scheme using `CustomTkinter`.
* **Tabbed Menu:** Categorized inventory (Hot Coffee, Cold Brews, Bakery, Meals).
* **Vector Icons:** Custom-drawn icons for every item (no external image files required).
* **Live Receipt:** Real-time scrolling receipt log showing items, subtotals, and taxes.
* **Smart Cart:** Dynamic calculation of Base Price + Size Costs + GST (12%).
* **Payment System:**
* **UPI:** Generates a real, scannable QR code with a 30-second security timer.
* **Cash:** Manual confirmation mode.


* **Transaction Logging:** Automatically saves order history to `transactions.txt`.

---

## 🛠️ Prerequisites

Before running the application, ensure you have **Python 3.10 or higher** installed on your system.

You can check your python version by running:

```bash
python --version

```

---

## 📦 Installation

### 1. Download the Project

Save your Python script (the code provided previously) into a folder. Let's call the file `main.py`.

### 2. Install Dependencies

Open your terminal or command prompt (CMD/PowerShell) in that folder and run the following command to install the required libraries:

```bash
pip install customtkinter qrcode[pil] pillow

```

**What these do:**

* `customtkinter`: For the modern UI elements.
* `qrcode[pil]`: To generate the payment QR codes.
* `pillow`: To handle image processing and graphics.

---

## 🚀 How to Run

1. Open your terminal/command prompt.
2. Navigate to the folder where you saved the file.
3. Run the application:

```bash
python main.py

```

*(Replace `main.py` with whatever you named your python file, e.g., `charbucks_v12.py`)*

---

## 📖 User Guide

### 1. Adding Items

1. Select a Category Tab (e.g., **HOT COFFEE**).
2. Click on an item (e.g., *Espresso*).
3. Select a Size (**S**, **M**, or **L**).
4. Click the big green **ADD ITEM TO ORDER** button.

### 2. The Receipt

* As you add items, they appear in the center "Live Order" panel.
* If you make a mistake, click **VOID TRANSACTION** to clear the cart.

### 3. Checkout

1. Review the **Total** on the right panel.
2. Select Payment Mode:
* **UPI:** Generates a QR code. Scan it with a phone. The system waits 30 seconds for confirmation (simulated). Click **Confirm Payment**.
* **CASH:** Displays a cash icon. Click **Mark as Paid**.


3. Once paid, an **Order Number** is generated, and the transaction is saved.

---

## 📂 Project Structure

This application is designed to be **single-file portable**. You do not need a folder full of images because all icons are drawn mathematically within the code.

```text
/CharBucks_POS
│
├── main.py              # The application source code
├── transactions.txt     # (Auto-generated) Logs of all sales
└── README.md            # This documentation file

```

---

## ❓ Troubleshooting

**Q: I get a `ModuleNotFoundError`?**
A: You likely missed a requirement. Run `pip install customtkinter qrcode pillow` again.

**Q: The QR Code is just a white square?**
A: Ensure you have the `pillow` library installed correctly.

**Q: The window is too big/small for my screen.**
A: In the code, look for the line `self.geometry("1300x700")` inside the `__init__` function and adjust the numbers to fit your screen resolution.

---

**Developed with ❤️ using Python.**

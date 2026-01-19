## CHAR BUCKS COFFEE ##
import customtkinter as ctk
import math
import datetime
import qrcode
import random
from PIL import Image, ImageTk, ImageDraw

# --- THEME SETUP ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# --- PRO COLOR PALETTE ---
C_BG_MAIN = "#09090b"       
C_PANEL   = "#18181b"       
C_CARD    = "#27272a"       
C_NAV     = "#1c1917"       
C_ACCENT  = "#10b981"       
C_ACCENT_HOVER = "#059669"  
C_FAIL    = "#ef4444"       
C_TEXT_MAIN = "#f4f4f5"     
C_TEXT_DIM  = "#a1a1aa"     
C_BORDER  = "#3f3f46"       
C_RECEIPT_BG = "#000000"    
C_RECEIPT_TXT = "#4ade80"   

class IconFactory:
    """Draws unique vector icons."""
    @staticmethod
    def get_icon(name, size=(20, 20)):
        img = Image.new("RGBA", size, (0,0,0,0))
        draw = ImageDraw.Draw(img)
        w, h = size
        color = C_ACCENT
        
        if name in ["Grilled Cheese", "Veggie Club", "Chicken Panini", "Egg & Mayo"]:
            draw.polygon([(w*0.1, h*0.8), (w*0.9, h*0.8), (w*0.9, h*0.2)], outline=color, width=2)
            draw.line([(w*0.1, h*0.8), (w*0.9, h*0.2)], fill=color, width=2)
            return ctk.CTkImage(img, size=size)

        if name == "None":
            draw.line([w*0.3, h*0.5, w*0.7, h*0.5], fill="gray", width=2)
            return ctk.CTkImage(img, size=size)

        if "Espresso" in name:
            draw.rectangle([w*0.3, h*0.4, w*0.7, h*0.8], fill=color)
            draw.arc([w*0.7, h*0.4, w*0.85, h*0.6], 270, 90, fill=color, width=2)
        elif "Latte" in name or "Flat White" in name:
            draw.polygon([(w*0.3, h*0.8), (w*0.7, h*0.8), (w*0.8, h*0.2), (w*0.2, h*0.2)], fill=color)
        elif "Cold" in name:
            draw.rectangle([w*0.3, h*0.3, w*0.7, h*0.7], outline=color, width=2)
        elif "Mocha" in name:
            draw.ellipse([w*0.3, h*0.4, w*0.7, h*0.9], fill=color)
        else:
            draw.chord([w*0.2, h*0.3, w*0.8, h*0.8], 0, 180, fill=color)

        return ctk.CTkImage(img, size=size)

    @staticmethod
    def create_main_logo(size):
        img = Image.new("RGBA", size, (0,0,0,0))
        draw = ImageDraw.Draw(img)
        w, h = size
        draw.ellipse([0, 0, w, h], fill=C_ACCENT)
        draw.chord([w*0.25, h*0.25, w*0.75, h*0.75], 0, 180, fill="white")
        draw.rectangle([w*0.25, h*0.25, w*0.75, h*0.5], fill="white")
        draw.line([w*0.4, h*0.2, w*0.4, h*0.1], fill="white", width=2)
        draw.line([w*0.6, h*0.2, w*0.6, h*0.1], fill="white", width=2)
        return ctk.CTkImage(img, size=size)

class CharBucksApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CharBucks POS | Enterprise Edition")
        self.geometry("1280x600")
        self.resizable(False, False)
        self.configure(fg_color=C_BG_MAIN)

        # Data
        self.menu_data = {
            "Cuppachino Hot": {"base": 50, "costs": {"Small": 80, "Medium": 160, "Large": 199, "Bucket": 299}},
            "Lioni Cold":     {"base": 20, "costs": {"Small": 130, "Medium": 170, "Large": 249, "Bucket": 349}},
            "Latte":          {"base": 30, "costs": {"Small": 90,  "Medium": 120, "Large": 149, "Bucket": 199}},
            "Americano":      {"base": 25, "costs": {"Small": 60,  "Medium": 80,  "Large": 119, "Bucket": 169}},
            "Espresso":       {"base": 40, "costs": {"Small": 50,  "Medium": 70,  "Large": 90,  "Bucket": 120}},
            "Mocha":          {"base": 55, "costs": {"Small": 100, "Medium": 180, "Large": 220, "Bucket": 310}},
            "Flat White":     {"base": 45, "costs": {"Small": 95,  "Medium": 130, "Large": 160, "Bucket": 210}},
            "Macchiato":      {"base": 50, "costs": {"Small": 85,  "Medium": 125, "Large": 155, "Bucket": 205}}
        }
        self.sandwich_data = {"None": 0, "Grilled Cheese": 120, "Veggie Club": 150, "Chicken Panini": 190, "Egg & Mayo": 160}
        self.shop_upi = "charbucks@upi"
        
        # State
        self.coffee_var = ctk.StringVar(value="Cuppachino Hot")
        self.size_var = ctk.StringVar(value="Small")
        self.food_var = ctk.StringVar(value="None")
        self.payment_mode = ctk.StringVar(value="UPI")
        self.cart = []
        self.cart_total = 0
        self.timer_running = False
        self.time_left = 30
        self.timer_id = None
        self.final_amount = 0

        # --- GRID LAYOUT ---
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(0, weight=0)   
        self.grid_rowconfigure(1, weight=1)    

        self.create_navbar()
        
        # Content Container
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=1)
        self.content.grid_columnconfigure(2, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        self.create_left_menu()
        self.create_center_receipt()
        self.create_right_checkout()

    # =========================================================================
    # NAVBAR (COMPACT HEIGHT)
    # =========================================================================
    def create_navbar(self):
        self.navbar = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color=C_NAV) # Reduced height
        self.navbar.grid(row=0, column=0, sticky="ew")
        self.navbar.grid_propagate(False)

        # Logo Left
        self.logo = IconFactory.create_main_logo((35,35))
        ctk.CTkLabel(self.navbar, text="", image=self.logo).pack(side="left", padx=(20, 10))
        
        # Branding
        title_frame = ctk.CTkFrame(self.navbar, fg_color="transparent")
        title_frame.pack(side="left", pady=10)
        ctk.CTkLabel(title_frame, text="CHAR BUCKS", font=("Segoe UI", 20, "bold"), text_color=C_TEXT_MAIN).pack(anchor="w")
        ctk.CTkLabel(title_frame, text="ENTERPRISE POS", font=("Segoe UI", 9, "bold"), text_color=C_ACCENT).pack(anchor="w")

        # Right Status
        status_frame = ctk.CTkFrame(self.navbar, fg_color="transparent")
        status_frame.pack(side="right", padx=30)
        
        dot = ctk.CTkCanvas(status_frame, width=8, height=8, bg=C_NAV, highlightthickness=0)
        dot.create_oval(1, 1, 7, 7, fill="#4ade80", outline="")
        dot.pack(side="left", padx=5)
        ctk.CTkLabel(status_frame, text="ONLINE", font=("Segoe UI", 11, "bold"), text_color=C_TEXT_DIM).pack(side="left")

    # =========================================================================
    # COLUMN 1: MENU
    # =========================================================================
    def create_left_menu(self):
        self.frame_menu = ctk.CTkFrame(self.content, fg_color=C_PANEL, corner_radius=8)
        self.frame_menu.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Scrollable Area (Smaller padding)
        self.scroll_menu = ctk.CTkScrollableFrame(self.frame_menu, fg_color="transparent")
        self.scroll_menu.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.add_label(self.scroll_menu, "1. SELECT BEVERAGE")
        for coffee in self.menu_data:
            self.create_radio_row(self.scroll_menu, coffee, self.coffee_var)

        self.add_label(self.scroll_menu, "2. SELECT SANDWICH")
        for food in self.sandwich_data:
            self.create_radio_row(self.scroll_menu, food, self.food_var)

        # Bottom Area
        bottom = ctk.CTkFrame(self.frame_menu, fg_color=C_PANEL)
        bottom.pack(fill="x", side="bottom", padx=15, pady=10)

        self.add_label(bottom, "3. CUP SIZE")
        self.seg_size = ctk.CTkSegmentedButton(bottom, values=["Small", "Medium", "Large", "Bucket"],
                                               variable=self.size_var,
                                               selected_color=C_ACCENT, selected_hover_color=C_ACCENT_HOVER,
                                               height=25)
        self.seg_size.pack(pady=5, fill="x")

        self.btn_add = ctk.CTkButton(bottom, text="ADD TO ORDER (+)", height=40,
                                     fg_color="#334155", hover_color="#475569",
                                     command=self.add_to_cart)
        self.btn_add.pack(pady=(10, 0), fill="x")

    def create_radio_row(self, parent, text, variable):
        row = ctk.CTkFrame(parent, fg_color="transparent", height=30)
        row.pack(fill="x", pady=0)
        icon = IconFactory.get_icon(text)
        ctk.CTkLabel(row, text="", image=icon, width=25).pack(side="left", padx=(5, 5))
        ctk.CTkRadioButton(row, text=text, variable=variable, value=text,
                           font=("Segoe UI", 12), fg_color=C_ACCENT, hover_color=C_ACCENT_HOVER).pack(side="left", pady=2)

    def add_label(self, parent, text):
        ctk.CTkLabel(parent, text=text, font=("Segoe UI", 10, "bold"), 
                     text_color=C_TEXT_DIM).pack(fill="x", padx=5, pady=(10, 2), anchor="w")

    # =========================================================================
    # COLUMN 2: RECEIPT
    # =========================================================================
    def create_center_receipt(self):
        self.frame_center = ctk.CTkFrame(self.content, fg_color=C_BG_MAIN, corner_radius=8)
        self.frame_center.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        ctk.CTkLabel(self.frame_center, text="LIVE RECEIPT", font=("Segoe UI", 12, "bold"), text_color=C_TEXT_DIM).pack(pady=(10, 5))

        card = ctk.CTkFrame(self.frame_center, fg_color=C_CARD, corner_radius=12, border_width=1, border_color=C_BORDER)
        card.pack(fill="both", expand=True, padx=15, pady=5)

        self.txt_receipt = ctk.CTkTextbox(card, font=("Consolas", 12),
                                          fg_color=C_RECEIPT_BG, text_color=C_RECEIPT_TXT,
                                          corner_radius=6)
        self.txt_receipt.pack(fill="both", expand=True, padx=8, pady=8)
        self.log_receipt("\n [SYSTEM READY]...")

        self.btn_reset = ctk.CTkButton(self.frame_center, text="CLEAR CART / RESET", height=35,
                                       fg_color=C_BORDER, hover_color="#52525b",
                                       command=self.reset)
        self.btn_reset.pack(pady=10, padx=15, fill="x")

    # =========================================================================
    # COLUMN 3: CHECKOUT
    # =========================================================================
    def create_right_checkout(self):
        self.frame_checkout = ctk.CTkFrame(self.content, fg_color=C_PANEL, corner_radius=8)
        self.frame_checkout.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.lbl_status = ctk.CTkLabel(self.frame_checkout, text="TOTAL: Rs. 0", 
                                       font=("Segoe UI", 20, "bold"), text_color=C_TEXT_MAIN)
        self.lbl_status.pack(pady=(20, 10))

        self.add_label(self.frame_checkout, "SELECT PAYMENT MODE")
        self.seg_mode = ctk.CTkSegmentedButton(self.frame_checkout, values=["UPI", "CASH"],
                                               variable=self.payment_mode,
                                               selected_color=C_ACCENT, selected_hover_color=C_ACCENT_HOVER,
                                               command=self.update_payment_ui, height=25)
        self.seg_mode.pack(padx=15, fill="x")

        self.pay_card = ctk.CTkFrame(self.frame_checkout, fg_color=C_CARD, corner_radius=12, border_width=1, border_color=C_BORDER)
        self.pay_card.pack(fill="both", expand=True, padx=15, pady=15)

        # UPI UI
        self.frame_upi = ctk.CTkFrame(self.pay_card, fg_color="transparent")
        self.qr_box = ctk.CTkFrame(self.frame_upi, width=160, height=160, fg_color=C_BG_MAIN, border_width=2, border_color=C_BORDER)
        self.qr_box.pack(pady=15)
        self.qr_box.pack_propagate(False)
        self.lbl_qr = ctk.CTkLabel(self.qr_box, text="QR GENERATING...", text_color=C_BORDER)
        self.lbl_qr.place(relx=0.5, rely=0.5, anchor="center")
        self.lbl_timer = ctk.CTkLabel(self.frame_upi, text="", font=("Consolas", 16, "bold"), text_color="#ef4444")
        self.lbl_timer.pack(pady=2)

        # Cash UI
        self.frame_cash = ctk.CTkFrame(self.pay_card, fg_color="transparent")
        ctk.CTkLabel(self.frame_cash, text="💵", font=("Arial", 50)).pack(pady=(30, 10))
        ctk.CTkLabel(self.frame_cash, text="COLLECT CASH AT COUNTER", font=("Segoe UI", 12, "bold")).pack()

        self.btn_action = ctk.CTkButton(self.frame_checkout, text="FINALIZE ORDER", 
                                        height=45, font=("Segoe UI", 13, "bold"),
                                        fg_color=C_ACCENT, hover_color=C_ACCENT_HOVER,
                                        command=self.initiate_payment)
        self.btn_action.pack(padx=15, pady=(0, 20), fill="x")
        
        self.frame_upi.pack_forget()
        self.frame_cash.pack_forget()

    # =========================================================================
    # LOGIC
    # =========================================================================
    def update_payment_ui(self, mode):
        if self.cart_total > 0 and self.btn_action.cget("text") != "FINALIZE ORDER":
             if mode == "UPI":
                 self.frame_cash.pack_forget()
                 self.frame_upi.pack(fill="both", expand=True)
                 self.generate_qr(self.final_amount)
             else:
                 self.stop_timer()
                 self.frame_upi.pack_forget()
                 self.frame_cash.pack(fill="both", expand=True)
                 self.btn_action.configure(text="MARK AS PAID (CASH)")

    def add_to_cart(self):
        if self.timer_running: return 

        c_name = self.coffee_var.get()
        s_name = self.size_var.get()
        f_name = self.food_var.get()
        
        c_cost = self.menu_data[c_name]['base'] + self.menu_data[c_name]['costs'][s_name] + 8.63
        f_cost = self.sandwich_data[f_name]
        item_total = c_cost + f_cost
        
        self.cart.append(item_total)
        self.cart_total += item_total
        
        self.log_receipt(f"\n + {c_name} ({s_name})")
        if f_name != "None": self.log_receipt(f"   & {f_name}")
        self.log_receipt(f"   Sub: Rs.{item_total:.2f}")
        
        self.lbl_status.configure(text=f"TOTAL: Rs. {self.cart_total:.0f}")

    def initiate_payment(self):
        if not self.cart:
            self.log_receipt("\n [ERROR] Cart is Empty!")
            return

        gst = self.cart_total * 0.12
        self.final_amount = math.ceil(self.cart_total + gst)
        donation = self.final_amount - (self.cart_total + gst)
        
        summary = (f"\n ---------------------------"
                   f"\n SUB TOTAL : Rs.{self.cart_total:.2f}"
                   f"\n GST (12%) : Rs.{gst:.2f}"
                   f"\n ROUND OFF : Rs.{donation:.2f}"
                   f"\n TOTAL PAY : Rs.{self.final_amount:.2f}"
                   f"\n ---------------------------")
        self.log_receipt(summary)

        mode = self.payment_mode.get()
        if mode == "UPI":
            self.frame_upi.pack(fill="both", expand=True)
            self.generate_qr(self.final_amount)
            self.btn_action.configure(text="CONFIRM PAYMENT RECEIVED")
        else:
            self.frame_cash.pack(fill="both", expand=True)
            self.btn_action.configure(text="MARK AS PAID (CASH)")
            
        self.btn_action.configure(command=self.finish_transaction)

    def generate_qr(self, amount):
        url = f"upi://pay?pa={self.shop_upi}&pn=CharBucks&am={amount}&cu=INR"
        qr = qrcode.QRCode(box_size=4, border=1) # Smaller blocks for compact space
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="white", back_color="black")
        
        self.qr_img = ctk.CTkImage(img.get_image(), size=(140, 140))
        self.lbl_qr.configure(image=self.qr_img, text="")
        
        self.time_left = 30
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.lbl_timer.configure(text=f"Expires in: {self.time_left}s")
            self.time_left -= 1
            self.timer_id = self.after(1000, self.update_timer)
        elif self.timer_running and self.time_left <= 0:
            self.stop_timer()
            self.lbl_qr.configure(image=None, text="TIMEOUT", text_color=C_FAIL)
            self.log_receipt("\n [TIMEOUT] TRANSACTION FAILED")
            self.reset_ui_state()

    def finish_transaction(self):
        self.stop_timer()
        order_num = random.randint(1000, 9999)
        
        self.log_receipt(f"\n ***************************")
        self.log_receipt(f"\n  ORDER #{order_num} [PAID: {self.payment_mode.get()}]")
        self.log_receipt(f"\n ***************************")
        
        try:
            with open("transactions.txt", "a") as f:
                t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{t}] #{order_num} | {self.payment_mode.get()} | Rs.{self.final_amount}\n")
        except: pass
        
        self.cart = []
        self.cart_total = 0
        self.lbl_status.configure(text="ORDER COMPLETE")
        self.btn_action.configure(text="START NEW ORDER", command=self.reset)

    def reset_ui_state(self):
        self.btn_action.configure(text="FINALIZE ORDER", command=self.initiate_payment)
        self.frame_upi.pack_forget()
        self.frame_cash.pack_forget()

    def reset(self):
        self.stop_timer()
        self.timer_running = False
        self.cart = []
        self.cart_total = 0
        
        self.reset_ui_state()
        self.lbl_status.configure(text="TOTAL: Rs. 0")
        self.txt_receipt.configure(state="normal")
        self.txt_receipt.delete("0.0", "end")
        self.log_receipt("\n [NEW SESSION STARTED]...")

    def stop_timer(self):
        if self.timer_id:
            try: self.after_cancel(self.timer_id)
            except: pass
        self.timer_id = None

    def log_receipt(self, text):
        self.txt_receipt.configure(state="normal")
        self.txt_receipt.insert("end", text)
        self.txt_receipt.see("end") 
        self.txt_receipt.configure(state="disabled")

if __name__ == "__main__":
    app = CharBucksApp()
    app.mainloop()

## COMPLETE PROGRAM ENDS HERE ##

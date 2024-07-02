import tkinter as tk
from tkinter import messagebox, filedialog
import pyqrcode
import png

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        self.url_label = tk.Label(root, text="Enter URL or String:")
        self.url_label.grid(row=0, column=0)
        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.grid(row=0, column=1)

        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.grid(row=1, column=0, columnspan=2)

        self.save_button = tk.Button(root, text="Save QR Code", command=self.save_qr_code, state=tk.DISABLED)
        self.save_button.grid(row=2, column=0, columnspan=2)

        self.qr_code = None

    def generate_qr_code(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL or string.")
            return

        self.qr_code = pyqrcode.create(url)
        self.qr_code.show()
        self.save_button.config(state=tk.NORMAL)

    def save_qr_code(self):
        if not self.qr_code:
            messagebox.showerror("Error", "No QR code to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png")])
        if file_path:
            self.qr_code.png(file_path, scale=8)
            messagebox.showinfo("Success", f"QR code saved as {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

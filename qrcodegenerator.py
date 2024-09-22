import sys
import pyqrcode
import png

def generate_qr_code(data):
    if not data:
        print("Error: Please provide a valid URL or string.")
        return None

    try:
        qr_code = pyqrcode.create(data)
        qr_code.show()
        return qr_code
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

def save_qr_code(qr_code, file_path):
    if not qr_code:
        print("Error: No QR code to save.")
        return

    try:
        qr_code.png(file_path, scale=8)
        print(f"Success: QR code saved as {file_path}")
    except Exception as e:
        print(f"Error saving QR code: {e}")

if __name__ == "__main__":
    # Check for command line arguments
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        # Take input from the user
        url = input("Enter URL or string to generate QR code: ")

    qr_code = generate_qr_code(url)

    # Prompt to save the QR code
    if qr_code:
        save_option = input("Do you want to save the QR code? (yes/no): ").lower()
        if save_option == 'yes':
            file_path = input("Enter the full path to save the QR code (with .png extension): ")
            save_qr_code(qr_code, file_path)
        else:
            print("QR code was not saved.")

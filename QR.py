import qrcode
import os
import random
import string

def generate_random_code(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

def get_project_folder():
    # Returns the folder where this script is located
    return os.path.dirname(os.path.abspath(__file__))

def generate_qr_code(code_data, filename_suffix):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(code_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save to project folder
    project_folder = get_project_folder()
    filename = f"qr_{filename_suffix}.png"
    full_path = os.path.join(project_folder, filename)
    img.save(full_path)
 
    print(f"\n✅ QR code saved to: {full_path}")
    print(f"📦 Encoded data: {code_data}\n")

    # Open the image using default viewer
    os.system(f'start {full_path}')  

# 🔄 Generate random code
random_code = generate_random_code()

# 🖼️ Generate QR code with only the random code
generate_qr_code(random_code, random_code)
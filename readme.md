# 📱 vCard QR Code Generator 🔲

Generate personalized QR codes containing your contact information in vCard format! Perfect for business cards, social media profiles, or any situation where you want to share your contact details instantly! 🚀

## ✨ Features

- 📝 Create detailed vCards with:
  - 👤 Basic contact information
  - 📞 Phone numbers
  - 📧 Email addresses
  - 🏢 Professional details
  - 📍 Address information
  - 🎂 Personal dates
  - 🌐 Social media links
- 🎨 Customize QR codes with your company logo
- 🖼️ Add profile photos
- ⬇️ Download QR codes instantly
- 🎯 Simple and intuitive web interface

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/vcard-qr-generator.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Docker 🐳

This project supports Dockerization, allowing you to easily run the application in a containerized environment. You have two options:

### Option 1: Build the Docker Image Yourself

1. Build the Docker image:

    ```bash
    docker build -t vcard-qr .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8501:8501 vcard-qr
    ```

### Option 2: Use the Pre-built Docker Image

You can use the pre-built Docker image available on [Docker Hub](https://hub.docker.com/r/JOramas/vcard-qr):

1. Pull the Docker image:

    ```bash
    docker pull joramas/vcard-qr:latest
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8501:8501 joramas/vcard-qr:latest
    ```

## 🚀 Usage

1. Start the Streamlit app:

    ```bash
    streamlit run web.py
    ```

2. Open your browser and navigate to the provided local URL 🌐

3. Fill in your contact details:
   - Required fields: Full Name and either Phone or Email 📝
   - Optional fields: Professional info, address, and more! ✨

4. Upload your logo (optional) 🎨

5. Click "Generate QR Code" and download your personalized QR code! ⬇️

## 🔧 Technical Details

- Built with Python 3.x 🐍
- Uses Streamlit for the web interface 🖥️
- Powered by:
  - qrcode library for QR code generation
  - vobject for vCard creation
  - Pillow for image processing
  - Streamlit for the web interface

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details. ⚖️

## 📞 Contact

Have questions? Found a bug? Please open an issue! 🐞

---

Made with ❤️ by JOramas

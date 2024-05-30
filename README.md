# CLEARCUT

Welcome to CLEARCUT, a Django project developed for the "Code Quest Summer of Innovation 2024." CLEARCUT allows users to easily upload images with backgrounds and download the same images with the backgrounds removed. Additionally, it provides a preview of both the original and processed images. When you upload a new image, the previously uploaded image is automatically deleted.

## Features

- **One-click Upload**: Quickly upload images with backgrounds.
- **One-click Download**: Easily download images with the backgrounds removed.
- **Image Preview**: View both the original and background-free images before downloading.
- **Automatic Cleanup**: Automatically delete the previously uploaded image when a new one is uploaded.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Pillow (Python Imaging Library)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Thamaraiselvan16/ClearCut
    cd clearcut
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    pip install virtualenv
    python -m venv venv_name
    source venv_name\Scripts\activate  # On mac, use `venv_name/bin/activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

### Usage

1. **Upload an Image**: Navigate to the upload page and select an image with a background.
2. **Preview Images**: After uploading, preview both the original and the background-free images.
3. **Download Image**: Click the download button to save the image without the background.


## Acknowledgments

- Thanks to the Code Quest Summer of Innovation 2024 for the opportunity to develop this project.
- Special thanks to the Django and Pillow communities for their excellent tools and documentation.

---

We hope you enjoy using CLEARCUT. If you have any questions or feedback, feel free to open an issue or contact us.

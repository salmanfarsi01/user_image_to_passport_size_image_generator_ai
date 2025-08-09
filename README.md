AI Passport Photo Maker

<img width="696" height="442" alt="2" src="https://github.com/user-attachments/assets/3f00c816-b9e3-4eb6-8ed2-72d50bf63d7e" />

A simple yet powerful web application built with Django that automates the creation of passport photos. This tool allows users to upload any straight-facing portrait, and it will automatically remove the background, resize the image to specific country standards, and allow the user to apply a compliant solid-color background before downloading the final result.

Preview

Note: You should take a screenshot of your running application and replace the URL above with your own.

The Problem It Solves

Getting official passport photos can be a hassle. It often requires finding a photo booth or studio, paying a fee, and hoping the photo meets the strict government requirements. This application streamlines the entire process, making it accessible, fast, and free from the comfort of your home.

Features

<img width="730" height="904" alt="3" src="https://github.com/user-attachments/assets/b2e1f204-b5c9-4422-aaf5-c8d726050efa" />

Automatic Background Removal: Integrates with the remove.bg API to instantly and cleanly remove the background from any photo.

Country-Specific Sizing: Pre-configured dimensions for different countries (e.g., USA, Bangladesh) to ensure compliance.

Custom Background Color: Users can choose from a palette of compliant background colors (White, Off-White, Light Blue).

Live Color Preview: Instantly see how the photo looks with a different background color before downloading.

Responsive Design: A clean, modern, and eye-catching UI that works on all devices.

Animated Background: A subtle JavaScript animation provides a pleasant user experience.

Technology Stack

<img width="629" height="863" alt="4" src="https://github.com/user-attachments/assets/41969bf2-b752-43df-86d1-78d60ba4cd36" />

Backend: Python, Django Framework

Frontend: HTML, CSS, JavaScript
-- Image Processing: Pillow (Python Imaging Library)

External APIs: remove.bg API for background removal.

Setup and Installation

Follow these steps to get a local copy of the project up and running.

Prerequisites

Python 3.8+

pip package manager

Git

1. Clone the Repository
code
Bash
download
content_copy
expand_less

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to keep dependencies isolated.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies

First, create a requirements.txt file from the packages you've installed.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip freeze > requirements.txt

Now, anyone (including you on a new machine) can install the required packages.```bash
pip install -r requirements.txt

code
Code
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
### 4. Set Up Environment Variables

This project requires an API key from `remove.bg`. To keep it secure, we will use environment variables.

**a.** Create a file named `.env` in the root directory of your project (the same level as `manage.py`).

**b.** Add your API key to the `.env` file:

REMOVE_BG_API_KEY="your_actual_api_key_from_remove.bg"

code
Code
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
**c.** **Important:** Add `.env` to your `.gitignore` file to prevent your secret keys from being pushed to GitHub. If you don't have a `.gitignore` file, create one and add this line to it:

.env

code
Code
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
_Note: The current code has the API key hardcoded in `views.py`. For best practice, you should update your code to read the key from the environment. This involves installing `python-dotenv`, loading it in your settings, and accessing the key with `os.environ.get('REMOVE_BG_API_KEY')`._

### 5. Run Django Migrations

Apply the initial database migrations.
```bash
python manage.py migrate
6. Run the Development Server

You're all set! Start the server.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python manage.py runserver

The application will be available at http://127.0.0.1:8000/.

Usage

Navigate to the homepage.

Select the desired country standard from the dropdown menu.

Click the file input area to upload a photo from your device.

Click the "Create My Photo" button.

You will be taken to the result page, where your photo is shown with the background removed.

Select a new background color and click "Preview Color" to see the change.

Once you are satisfied, click "Download Final Photo" to save the compliant passport photo as a high-quality JPEG.

License

This project is licensed under the MIT License. See the LICENSE file for details.

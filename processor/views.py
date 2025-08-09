# processor/views.py

from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from PIL import Image, ImageOps
import io
import base64

# --- IMPORTANT: PASTE YOUR REMOVE.BG API KEY HERE ---
REMOVE_BG_API_KEY = "QU4Qd93K25ycWMKnVVZ5aFuP"

# --- Passport Specifications (no changes) ---
PASSPORT_SPECS = {
    "bd": { "name": "Bangladesh", "width": 531, "height": 648 },
    "us": { "name": "USA", "width": 600, "height": 600 },
}

# --- Color Mapping (no changes) ---
COLOR_MAP = {
    "white": (255, 255, 255),
    "off-white": (245, 245, 245),
    "light-blue": (230, 240, 255),
}


def passport_photo_view(request):
    if request.method == 'POST':
        action = request.POST.get('action', 'upload')
        country_code = request.POST.get('country', 'us')
        specs = PASSPORT_SPECS.get(country_code, PASSPORT_SPECS['us'])

        if action == 'upload':
            if 'image' not in request.FILES:
                return HttpResponse("No image file was uploaded.")
            
            original_image_file = request.FILES['image']

            print("Sending original image to remove.bg...")
            try:
                removebg_response = requests.post(
                    'https://api.remove.bg/v1.0/removebg',
                    files={'image_file': original_image_file},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': REMOVE_BG_API_KEY},
                )
                removebg_response.raise_for_status()

                image_data_base64 = base64.b64encode(removebg_response.content).decode('utf-8')
                context = {
                    'image_data_base64': image_data_base64,
                    'color_name': 'white',
                    'color_hex': '#FFFFFF',
                    'country_name': country_code,
                }
                return render(request, 'result.html', context)

            except requests.exceptions.RequestException as e:
                 error_details = e.response.text if e.response else "No response from server"
                 print(f"Full error response: {error_details}")
                 return HttpResponse(f"Error communicating with remove.bg API: {e}")

        # --- THIS ELSE BLOCK IS WHERE THE CHANGES ARE ---
        else: # This handles 'preview' and 'download' actions from the result page
            image_data_base64 = request.POST.get('image_data')
            if not image_data_base64:
                return HttpResponse("Could not find image data. Please start over.")

            color_name = request.POST.get('color', 'white')
            image_data = base64.b64decode(image_data_base64)
            
            # Open the image from remove.bg
            original_image = Image.open(io.BytesIO(image_data))
            
            # --- IMPORTANT CHANGES HERE ---
            # 1. Convert to RGBA to ensure it has a proper alpha channel
            original_image = original_image.convert("RGBA")

            # 2. Crop/Fit the image
            cropped_image = ImageOps.fit(
                original_image, 
                (specs['width'], specs['height']), 
                method=Image.LANCZOS
            )

            # 3. Create the solid color background (RGB mode)
            background = Image.new('RGB', cropped_image.size, COLOR_MAP[color_name])

            # 4. Paste the cropped_image onto the background using its alpha channel as mask
            #    cropped_image.split() creates a tuple of bands (R, G, B, A)
            #    [-1] gets the last band, which is the alpha channel (the mask)
            background.paste(cropped_image, (0, 0), mask=cropped_image.split()[-1])
            # --- END IMPORTANT CHANGES ---

            if action == 'preview':
                buffer = io.BytesIO()
                background.save(buffer, format='PNG') # Save as PNG for preview to preserve transparency if any was unexpected
                final_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                context = {
                    'image_data_base64': final_image_base64,
                    'color_name': color_name,
                    'color_hex': f'#{COLOR_MAP[color_name][0]:02x}{COLOR_MAP[color_name][1]:02x}{COLOR_MAP[color_name][2]:02x}',
                    'country_name': country_code,
                }
                return render(request, 'result.html', context)

            elif action == 'download':
                response = HttpResponse(content_type='image/jpeg')
                background.save(response, 'JPEG', quality=95) # Save as JPEG for final download
                response['Content-Disposition'] = f'attachment; filename="passport_{country_code}.jpg"'
                return response

    return render(request, 'upload.html')
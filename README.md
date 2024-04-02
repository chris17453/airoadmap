# AI Adoption Roadmap Presentation Generator

This Python script generates a PowerPoint presentation based on a YAML template, outlining an AI adoption roadmap. The presentation includes various slides with content and images, adhering to a professional design.

## Requirements

- Python 3.x
- Required Python packages: `openai`, `python-pptx`, `requests`, `PIL`

## Setup

1. Install the required Python packages using pip:

   ```bash
   pip install openai python-pptx requests pillow
   ```

2. Ensure you have an OpenAI API key set up and stored as an environment variable `aitui_openai_key`.

## Usage

1. Prepare a YAML template file (`template.yaml`) defining the structure and content of the presentation. See the provided example for reference.

2. Run the script `main.py`:

   ```bash
   python main.py
   ```

3. The script will generate a PowerPoint presentation (`AI_Adoption_Roadmap.pptx`) based on the provided template.

## YAML Template Structure

The YAML template contains the following fields:

- `company_name`: Name of the company or organization.
- `author`: Author of the presentation.
- `date`: Creation date of the presentation.
- `logo_path`: File path to the company logo.
- `title`: Title of the presentation.
- `ppt_name`: Desired name for the output PowerPoint file.
- `intro_image_prompt`: Prompt for generating the introductory image.
- `intro_image`: File path to the introductory image.
- `background_image`: File path to the background image for section slides.
- `sections`: List of sections containing titles, content, and optional images for each slide.

## Features

- Generates a professional PowerPoint presentation outlining an AI adoption roadmap.
- Incorporates a company logo and introductory image.
- Utilizes IBM Plex Sans font for consistent branding.
- Customizes slide backgrounds with high-quality images.
- Supports the inclusion of images for each content section.

## Note

- Ensure all file paths (logo, images) are correctly specified in the YAML template and exist in the appropriate directories.
- The script automatically generates images using OpenAI DALL-E API if an image path is not provided for a section.

Feel free to reach out for any assistance or customization needs!

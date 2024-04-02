# PPTonator: Automated PowerPoint Presentation Builder

PPTonator is a cutting-edge tool designed to automate the creation of PowerPoint presentations using advanced natural language processing and image generation techniques. Leveraging OpenAI's powerful models, PPTonator transforms textual content into engaging, visually appealing PowerPoint slides that capture the essence of your topics.

## Features

- **Automatic Slide Generation:** Converts textual descriptions into comprehensive PowerPoint slides.
- **DALL-E Image Integration:** Utilizes DALL-E 3 for dynamic image creation, making each slide visually unique.
- **Customizable Templates:** Offers flexibility in presentation design with customizable templates.
- **Efficient Workflow:** Streamlines the presentation creation process, saving time and enhancing productivity.

## Installation

Clone the repository and install the required dependencies.

```bash
git clone https://github.com/yourgithub/pptonator.git
cd pptonator
pip install -r requirements.txt
```

## Usage

PPTonator comprises two main scripts: `build.py` for constructing the presentation and `generate.py` for creating a presentation template based on provided textual content.

### Generating a Template

Generate a YAML template specifying the presentation's structure, including titles, sections, and images.

```bash
python -m pptonator.cli generate --out <output_template.yaml>
```

### Building the Presentation

Create the PowerPoint presentation using the previously generated YAML template.

```bash
python -m pptonator.cli build --input <template.yaml> --out <presentation.pptx>
```

## Configuration

Before generating your presentation, customize the `config` section in `cli.py` to include your company name, author, presentation date, and paths to logos or background images.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## License

Distributed under the BSD 3T License. See `LICENSE` for more information.

## Acknowledgments

- OpenAI for providing the AI models that power the text and image generation.
- The Python-PPTX library for making PowerPoint automation possible.

Transform your presentation creation process with PPTonator—where innovation meets efficiency.
ccinctly introduce, guide, and inform users about the functionalities, setup, and usage of your GitHub project, PPTonator.
import argparse
from .build import create_ppt
from .generate import PptEngine

def build_ppt(args):
    create_ppt(args.input,args.out)


def build_template(args):

    config = {
        'company_name': "Watkins Labs",
        'author': 'Charles Watkins',
        'date': '2024-04-02',
        'config':args.out,
        'logo_path': 'assets/logo.png',
        'intro_image': "assets/intro.png",
        'background_image': "assets/background1.png",
    }


    PPT = "I want to talk about legacy DOS applications, their maintenance, and how they are still relevant. \
        How to service them and what the legacy support paths are."
    PPT = "I want to talk about the indecency and obsurdity surrounding whitespaces and tabs.. and why YOU are wrong. \
        "
    engine = PptEngine(config, PPT)

def main():
    parser = argparse.ArgumentParser(description="Build template and generate PowerPoint presentation")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Subparser for building template
    build_parser = subparsers.add_parser("generate", help="Generate template")
    build_parser.add_argument("--out", help="Output template file")
    build_parser.set_defaults(func=build_template)

    # Subparser for generating PowerPoint presentation
    generate_parser = subparsers.add_parser("build", help="Build PowerPoint from template")
    generate_parser.add_argument("--input", help="yaml template file")
    generate_parser.add_argument("--out", help="PPT file")
    generate_parser.set_defaults(func=build_ppt)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
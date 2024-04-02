import os
import yaml
from openai import OpenAI
import re
OPENAI_API_KEY = os.getenv('aitui_openai_key')
client = OpenAI(api_key=OPENAI_API_KEY)


class PptEngine:
    def __init__(self, config, prompt):
        self.config = config
        self.main_prompt = prompt
        self.prompts = {}
        self.sections_data = []

        self.add_prompt('system', "You are an expert editor trying to finish a ppt for work. Answer clearly and precisely.")
        self.add_prompt('title', "Below is what I want to talk about. Give me a title for this book, only output the answer\n{content}")
        self.add_prompt('sections', "Below is what you to talk about. give relivant data that people care about. not fluff.. Give me a detailed list of sections 1 per line, only output the answer\n{content}")
        self.add_prompt('content', "Below is what you to talk about. Give relivant data that people care about. we need a single slide.. just 3 or 4 bulletpoints on content for it, only output the answer\n{content}")
        self.add_prompt('image', "I need a detailed image for this topic, only output the topic image description I can use to generate a great image\n{content}")
        self.add_prompt('image_path', "give me a filename for an image based on this prompt.. keep it simple and short. it should be a png. \n{content}")
        
        self.add_prompt('calltoaction', "generate a call to action for working on , {content}")

        self.generate_presentation_structure()
        self.generate_yaml_template()

    def add_prompt(self, key, prompt):
        self.prompts[key] = prompt

    def get_prompt(self, key):
        return self.prompts[key]

    def p(self, key, data):
        #gpt-4-turbo-preview
        response = client.chat.completions.create(model="gpt-3.5-turbo", 
                                                   messages=[
                                                       {"role": "system", "content": self.get_prompt('system')},
                                                       {"role": "user", "content": self.get_prompt(key).format(content=data)}
                                                   ])
        text = response.choices[0].message.content.strip()
        return self.strip_text(text)
        
    def strip_text(self,text):
        # Remove anything before a colon (including the colon)
        text = re.sub(r'.*?:', '', text)
        
        # Remove single and double quotes
        text = text.replace("'", "").replace('"', '')
        
        # Remove HTML elements
        text = re.sub(r'<[^>]*>', '', text)
        
        # Remove double blank lines
        text = re.sub(r'\n\s*\n', '\n', text)
        
        # Remove Markdown formatting
        text = re.sub(r'[*_~`]', '', text)
        
        return text
    

    def generate_presentation_structure(self):
        self.title = self.p('title', self.main_prompt)
        self.sections = self.p('sections', self.main_prompt)
        self.calltoaction = self.p('calltoaction', self.main_prompt)
        lines = self.sections.split('\n')

        for line in lines:
            content = self.p('content', self.title + " " + line)
            image_prompt = self.p('image', self.title + "\n" + line + "\n" + content)
            image = self.p('image_path',  line )
            section = {'title': line, 'content': content, 'image_prompt': image_prompt,'image':os.path.join("assets",image)}
            self.sections_data.append(section)

    def generate_yaml_template(self):
        template = {
            "company_name": self.config['company_name'],
            "author": self.config['author'],
            "date": self.config['date'],
            "logo_path": self.config['logo_path'],
            "title": self.title,
            "intro_image": self.config['intro_image'],
            "background_image": self.config['background_image'],
            "sections": self.sections_data,
            "calltoaction": self.calltoaction
        }
        
        with open(self.config['config'], 'w') as file:
            yaml.dump(template, file, sort_keys=False)

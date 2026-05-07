class MarkdownParser:
    def __init__(self, text):
        self.text = text

    def parse_header(self):
        lines = self.text.split('\n')
        headers = []
        for line in lines:
            if line.startswith('#'):
                level = line.find(' ')
                header = line[level+1:]
                headers.append((level, header))
        return headers

    def parse_bold_text(self):
        lines = self.text.split('\n')
        bold_text = []
        for line in lines:
            if '**' in line:
                start = line.find('**')
                end = line.find('**', start+2)
                text = line[start+2:end]
                bold_text.append(text)
        return bold_text

    def parse_italic_text(self):
        lines = self.text.split('\n')
        italic_text = []
        for line in lines:
            if '*' in line:
                start = line.find('*')
                end = line.find('*', start+1)
                text = line[start+1:end]
                italic_text.append(text)
        return italic_text

    def parse_links(self):
        lines = self.text.split('\n')
        links = []
        for line in lines:
            if '[' in line and ']' in line and '(' in line and ')' in line:
                start = line.find('[')
                end = line.find(']')
                text = line[start+1:end]
                link = line[line.find('(')+1:line.find(')')]
                links.append((text, link))
        return links

    def parse_images(self):
        lines = self.text.split('\n')
        images = []
        for line in lines:
            if '![' in line and ']' in line and '(' in line and ')' in line:
                start = line.find('![')
                end = line.find(']')
                text = line[start+2:end]
                link = line[line.find('(')+1:line.find(')')]
                images.append((text, link))
        return images

    def parse_lists(self):
        lines = self.text.split('\n')
        lists = []
        for line in lines:
            if line.startswith('- ') or line.startswith('+ ') or line.startswith('* '):
                lists.append(line[2:])
        return lists

    def parse_code_blocks(self):
        lines = self.text.split('\n')
        code_blocks = []
        in_code_block = False
        code = ''
        for line in lines:
            if line.startswith('```'):
                in_code_block = not in_code_block
                if in_code_block:
                    code = ''
                else:
                    code_blocks.append(code.strip())
            elif in_code_block:
                code += line + '\n'
        return code_blocks

parser = MarkdownParser('# Header\n## Subheader\n- Item 1\n- Item 2\n**Bold text**\n*Italic text*\n[Link](https://www.example.com)\n![Image](https://www.example.com/image.jpg)\n```\ncode block\n```')
print(parser.parse_header())
print(parser.parse_bold_text())
print(parser.parse_italic_text())
print(parser.parse_links())
print(parser.parse_images())
print(parser.parse_lists())
print(parser.parse_code_blocks())
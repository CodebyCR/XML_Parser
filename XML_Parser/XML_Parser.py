import xml.etree.ElementTree as ET


class XML_Parser:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()

    def get_tag_text(self, tag_name) -> str:
        return self.root.findtext(tag_name)

    def get_tag_list(self, tag_name) -> list:
        return self.root.findall(tag_name)

    def set_tag_text(self, tag_name, new_tag_text) -> None:
        self.root.find(tag_name).text = new_tag_text
        self.tree.write(self.xml_file)

    def create_tag(self, tag_name, tag_text) -> None:
        new_tag = ET.SubElement(self.root, tag_name)
        new_tag.text = tag_text
        self.tree.write(self.xml_file)


# ================================================================


xml_parser = XML_Parser('settings.xml')

# Get tag Text
tag_text = xml_parser.get_tag_text(tag_name='Setting_1')
print("This is the tag text:", tag_text)

# Set new Text
xml_parser.set_tag_text(tag_name='Setting_1', new_tag_text='New_Setting_1')

# Print new Text
new_text = xml_parser.get_tag_text(tag_name='Setting_1')
print("This is the new tag text:", new_text)

# Create new tag
xml_parser.create_tag(tag_name='Setting_4', tag_text='New_Setting_4')

# Print new tag
new_tag_text = xml_parser.get_tag_text(tag_name='Setting_4')
print("This is the new tag text:", new_tag_text)

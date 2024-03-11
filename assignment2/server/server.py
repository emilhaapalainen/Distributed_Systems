#https://docs.python.org/3/library/xmlrpc.html
#https://docs.python.org/3/library/xml.etree.elementtree.html
#https://docs.python.org/3/library/xmlrpc.server.html

import xmlrpc.server
import xml.etree.ElementTree as ET
import datetime

class Server:
    def __init__(self):
        self.db = 'db.xml'
        try:
            self.tree = ET.parse(self.db)
            self.root = self.tree.getroot()
        except ET.ParseError:
            self.root = ET.Element('root')
            self.tree = ET.ElementTree(self.root)
            self.tree.write(self.db)

    def newNote (self, topic, name, text):
        note = ET.SubElement(topic, 'note', {'name': name})
        ET.SubElement(note, 'text').text = text
        ET.SubElement(note, 'time').text = str(datetime.datetime.now())
    
    def appendNote (self, noteTopic, name, text):
        topic = self.getTopic(noteTopic)
        if not topic:
            topic = ET.SubElement(self.root, 'topic', {'name': noteTopic})

        self.newNote(topic, name, text)
        self.tree.write(self.db)
        return "Note added."
    
    def getTopic (self, topic):
        for child in self.root.findall('topic'):
            if child.get('name') == topic:
                return child
        return ''
    
    def getNotes (self, topic):
        found = []
        search = self.getTopic(topic)
        if not search:
            return found
        
        for note in search.findall('note'):
            found.append({'name': note.get('name'), 'text': note.find('text').text, 'time': note.find('time').text})
        return found
    
if __name__ == "__main__":
    server = Server()
    server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
    server.register_instance(Server())
    server.serve_forever()
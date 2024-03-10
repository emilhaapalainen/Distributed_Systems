import xmlrpc.server
import datetime
import xml.etree.ElementTree as ET

class Server:
    def __init__(self):
        self.db = 'db.xml'
        try:
            self.tree = ET.parse(self.db)
            self.root = self.tree.getroot()
        except ET.ParseError:
            self.root = ET.Element('root')
            self.tree = ET.ElementTree(self.root)

    def newNote (self, topic, text):
        return
    
    def getNotes (self, topic):
        return
    
if __name__ == "__main__":
    server = Server()
    server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
    server.register_instance(Server())
    server.serve_forever()
import xml.sax


class ModelNameHandler(xml.sax.ContentHandler):
    ENTITY_TAG = "GeographicalArea"
    inGeoTag = False

    def __init__(self):
        self.entity_code = None
        self.entity_names = {}
        self.attr_names = {}

    def startElement(self, tag, attributes):
        if tag == self.ENTITY_TAG:
            inGeoTag = True
        else:
            pass

    def endElement(self, tag):
        if tag == self.ENTITY_TAG:
            inGeoTag = False
            a = 1

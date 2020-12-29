from lxml import etree
import os
import sys
import xml.sax
from ModelNameHandler import ModelNameHandler

def main():
    filename = "kenya.xml"
    filename = os.path.join("import", filename)
    ret = get_model_names(filename)
    a = 1

def get_model_names(file):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = ModelNameHandler()
    parser.setContentHandler(handler)
    parser.parse(file)

    return handler.entity_names, handler.attr_names

if __name__ == "__main__":
    main()

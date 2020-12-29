import xml.sax


class ModelNameHandler(xml.sax.ContentHandler):
    ENTITY_TAG = "GeographicalArea"
    STORAGE_TABLE_NAME_ATTR = "storageTableName"
    TABLE_NAME_ATTR = "tableName"
    ATTRIBUTE_TAG = "attribute"
    STORAGE_FIELD_NAME_ATTR = "storageFieldName"
    FIELD_NAME_ATTR = "fieldName"

    inGeoTag = False

    def __init__(self):
        self.entity_code = None
        self.entity_names = {}
        self.attr_names = {}

    def startElement(self, tag, attributes):
        if tag == self.ENTITY_TAG:
            inGeoTag = True
            a = 2
            # self.entity_code = attributes[self.STORAGE_TABLE_NAME_ATTR]
            # entity_name = attributes[self.TABLE_NAME_ATTR]
            # self.entity_names[self.entity_code] = entity_name
        # elif tag == self.ATTRIBUTE_TAG:
        #     attr_code = attributes[self.STORAGE_FIELD_NAME_ATTR]
        #     key = self.entity_code + "." + attr_code
        #     attr_name = attributes[self.FIELD_NAME_ATTR]
        #     self.attr_names[key] = attr_name
        else:
            a = 1

    def endElement(self, tag):
        if tag == self.ENTITY_TAG:
            inGeoTag = False
            a = 1

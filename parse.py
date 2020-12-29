from lxml import etree
import xml.etree.ElementTree as ET
import os


def parseXML(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    f = open("hjid_to_sid_map.txt", "w+")
    f2 = open("hjid_member_map.txt", "w+")
    f.write('"hjid","sid"\n')
    f2.write('"membership_hjid","member_hjid","parent_hjid","parent_sid"\n')

    # Get the hjids for the geographical areas
    for geo in root.findall('.//GeographicalArea'):
        hjid = geo.find("hjid").text
        sid = geo.find("sid").text
        f.write(str(hjid) + "," + str(sid) + "\n")
        # Get the hjids for the geographical area memberships
        for member in geo.findall('geographicalAreaMembership'):
            membership_hjid = member.find("hjid").text
            geographicalAreaGroupSid = member.find("geographicalAreaGroupSid").text
            f2.write(str(membership_hjid) + "," + str(geographicalAreaGroupSid) + "," + str(hjid)  + "," + str(sid) + "\n")

    # Close the files
    f.close()
    f2.close()

if __name__ == "__main__":
    filename = "cds_partsab.xml"
    filename = os.path.join("import", filename)
    parseXML(filename)

#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    sys.exit(1)

config_xml = sys.argv[1]


def get_child(element, tag):
    result = element.findall(tag)
    assert len(result) == 1
    return result[0]


tree = ET.parse(config_xml)
root = tree.getroot()
get_child(root, "useSecurity").text = "false"
tree.write(config_xml)


#XML inside Python
import xml.etree.ElementTree as ET

def xmlEx1():
    #   The XML:
    data = '''<person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

    # Parse a string of data
    tree = ET.fromstring(data)                      #NOTE: you could find many child attributes
    print('Name:', tree.find('name').text)          #Only one text attribute (Chuck)
    print('Attr:', tree.find('email').get('hide'))  #Many child attributes, so specify with get()
                                                    # Other child attributes are type= and hide=
#xmlEx1()

def XMLExample2():
    #   The XML:
    input = '''<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>        
    </stuff>'''
    #Parse string of data
    stuff = ET.fromstring(input)
    lst = stuff.findall('users/user')
    print('User count:', len(lst))
    for item in lst:
        print('Name:', item.find('name').text)
        print('ID:', item.find('id').text)
        print('Attribute:', item.get('x'))
XMLExample2()

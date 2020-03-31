"""
<column caption='Donut5' datatype='integer' name='[Calculation_399976008987545603]' r

caption
name
formula
"""


import csv
import xml.etree.ElementTree as ET


def main():
    write_this_lst = []
    tree = ET.parse('in.xml')
    root = tree.getroot()

    # init csv file
    with open('out.csv', 'w') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerow(['caption', 'name', 'formula'])
    
    for child in root:
        # print(child.tag, child.attrib)
        if child.tag == 'datasources':
            for datasource in child:
                for column in datasource:
                    if column.tag == 'column':
                        if '[Calculation_' in column.attrib['name']:
                            # print('#############')
                            caption = column.attrib['caption']
                            name = column.attrib['name']
                            for calculation in column:
                                formula = calculation.attrib['formula']
                            with open('out.csv', 'a') as out_csv:
                                writer = csv.writer(out_csv)
                                writer.writerow([caption, name, formula])

if __name__ == '__main__':
    main()
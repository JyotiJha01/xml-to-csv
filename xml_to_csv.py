import xml.etree.ElementTree as ET
import pandas as pd 
import glob
from pathlib import Path
import os

# collecting all the xml files
p = Path('.')
xml_files = list(p.glob('data/*.xml'))

# creating a directory to store the csv files
if not os.path.exists('data/output'):
    os.makedirs('data/output')

for n in range(len(xml_files)):
    # parse the xml file
    tree =ET.parse(str(xml_files[n]))
    root =tree.getroot()

    main_tag = []
    for child in root:
        main_tag.append(child.tag)
    pyld = root.find(main_tag[1])


    all_FinInstrm = []   
    for i in pyld[0][0]:
        all_FinInstrm.append(i)

    one_fin = all_FinInstrm[1]


    # collecting all the tags
    all_data = []
    for rcrd in all_FinInstrm[1:]:
        temp = []
        temp.append(rcrd[0][0][0].text)
        temp.append(rcrd[0][0][1].text)
        temp.append(rcrd[0][0][3].text)
        temp.append(rcrd[0][0][4].text)
        temp.append(rcrd[0][0][5].text)
        temp.append(rcrd[0][1].text)
        all_data.append(temp)

    # saving the data in a csv file
    cols = ["Id", "FullNm", "ClssfctnTp", "NtnlCcy", "CmmdtyDerivInd", "Issr"]
    df = pd.DataFrame(all_data, columns=cols)
    df.to_csv('data/output/{}.csv'.format(xml_files[n].stem, index=False))

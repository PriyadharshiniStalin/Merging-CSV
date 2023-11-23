import csv
from collections import OrderedDict

filenames = "C:\Users\pstalin\Downloads\_Cat_9K_user_inputs_mgmtintf_513.csv", "C:\Users\pstalin\Downloads\9300_logging_mgmt_src.csv"
data = OrderedDict()
fieldnames = []
for filename in filenames:
    with open(filename, "rb") as fp: # python 2
        reader = csv.DictReader(fp)
        fieldnames.extend(reader.fieldnames)
        for row in reader:
            data.setdefault(row["Device"], {}).update(row)

fieldnames = list(OrderedDict.fromkeys(fieldnames))
with open("merged2.csv", "wb") as fp:
    writer = csv.writer(fp)
    writer.writerow(fieldnames)
    for row in data.itervalues():
        writer.writerow([row.get(field, '') for field in fieldnames])
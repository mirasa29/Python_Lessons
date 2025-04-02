import os

infiledir = f"{os.path.abspath(os.curdir)}/in"
outfiledir = f"{os.path.abspath(os.curdir)}/out"

# with open('/Users/mirasa/PycharmProjects/pythonProject/Notes.txt', 'r', encoding='utf-8') as file:
#     t = '|'.join([l.strip() for l in file if l.startswith('samp_str')])
#
#     with open(outfile, 'w', encoding='utf-8') as out:
#         out.write(t)


# with open(f'{infiledir}/sample_in.txt', 'r', encoding='utf-8') as file:
#         our_var = ''.join([l.upper() for l in file])
#
#         with open(f'{outfiledir}/outfile', 'w', encoding='utf-8') as out:
#             out.write(our_var)


#####################################################################

# import csv
#
# with open(f'{infiledir}/dutton_family.csv', 'r', encoding='utf-8') as csvfile:
#     try:
#         reader = csv.reader(csvfile)
#     except csv.Error as e:
#         print(f'file {csvfile} could not be read: {e}')
#         exit(1)
#
#     with open(f'{outfiledir}/out_dutton_family.csv', 'w', newline='', encoding='utf-8') as outfile:
#         writer = csv.writer(outfile)
#         for row in reader:
#             writer.writerow([r.upper() for r in row])


#####################################################################

import json

with open(f'{infiledir}/yellowstone_series.json', 'r', encoding='utf-8') as jsonfile:
    try:
        data = json.load(jsonfile)
    except json.JSONDecodeError as e:
        print(f'file {jsonfile} could not be read: {e}')
        exit(1)

    with open(f'{outfiledir}/out_yellowstone_series.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)


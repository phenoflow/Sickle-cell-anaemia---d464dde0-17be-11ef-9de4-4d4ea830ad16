# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"K0G..00","system":"readv2"},{"code":"D106z00","system":"readv2"},{"code":"F422100","system":"readv2"},{"code":"D106.00","system":"readv2"},{"code":"D106000","system":"readv2"},{"code":"D104211","system":"readv2"},{"code":"32937.0","system":"readv2"},{"code":"93872.0","system":"readv2"},{"code":"31370.0","system":"readv2"},{"code":"8119.0","system":"readv2"},{"code":"31075.0","system":"readv2"},{"code":"69964.0","system":"readv2"},{"code":"48295.0","system":"readv2"},{"code":"57397.0","system":"readv2"},{"code":"31306.0","system":"readv2"},{"code":"23519.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('sickle-cell-anaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["sicklecell---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["sicklecell---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["sicklecell---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

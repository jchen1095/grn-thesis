import csv

def process_gene_data(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, \
         open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=',')
        writer = csv.writer(outfile)
        # Optional header:
        # writer.writerow(['affector','target'])

        for row in reader:
            if len(row) < 2:
                continue
            target = row[0]
            try:
                nregs = int(row[1])
            except ValueError:
                continue
            # regulators are the next nregs entries
            regs = row[2:2 + nregs]
            for reg in regs:
                writer.writerow([reg, target])

# Example usage:
input_filename  = "gene_interactions.txt"
output_filename = "grn_gt_test.csv"
process_gene_data(input_filename, output_filename)

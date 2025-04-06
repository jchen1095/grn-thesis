import csv

def process_gene_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=',')  # delim for txt
        writer = csv.writer(outfile)
        # writer.writerow(["target_gene", "targeting_gene"])
        
        for row in reader:
            if len(row) >= 3:
                target_gene = row[0]
                targeting_gene = row[2]
                writer.writerow([target_gene, targeting_gene])

# Example usage:
input_filename = "./data/input/differentiation_input_GRN.txt"  
output_filename = "differentiation_input_GRN_Gt.csv"
process_gene_data(input_filename, output_filename)

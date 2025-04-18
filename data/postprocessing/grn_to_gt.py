import csv

#To generate the csv of gene interactions in the format of target, affector gene
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
input_filename = "./data/input/perturbed_matrix.txt"  
output_filename = "./data/input/artificial/grn_gt_test.csv"
process_gene_data(input_filename, output_filename)

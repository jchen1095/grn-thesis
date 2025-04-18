# Makes sure that a txt file is tab-delimited.


input_filename = 'perturbed_matrix.txt'
output_filename = 'only_tabs.txt'

# Open the input file and read all its lines.
with open(input_filename, 'r') as infile:
    lines = infile.readlines()

# Open the output file for writing.
with open(output_filename, 'w') as outfile:
    for line in lines:
        # Remove extra whitespace at the beginning or end,
        # then split the line by any whitespace (both spaces and tabs).
        fields = line.strip().split()
        # Join the fields with a tab ("\t") as the delimiter.
        new_line = "\t".join(fields)
        outfile.write(new_line + "\n")

print(f"New file '{output_filename}' created with only tab delimiters.")

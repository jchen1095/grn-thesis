import os
import sys

def csv_to_txt(input_csv, output_txt):
    with open(input_csv, 'r') as csv_file, open(output_txt, 'w') as txt_file:
        for line in csv_file:
            txt_file.write(line.replace(',', ' '))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python csv_to_txt_parse.py <input_csv>")
        sys.exit(1)

    input_csv = sys.argv[1]

    output_dir = "./data"
    os.makedirs(output_dir, exist_ok=True)

    # Generate an appropriate output filename
    base_name = os.path.splitext(os.path.basename(input_csv))[0]
    output_txt = os.path.join(output_dir, f"{base_name}.txt")

    csv_to_txt(input_csv, output_txt)
    print(f"Conversion complete. Output saved to {output_txt}")

# import os
# print("Current Working Directory:", os.getcwd())

# def csv_to_txt(input_csv, output_txt):
#     with open(input_csv, 'r') as csv_file, open(output_txt, 'w') as txt_file:
#         for line in csv_file:
#             txt_file.write(line.replace(',', ' '))

# # Example usage

# input_csv = './SERGIO/data_sets/De-noised_100G_3T_300cPerT_dynamics_8_DS8/simulated_noNoise_S_0.csv'  # Replace with your CSV file
# output_txt = 'output.txt'  # Replace with your desired TXT file
# csv_to_txt(input_csv, output_txt)
# print('done')


#questions for wenjun: 
#what is the meaning of all of these instances of simulated csvs? are they all for the same grn and am i supposed to simulate all of them?
#help me figure out wt is going on w sergio
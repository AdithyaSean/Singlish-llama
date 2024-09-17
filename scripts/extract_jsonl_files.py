def copy_first_200_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for i, line in enumerate(infile):
            if i >= 200:
                break
            outfile.write(line)

input_file = input("Name of your input file: ")
output_file = input("Name of your output file: ")

copy_first_200_lines(input_file, output_file)
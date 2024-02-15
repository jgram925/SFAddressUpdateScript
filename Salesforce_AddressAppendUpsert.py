def modify_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Read lines from input file
        lines = infile.readlines()

        # Modify the header
        header = lines[0].strip().split(',')
        # Exclude column headers b, c, and f
        modified_header = [header[i] for i in range(len(header)) if i not in [1, 2, 7]] 
        outfile.write(','.join(modified_header) + '\n')

        # Process each row and write the modified rows to the output file
        for line in lines[1:]:
            row = line.strip().split(',')

            # Capitalize columns d and e
            row[3] = row[3].title()
            row[4] = row[4].title()

            # Convert state abbreviation to state name
            state_abbreviations = {
                'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
                'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
                'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
                'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts',
                'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
                'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
                'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
                'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
                'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
                'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
            }
            row[5] = state_abbreviations.get(row[5], row[5])

            # Combine columns g and h with a dash in between
            combined_g_h = f'{row[6]}-{row[7]}'
            # Exclude data from columns b, c, g, h
            row = [row[i] for i in range(len(row)) if i not in [1, 2, 6, 7]]
            row.append(combined_g_h)

            # Write the modified row to the output file
            outfile.write(','.join(row) + '\n')

# Modify input and output paths
input_file_path = 'C:\\Users\\jgram\\OneDrive\\Desktop\\Feb24_AddressAppend.csv'
output_file_path = 'C:\\Users\\jgram\\OneDrive\\Desktop\\output.csv'
modify_csv(input_file_path, output_file_path)

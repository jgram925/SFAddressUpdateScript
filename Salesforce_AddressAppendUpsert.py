def modify_and_split_csv(input_file, output_prefix, max_records_per_file=2000):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

        header = lines[0].strip().split(',')
        modified_header = [header[i] for i in range(len(header)) if i not in [1, 2, 7]]
        modified_header.append("Country")

        current_file_index = 1
        current_records_count = 0

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
            country = 'United States'
            row = [row[i] for i in range(len(row)) if i not in [1, 2, 6, 7]]
            row.append(combined_g_h)
            row.append(country)

            # Write the modified row to the current output file
            if current_records_count == 0:
                current_output_file = f"{output_prefix}_{current_file_index}.csv"
                with open(current_output_file, 'w') as outfile:
                    outfile.write(','.join(modified_header) + '\n')

            with open(current_output_file, 'a') as outfile:
                outfile.write(','.join(row) + '\n')

            current_records_count += 1

            # If the maximum records per file is reached, reset count and move to the next file
            if current_records_count >= max_records_per_file:
                current_file_index += 1
                current_records_count = 0

# Example usage
input_file_path = 'C:\\Users\\jgram\\OneDrive\\Desktop\\Feb24_AddressAppend.csv'
output_file_prefix = 'C:\\Users\\jgram\\OneDrive\\Desktop\\output'
modify_and_split_csv(input_file_path, output_file_prefix)

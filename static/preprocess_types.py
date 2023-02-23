import csv, json
FILE_NAME = "typing_chart.csv"

# Creates JSON file that maps each type to pokemon they are super effective attacking against
data = {}

def preprocess(file_name):
    """
    Reads CSV with `file_name` and parses the data into the global `data` dictionary.
    """
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row["\ufeffTypes"]] = []
            for key, value in row.items():
                try: 
                    val = int(value)
                    if val == 2:
                        data[row["\ufeffTypes"]].append(key)
                except:
                    pass
                
    
preprocess(FILE_NAME)

# Writing to data.json          
json_object = json.dumps(data, indent=4)
with open("types_data.json", "w") as outfile:
    outfile.write(json_object)
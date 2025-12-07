# "r" = read mode, "w" = write mode (overwrites), "a" = append mode
#with open("data.txt", "r", encoding="utf-8") as f:
#    data = f.read() 
#    # File closes automatically here
#
#with open("huge_log_file.txt", "r") as f:
#    for line in f:
#        # process one line at a time
#        print(line.strip()) 
#
users = []

with open("users.csv", "r") as f:
    # 1. Read the header separately (moves the pointer to line 2)
    header = f.readline().strip().split(",")
    
    # 2. Loop through the rest
    for line in f:
        # Strip newline characters (\n) and split by comma
        parts = line.strip().split(",")
        
        # Convert to a dictionary for safety
        row = {
            "id": int(parts[0]),
            "name": parts[1],
            "role": parts[2]
        }
        users.append(row)

print(users)
# [{'id': 1, 'name': 'Jonas', 'role': 'Admin'}, ...]

product_list = []
with open("csv_content.csv", "r") as f:
    header = f.readline().strip().split(",")

    for line in f:
        parts = line.strip().split(",")

        row = {
            "product": (parts[0]),
            "Price": float(parts[1]),
            "Currency": parts[2]
        }
        product_list.append(row)

print(product_list)

error_file_content = []
with open("task2Reading.csv", "r") as f:
    for line in f:
        line_splited = line.strip().split(",")

        if line_splited[0].startswith("ERROR:"):
            error_file_content.append(line)
print(error_file_content)

raw_text = "line1\nline2\nline3"

def read_lines(text):
    lines = text.strip().split("\n")
    
    for line in lines:
        yield line 

my_generator = read_lines(raw_text)

for item in my_generator:
    print(f"Processing: {item}")
# Task: Fix this code so it actually runs
def clean_data(raw_list):
    clean = []
    for item in raw_list:
        
        # 1. Check if item is NOT None and NOT empty string
        # 2. Clean whitespace (strip)
        # 3. Convert to Title Case
        if item != None and item != "":
            string = str(item).strip()
            lower = string.lower()
            final = lower.title()
            clean.append(final)
    return clean

test_data = ["  vilnius ", None, "KAUNAS", ""]
print(clean_data(test_data)) 
# Goal output: ['Vilnius', 'Kaunas']
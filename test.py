# pip install fuzzywuzzy python-Levenshtein

# from fuzzywuzzy import fuzz(use when you want to compare input string to single string)
# from fuzzywuzzy import process(use when you want to compare input string to multiple string))

from fuzzywuzzy import process

def get_property_summary(user_input):#, database_path="your_database.db"
    # conn = sqlite3.connect(database_path)
    # cursor = conn.cursor()

    # cursor.execute("SELECT property_name FROM properties")
    property_names = ["Aishwar property","Agarwal Property"]

    best_match, score = process.extractOne(user_input, property_names)

    return best_match,score
# Example usage:
user_input = "please give brief information about Aaesuar property"
matched_name, summary = get_property_summary(user_input)

if matched_name:
    print(f"Matched property: {matched_name}")
    print(f"Summary: {summary}")
else:
    print(summary)

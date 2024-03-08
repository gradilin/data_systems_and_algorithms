import json


def check_status(string): 
    if string.isalnum() and string == string.lower(): 
        return True 
    return False 

def check_build_id(string): 
    if string[0:2] == "b_" and len(string) == 9: 
        return True 

# Define the list of builds as a Python list of dictionaries
builds = [
  '{"buildName": "b_232dhj1", "buildResult": "success"}',
  '{"buildName": "b_232dwaf", "buildResult": "failure"}',
  '{"buildName": "b_232dwaf"}',
  '{"buildName": "b_2323dwg", "buildResult": "success"}',
  '{"buildName": "b_2363321", "buildResult": "failure"}'
]

# # Convert the Python list of dictionaries into a JSON string
# json_string = json.dumps(builds)

# s = "yourstring"  # Replace 'yourstring' with the actual string you want to check
# is_lowercase_alphanumeric = s.isalnum() and s == s.lower()

success = 0 
failed = 0 
errors = 0 

for x in builds: 
    build = json.loads(x)
    # check for values 
    if 'buildName' in build.keys() and 'buildResult' in build.keys():  
        name = build['buildName']
        result = build['buildResult']
        if check_build_id(name) and check_status(result): 
            if result in ("success", "failure"): 
                if result == "success": 
                    success += 1    
                else:
                    failed += 1 
            else: 
                errors += 1 
    else: 
        errors += 1 
results = [success, failed, errors]

print(results)

import os
import re
import sys
def count_potential_in_files(directory):
    total_count = 0
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check for .c or .cpp files
            if file.endswith('.c') or file.endswith('.cpp'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Count occurrences of "POTENTIAL" (case insensitive)
                        count=0
                        count += len(re.findall(r'POTENTIAL', content, re.IGNORECASE))
                        #count += len(re.findall(r'FLAW', content, re.IGNORECASE))
                        #count -= len(re.findall(r'POTENTIAL FLAW', content, re.IGNORECASE))
                        total_count += count
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return total_count

# Specify the directory you want to search
directory_path=sys.argv[1]
#/home/perry/git_repos/juliet-test-suite-c/testcases/CWE122_Heap_Based_Buffer_Overflow
#/home/perry/git_repos/juliet-test-suite-c/testcases/CWE835_Infinite_Loop 
#/home/perry/git_repos/juliet-test-suite-c/testcases/CWE127_Buffer_Underread 
#/home/perry/git_repos/juliet-test-suite-c/testcases/CWE134_Uncontrolled_Format_String
#/home/perry/git_repos/juliet-test-suite-c/testcases/CWE190_Integer_Overflow 

total_occurrences = 0

for d in os.listdir(directory_path):

    total_occurrences+=count_potential_in_files(os.path.join(directory_path,d))
print(f'Total occurrences of "POTENTIAL" or "FLAW": {total_occurrences}')
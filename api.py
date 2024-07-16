import os
import anthropic 
from typing import List 
import subprocess 


language_mapping = {
    '.py': 'Python',
    '.rs': 'Rust',
    '.c': 'C',
    '.sol': 'Solidity'
}


client = anthropic.Anthropic( api_key="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", ) 

def read_file_content(filename: str) -> str: 
    with open(filename, 'r') as file: 
        return file.read() 

def save_file(filename: str, content: str): 
    with open(filename, 'w') as file: 
        file.write(content) 

# Take inputs from the user 

input_file = input("Enter the path to input file: ")
_, file_extension = os.path.splitext(input_file)

if file_extension in language_mapping:
    language = language_mapping[file_extension]
    if language == 'Python':
        system_prompt = "Python to Zokrates, and mention whether the input is private or not, and remember default type is field in zokrates, and remember that main function is the only function in zokrates for whichever name in python, and instead of scoping the function in curly braces, use colon and no semi-colon after return, and return the the zokrates code in a code block"
    elif language == 'Rust':
        system_prompt = "Rust to Zokrates, and mention whether the input is private or not, and remember default type is field in zokrates, and remember that main function is the only function in zokrates for whichever name in rust, and instead of scoping the function in curly braces, use colon and no semi-colon after return, and return the the zokrates code in a code block"
    elif language == 'C':
        system_prompt = "C to Zokrates, and mention whether the input is private or not, and remember default type is field in zokrates, and remember that main function is the only function in zokrates for whichever name in C, and instead of scoping the function in curly braces, use colon and no semi-colon after return, and return the the zokrates code in a code block"
    elif language == 'Solidity':
        system_prompt = "Solidity to Zokrates, and mention whether the input is private or not, and remember default type is field in zokrates, and remember that main function is the only function in zokrates for whichever name in C, and instead of scoping the function in curly braces, use colon and no semi-colon after return, and return the the zokrates code in a code block"
else:
    print(f"Unsupported file extension: {file_extension}")
    exit()

file1_zok_pin = input("Enter the path to file1.zok.pin: ") 
file1_zok_vin = input("Enter the path to file1.zok.vin: ") 
# Read file contents 
input_py_content = read_file_content(input_file) 
file1_zok_pin_content = read_file_content(file1_zok_pin) 
file1_zok_vin_content = read_file_content(file1_zok_vin) 
input_py_filename = "input.py" 
file1_zok_pin_filename = "output.zok.pin" 
file1_zok_vin_filename = "output.zok.vin" 
save_file(input_py_filename, input_py_content) 
save_file(file1_zok_pin_filename, file1_zok_pin_content) 
save_file(file1_zok_vin_filename, file1_zok_vin_content) 
message = client.messages.create( 
            model="claude-3-opus-20240229", 
            max_tokens=1000, 
            temperature=0.0, 
            system="Python to Zokrates, and mention wherether the input is private or not, and remember default type is field in zokrates, and rememeber that main function is the only function in zokrates for whichever name in python, and instead of scoping the function in curly braces, use colon and no semi-colon after return, and return the the zokrates code in a code block", 
            messages=[ {"role": "user", "content": input_py_content}, ] ) 
print(message.content)
class ContentBlock: 
    def __init__(self, text: str, type: str): 
        self.text = text 
        self.type = type 
    # def extract_zokrates_code(output: List[ContentBlock]) -> str: # for block in output: # if isinstance(block, ContentBlock) and block.type == 'text': # if '```zokrates' in block.text: # return block.text.split('```zokrates\n')[1].split('\n```')[0] # return '' 
def save_zokrates_code(zokrates_code: str, filename: str): 
    with open(filename, 'w') as f: 
        f.write(zokrates_code)
output = message.content 
# Iterate over the output 
for block in output: 
    # Check if the block type is 'text' 
    if block.type == 'text': 
    # Extract Zokrates code 
        zokrates_code = block.text.split('```zokrates\n')[1].split('\n```')[0] 
# Write Zokrates code to a file 
with open('output.zok', 'w') as f: 
    f.write(zokrates_code)
# zokrates_code = extract_zokrates_code(output) 
if zokrates_code: 
    save_zokrates_code(zokrates_code, 'output.zok') 
    print("Zokrates code saved to 'output.zok'") 
else: 
    print("No Zokrates code found in the output.") 
    
subprocess.run(["chmod", "+x", "./cli.sh"]) 
    # Change permissions 
subprocess.run(["./cli.sh", "output.zok", file1_zok_pin_filename, file1_zok_vin_filename]) 
    # Build project using Cargo 
subprocess.run(["cargo", "build", "--release", "--features", "smt,bellman,zok,poly", "--examples", "--verbose"]) 
    # Run the zokrates_test.zsh script 
subprocess.run(["./scripts/zokrates_test.zsh"])
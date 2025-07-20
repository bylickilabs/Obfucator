import base64
import re
import sys
import random
import string

def generate_obfuscated_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def obfuscate_variables(code):
    variables = set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\b", code))
    blacklist = {"def", "return", "import", "as", "from", "if", "else", "for", "while", "with", "try", "except", "True", "False", "None", "class", "print", "open", "in", "not", "is", "and", "or", "self"}
    mapping = {}
    for var in variables:
        if var not in blacklist and not var.startswith("__") and len(var) > 2:
            mapping[var] = generate_obfuscated_name()
    for orig, obf in mapping.items():
        code = re.sub(rf"\b{orig}\b", obf, code)
    return code

def remove_whitespace_and_comments(code):
    lines = code.splitlines()
    stripped = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            stripped.append(line)
    return " ".join(stripped)

def base64_encode(code):
    encoded = base64.b64encode(code.encode("utf-8")).decode("utf-8")
    wrapper = f"""
import base64
exec(base64.b64decode("{encoded}").decode("utf-8"))
"""
    return wrapper.strip()

def obfuscate_file(input_path, output_path, use_base64=True):
    with open(input_path, "r", encoding="utf-8") as f:
        code = f.read()

    code = obfuscate_variables(code)
    code = remove_whitespace_and_comments(code)

    if use_base64:
        code = base64_encode(code)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"[✓] Obfuscated file saved as: {output_path}")

# Beispiel-Nutzung:
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python obfuscator.py input.py output.py [--nobase64]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    base64_enabled = "--nobase64" not in sys.argv

    obfuscate_file(input_file, output_file, use_base64=base64_enabled)

# 🔐 Python Obfuscator – Lightweight CLI Tool

A simple yet effective tool to obfuscate Python source code by renaming variables, stripping comments and whitespace, and optionally wrapping the result in Base64 encoding. Ideal for developers who want basic code protection or reduced readability of Python scripts.

---

## ✅ Features

- **Variable Obfuscation**  
  Replaces variable names with randomized, meaningless identifiers.

- **Whitespace & Comment Removal**  
  Cleans up the code to make it more compact and less readable.

- **Base64 Encoding (Optional)**  
  Encapsulates the script using `exec(base64.b64decode(...))` for an extra layer of obfuscation.

- **No Dependencies**  
  Pure Python implementation using only standard libraries.

- **CLI Friendly**  
  Simple usage with command-line parameters.

---

## 🛠️ Usage

```yarn
python obfuscator.py input.py output.py
python obfuscator.py input.py output.py --nobase64
```

---

## License

This project is licensed under the MIT License.  
See MIT [LICENSE](LICENSE) for details.

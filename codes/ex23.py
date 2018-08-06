import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline()
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)
def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<==>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# When you have bytes and need a string, decode bytes. When you have a string and need bytes, encode strings.

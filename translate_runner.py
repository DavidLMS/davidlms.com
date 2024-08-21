import sys
from aphra import translate

def main():
    config_file = sys.argv[1]
    source_language = sys.argv[2]
    target_language = sys.argv[3]
    input_file = sys.argv[4]
    output_file = sys.argv[5]

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    translated_text = translate(
        source_language=source_language,
        target_language=target_language,
        text=text,
        config_file=config_file
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_text)

if __name__ == "__main__":
    main()
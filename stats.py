def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(file_path):
    file_contents = get_book_text(file_path)
    words_counter = len(file_contents.split())
    # print(f'{words_counter} words found in the document')
    return words_counter

def get_num_char(file_path):
    file_contents = get_book_text(file_path)
    char_report = {}
    for c in file_contents:
        c_lowercase = c.lower()
        if c_lowercase not in char_report:
            char_report[c_lowercase] = 0
        char_report[c_lowercase] += 1
    return char_report

def sort_on(items):
    return items["num"]

def get_report(file_path):
    char_report = get_num_char(file_path)
    char_report_list = []
    for c in char_report:
        char_report_per_char = {}
        char_report_per_char['char'] = c
        char_report_per_char['num'] = char_report[c]
        char_report_list.append(char_report_per_char)
    char_report_list.sort(reverse=True, key=sort_on)
    return char_report_list
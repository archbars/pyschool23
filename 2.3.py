import os
import chardet


def get_from_file_in_utf8(path):
    list_of_strings_in_file = []
    cur_file = open(str(path), 'rb')
    for line in cur_file:
        cur_char=chardet.detect(line).get("encoding")
        # print(cur_char)
        # print(line.decode('utf-8'))
        if cur_char.lower() == "utf-8":
            # print("ok")
            list_of_strings_in_file.append(line.decode('utf-8'))
        else:
            # print("bad")
            line_in_utf8=line.decode(cur_char)
            line_in_utf8=line_in_utf8.encode("utf-8")
            list_of_strings_in_file.append(line_in_utf8.decode("utf-8"))
    # print(list_of_strings_in_file)
    return list_of_strings_in_file


def get_count_of_words(list_of_words):
    dict_words={}
    # print(list_of_words)
    for line_in_list in list_of_words:
        # print(line_in_list)
        words=line_in_list.rstrip(" \n").split(" ")
        # print(words)
        for i in words:
            # print(i)
            i=i.lower()
            if len(i) >= 6:
                if dict_words.get(i,0) == 0:
                    dict_words[i] = int(1)
                else:
                    dict_words[i] = int(dict_words[i]+1)
    sorted_words = sorted(dict_words.items(), key=lambda item: -item[1])
    list_of_10 = []
    for i in range(10):
        # print(sorted_words[i])
        list_of_10.append(sorted_words[i])
    return list_of_10


def for_all_txt_files_in_script_folder():
    for d, dirs, files in os.walk(os.path.dirname(__file__)):
        for file in files:
            if str(file.find(".txt")) != '-1':
                content=get_from_file_in_utf8(path = os.path.join(d, file))
                list_of_most_frequent = get_count_of_words(content)
                print("Самые встречающиеся слова в файле {} - {}".format(file,list_of_most_frequent))


for_all_txt_files_in_script_folder()


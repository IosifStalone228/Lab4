def get_count_char(str_):
    dictionary_ = {}
    for char in str_.lower():
        if char.isalpha():
            if char not in dictionary_:
                dictionary_[char] = 1
            else:
                dictionary_[char] += 1
    return dictionary_

def get_perc(dict_):
    new_dict = dict_.copy()
    sum_ = sum(dict_.values())
    for item in dict_:
        new_dict[key] = (new_dict[key] / sum_) * 100
    return dict_




main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

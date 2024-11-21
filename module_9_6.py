# генераторы

# функция-генератор all_variants() принимает строку text и возвращает объект-генератор,
# при каждой итерации возвращает подпоследовательность переданной строки text.
def all_variants(text):
    subsequence_len = 1
    text_len = len(text)
    while subsequence_len <= text_len:
        start_index = 0
        end_index = subsequence_len
        while end_index <= text_len:
            yield text[start_index: end_index]
            start_index += 1
            end_index += 1
        subsequence_len += 1

a = all_variants("abc")
for i in a:
    print(i)
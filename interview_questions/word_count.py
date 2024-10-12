# given  a sentence space seperated your have to count frequency of unique words

input_str = "We have one banana. We want one more banana."

list_string = input_str.split(" ")
mapping_dict = {}

for word in list_string:
    if word in mapping_dict.keys():
        mapping_dict[word] += 1
    else:
        mapping_dict[word] = 1

print(f"Frequebcy mapping: {mapping_dict}")

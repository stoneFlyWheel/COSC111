import re
def find_years_mentioned(text):
    return re.findall(r'\b\d{4}\b', text)

passage = "The novel, published in 1851, is set mostly in 1849 but references events from 1620."
excerpt = "Written in 1959, Alas Babylon is a novel that explores the aftermath of a nuclear war."
print(find_years_mentioned(passage)) # ['1851', '1849', '1620'] 
print(find_years_mentioned(excerpt))


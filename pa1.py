words = []
full_list = ['you',3.13,'can','be','anything',False,'you','want','to','be','\n',
'just turn', 'yourself', 'into', 'anything','you','think','that',
'you','could', 'ever','be',True] 


for item in full_list:
    if isinstance(item, str):
        words.append(item)


final_string = " ".join(words)

print(final_string)

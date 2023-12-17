import re

# for name in pattern:
#     print(re.search(name, data))
with open('names.txt') as f:
    pattern_twitter = re.compile(r'\s[@][a-zA-Z]+')  #\s ensures emails wont pass
    pattern_name = re.compile('([A-Z][a-zA-Za-z]+), ([A-Z][A-Za-z-]+)')
    twitter_handles = []
    names = []
    
    for line in f:  #read line by line
        find_names = (re.match(pattern_name, line)) #only returns matches at beginning so nothing else passes through
        find_x = (re.search(pattern_twitter, line)) 
        if find_x: #if true or if characters match the case test...
            twitter_handles.append(find_x.group()) #.group appends on the matched characters # add string to a list
        if find_names:
            for user in twitter_handles: #iterate over list
                if user in line: # check if twitter name in line, to narrow search results  
                    if user == '@sverik':
                        # find_names = 'Sven-Osterberg, Erik'
                        # print(find_names)
                        # print(f'{find_names.split()[1]} {find_names.split()[0]} / {user.strip()}')
#                     print(f'{find_names.groups()[1]} {find_names.groups()[0]} / {user.strip()}')
                    
                    
                    
                    # 'Osterberg, Sven-Erik' is in  find_names:
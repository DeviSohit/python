sample = 'a'
sample_str = "abc"
sample_str = """abc"""
sample_str = "Today's weather is very nice"
sample_str = """Microsoft Windows [Version 10.0.22621.2861]
 (c) Microsoft Corporation. All rights reserved.
 Clink v1.6.0.3e6b73
 Copyright (c) 2012-2018 Martin Ridgers
 Portions Copyright (c) 2020-2023 Christopher Antos
 https://github.com/chrisant996/clink"""

sample_str = "Microsoft Windows [Version 10.0.22621.2861] \
 (c) Microsoft Corporation. All rights reserved.\
 Clink v1.6.0.3e6b73 \
 Copyright (c) 2012-2018 Martin Ridgers \
 Portions Copyright (c) 2020-2023 Christopher Antos \
 https://github.com/chrisant996/clink"

sample_str = """Microsoft Windows [Version 10.0.22621.2861]
 (c) Microsoft Corporation. All rights reserved.
 Clink v1.6.0.3e6b73
 Copyright (c) 2012-2018 Martin Ridgers
 Portions Copyright (c) 2020-2023 Christopher Antos
 https://github.com/chrisant996/clink"""

#print(len(sample_str))

#print(sample_str.upper())
#print(sample_str.capitalize())
#print(sample_str.count("Microsoft"))
#ans = sample_str.split(" ") # split based on space delimitizer
#ans = sample_str.split("\n") # split based on new line
# ans = sample_str.splitlines() # split based on new line
# print(ans)

# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"

# Indexing
# print(sample_str[0]) # 0th index --> M
# print(sample_str[3])
# print(sample_str[-1]) # in reverse 0th index --> ]
# print(sample_str[-4])

# Slicing
# print(sample_str[0:4]) # 0,1,2,3 indexes --> Micr
# print(sample_str[1:4]) # icr
# print(sample_str[:4]) # 0,1,2,3 --> Micr
# print(sample_str[20:]) # print from 20th char to end if u don't include end index
# print(sample_str[-1:-4]) # gives an empty output bcz it is from -4 to -1
# print(sample_str[-4:-1]) # 861
# print(sample_str[:]) # print total string chars
# print(sample_str[::2]) #Every second index will be removed/omitted --> McootWnos[eso 0026126]
# print(sample_str[1::2]) # starts from i index and every second char will be omitted --> McootWnos[eso 0026126]

# [start:end:step] 
# start: 0
# end: end
# step: -1
# print(sample_str[::-1]) # reverse a string

# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
# sample_str[0] = "p" # it is not allowed to change string char M to p. string is immutable
# print(sample_str)

## String concatenation
# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
# sample_str = sample_str + "Microsoft Corporation. All rights reserved."
# print(sample_str)

# sample_str = "abc"
# sample_str *= 10
# print(sample_str)
# print(len(sample_str))

sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
sample_str = "{0}{1}".format(sample_str, 'abc') # Microsoft Windows [Version 10.0.22621.2861]abc
sample_str = "{1}{0}".format(sample_str, 'abc') # abcMicrosoft Windows [Version 10.0.22621.2861]
sample_str = "{0}{0}".format(sample_str, 'abc') # Microsoft Windows [Version 10.0.22621.2861]Microsoft Windows [Version 10.0.22621.2861]
sample_str = "{1}{1}".format(sample_str, 'abc') # abcabc
sample_str = "{0}{1}{2}".format("abc", "def", "123") # abcdef123
print(sample_str)
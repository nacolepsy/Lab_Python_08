import re
def isEmail(inp): 
    return re.match(r'(^\w)+@\w+\.(\w){2,4}$', inp) != None
inp=(raw_input("Please Enter Your Email Address: "))
print isEmail(inp)


def getTxts(files):
    
    return re.findall(r'\w+\.txt\s', files)
  
print getTxts('yo.html blah.txt woah.txt he ')

def percAwesome(inp):
# find awesome or awes0me in the sentence
    rt= re.findall(r'(awesome|awes0me)', inp)
#Find all words 
    t=re.findall(r'\w+', inp)
#Count Number of words in Sentence
    main_length=len(t)
#Count Number of awesome or awes0me 
    first_length= len(rt)
# Convert Number of awesome to float
    s=float(first_length)
    #print s
    
#Calculate percentage of awesomeness in sentence
    percentage=s/main_length*100.0
    print " The percentage of awesomeness a string is", percentage
percAwesome('iamawesomeblah and awes0me is as awesomeo does') #returns 42.9(3/7*100)
percAwesome('hello my name is wayawesomedude') #returns 20.0 (1/5*100)


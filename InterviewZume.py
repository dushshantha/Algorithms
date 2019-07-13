"""

We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample output:

findContiguousHistory(user0, user1)
   /pink
   /register
   /orange

findContiguousHistory(user1, user2)
   (empty)

findContiguousHistory(user2, user0)
   a

findContiguousHistory(user5, user2)
   a

findContiguousHistory(user3, user4)
   /green
   /blue
   /purple
   /white

findContiguousHistory(user4, user3)
   /green
   /blue
   /purple

"""

user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
                   
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]

                                

user2 = ["a", "/one", "/two"]
user3 = ["/red", "/orange", "/yellow", "/green", "/blue", "/purple", "/white", "/yellow", "/HotRodPink", "/BritishRacingGreen"]
user4 = ["/red", "/orange", "/amber", "/green", "/blue", "/purple", "/white", "/lavender", "/HotRodPink", "/BritishRacingGreen"]
user5 = ["a"]

counts = [ "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" ]

def calculateClicksByDomain(counts):
    dict = {}
    for count in counts:      # n * k
        a = count.split(',')
        c = int(a[0])
        d = a[1].split('.')
        s = ''
        for i in range(len(d) - 1, -1, -1): # k
            if s == '':
                s = d[i]
            else:
                s = d[i] + '.' + s
            if s in dict:
                dict[s] += c
            else:
                dict[s] = c
    return dict
 

#r = calculateClicksByDomain(counts)

#for k in r.keys():
#    print( r[k], k)
    

def findContiguousHistory(u1, u2):
    dict = {}
    
    for i in range(len(u1)):
         dict[u1[i]] = i
    count = 0
    start = -1
    i = 0
    while i < len(u2):
        if u2[i] in dict:
            j = dict[u2[i]]
            
            c = 0
            while i < len(u2) and j < len(u1) and u1[j] == u2[i]:
                j += 1
                i += 1
                c += 1
            if count < c:
                count = c
                start = j - c

        else:
            i += 1
            
    return u1[start: start + count]
    
print('-------')
print(findContiguousHistory(user0, user1)) 
print('-------')
print(findContiguousHistory(user0, user2)) 
print('-------')
print(findContiguousHistory(user3, user4))
print('-------')
print(findContiguousHistory(user4, user3))
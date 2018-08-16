#9.4 Write a program to read through the mbox-short.txt 
#and figure out who has the sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
  line = line.rstrip()
  if not line.startswith('From '): continue
  email = line.split()[1]
  counts[email] = counts.get(email,0) + 1 #get email as dict key, give value 0 then plus 1 to start counting
                                          # if key doesn't exist, return 0 as default

maxmail = None
ct = 0
for email, value in counts.items(): #items() returns a list of dict of (key, value)
  if value is None or value > ct:
    maxemail = email
    ct = value
print(maxemail, ct)
  

hashfile = input("Enter filename for input hashes: ")
print (hashfile)


f = open(hashfile, "r")
#f = open('hashes.txt', "r")
hashes = f.readlines()
f.close()

print ("Hashes from readlines:")
for hash in hashes:
    print(hash)



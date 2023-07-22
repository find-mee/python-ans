passwd={"rahul": "genius","kumar": "smart","ankita": "intelligent"}

# i.	To print all the items in the dictionary.
print("All items")
print(passwd)
print()
# ii.	To print all the keys in the dictionary.
print("All keys")
print(passwd.keys())
print()
# iii.	To print all the values in the dictionary.
print("All values")
print(passwd.values())
print()
# iv.	To get the passwords of users. For example, passwd[‘rahul’]= genius
name = input("Enter name to get passw ")
if name in passwd:
    print(f"password of {name} is:")
    print(passwd[name])
else:
    print("Name doesnt exist")
print()
# v.	Change the password of a particular user. For example, passwd[‘ankita’]=‘brilliant’
name = input("Enter name to change their passw ")
if name in passwd:
    new_passw = input("Enter new passw ")
    print(f"old password: {passwd[name]}")
    passwd[name] = new_passw
    print(f"password changed to: {passwd[name]}")
else:
    print("Name doesnt exist")
print()

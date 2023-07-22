subjects = ["Maths","DCN","DAA","Python Programming Lab","FAFL","AEC"]

#1
for i in subjects:
    print(i)
print()

#2cl
print(subjects[1],"\n",subjects[4])
print()

#3
for i in range(4):
    print(subjects[i])
print()

#4
for i in range(-4,0):
    print(subjects[i])
print()

#5
for python in subjects:
    if python == "Python Programming Lab":
        print("Python Programming Lab is present")
        break
print()

#6
subjects.append("COI")
print("Appended COI\n",subjects)
print()

#7
subjects.insert(2,"MCIOT")
print("Inserted MCIOT at index 2 \n",subjects)
print()

#8
subjects.pop()
print("Poped\n",subjects)
print()

#9
subjects.remove("MCIOT")
print("Removed MCIOT \n",subjects)

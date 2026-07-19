# String
word1, word2 = "I Love", "Python"
sentence = word1+" "+word2
print(sentence,"<->", len(sentence))
print(sentence[2])
for ch in word2:
    print(ch, end=" ")
print()

# String Slicing
print(sentence[2:5]," -- ", sentence[2:8:2])

# String Formatting
a, b = 5, 10
sum = a+b
print("Sum of {1} & {0} is: {2}".format(a, b, sum)) # format
print("Values of vars {a} & {b}".format(a=5, b=10))
print(f"Average of {a} & {b} is {(a+b)/2}") # f-strings -> Literal string interpolation

# Lists
marks = [99, 89, 100, 65, 92]
marks.sort()
print(len(marks)," -- ", marks," -- ", marks[1:3])
marks[2] = 98
print(marks)
data = [4, 55, "Hello!", 67, "Yo!", 100]
data.append("Kyu Re")
data.reverse()
print(data)
for l in data:
    print(l," ", end=" ")
    if(l == 67):
        break
print()

# Tuples
tup = (1, 2, 3, 4, 5)
print(type(tup)," | ", len(tup)," | ", tup)
sum = 0
for t in tup:
    sum += t
    if(t == 3):
        continue
    print(t, end=" ")
print(f"\nSum of tuples is: {sum}")

# Dictionary
info = {
    "name": "Adeeb",
    "cgpa": 9.2,
    "subjects": ["Maths", "Science", "Social Studies"],
    3.14: "PI"
}
print(type(info)," | ", info)
print(info[3.14])
print(info.keys()," | ", info.values(), " | ", info.get(3.12), info.get(3.14))

# Sets
st = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5}
empty_set = set()
print(type(st)," | ", len(st)," | " ,st)
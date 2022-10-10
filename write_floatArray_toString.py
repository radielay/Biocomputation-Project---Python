
floats = [1.1, 2.2, 3.3, 4.4]
str_floats = [str(fl) for fl in floats]

str = ",".join(str_floats)

file = open("graph", "a")
file.write(str + '\n')
file.close()

print(str)
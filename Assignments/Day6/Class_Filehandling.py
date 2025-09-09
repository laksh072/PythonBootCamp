def read_first_n_lines(filename,n):   # read the specific first N lines of a file
    with open(filename,'r') as f:
        for i in range(n):
            line = f.readline()
            print(type(line))
            if not line:
                break
            print(line.strip())
           
read_first_n_lines('D:/PyGit/PythonBootCamp/Assignments/Day6/sample.txt',15)

data = {
    "name":"Ravi",
    "age": 45,
    "location":"Delhi"
}
 
with open('D:/PyGit/PythonBootCamp/Assignments/Day6/user.txt','w') as f:
    for key, value in data.items():
        f.write(f"{key}:{value}\n")

for person in arr_of_dicts:
    for key, value in data.items():
       f.write(f"{key}:{value}\n")
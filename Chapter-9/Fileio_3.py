#Exercise to print the table for n numbers

def Tables(num):
    str = ""
    for i in range(1,11):
        str += f"{num} X {i} = {num * i}\n"

    with open(f"Table/table_no_{num}.txt","w") as F:
        F.write(str)

for i in range(2,7):
    Tables(i)
# # # file = open("geek.txt", )
# # # print(file.name)
# # # print(file.mode)
# # # print("Is file closed?", file.closed)
# # # file.close()
# # # print("Is file closed?", file.closed)
# # # f= open("geek.txt",)
# # # content=f.read()
# # # print(content)
# # # f.close()
# # # print("Is file closed?", f.closed)
# # with open("geek.txt","w") as f:
# #  f.write("hello python is easy for handling files")
# #  f.write("\n")
# #  f.write("I love python")
# # f.close()
# # f= open("geek.txt",)
# # content=f.read()  
# # print(content)
# # print("Is file closed?", f.closed)
# # f.close()
# # print("Is file closed?", f.closed)
# with open("geek.txt",) as f:
#     content=f.read()  
#     print(content)
#     print("Is file closed?", f.closed)

try :
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file was not found.")
finally:
    if 'file' in locals():
        file.close()    
# This code attempts to open and read a file named "example.txt".

# def do(line: str, lines: list[str], list_counter: int):
#     if line.upper() == line and not line.isdigit():
#         print(f'deleted {lines[list_counter + 1]}')
#         del(lines[list_counter + 1])

#         print(f'deleted {lines[list_counter]}')
#         del(lines[list_counter])
#         # print(line)

# def par(x: str, List: list[str], Counter: int, loop: int):
#     if x == '(':
#         loop += 1
#         Counter += 1
#         while True:
#             if List[Counter] == ')':
#                 loop = loop - 1
#                 break
#             else:
#                 par(List[Counter], List, Counter, loop)
#             Counter += 1
                
#     elif loop != 0:
#         print(x * loop)
    
        

# def loo(x: str, List: list[str], Counter: int):
#     while True:
#         Counter += 1
#         if List[Counter] == ')':
#             break
#         elif List[Counter] == '(':
#             loo(x, List, Counter)
        

# def m(x):
#     x_type = 'bool'
#     return x_type, True if x == 'True' else False

# c = 0
# def z(a, c, cap):
#     print(a)
#     current = c
#     c += 1
#     if c < cap:
#         z(a, c,cap)
#     print(current)




# if __name__ == '__main__':
#     x = ['a', 'b', 'c', '(', '1', '2', '3', '(', 'A', 'B', 'C', ')', '4', '5', ')']
#     c = 0
#     z(5, c, 3)




#     # lc = 0
#     # loop = 0
#     # while lc < len(x):
#     #     par(x[lc], x, lc, loop)
#     #     lc += 1


#     # a = ['(', ' ', ' ', ' ', ' ', '(', ' ', ')', ' ', ' ', ')']
#     # c = 0
#     # print(len(a))
#     # while c < len(a):
#     #     print(c)
#     #     i = a[c]
#     #     if i == '(':
#     #         loo(i, a, c)

#     #     c += 1
#     # print('done')
    

#     # print(m('False'))

x = 'file.txt'
print(x[-3:])
# # def loo(x: str, List: list[str], Counter: int, loop: int):
# #     if x == '(':
# #         loop += 1
# #         Counter += 1
# #         while True:
# #             if List[Counter] == ')':
# #                 loop = loop - 1
# #                 break
# #             else:
# #                 loo(List[Counter], List, Counter, loop)
# #             Counter += 1
                
# #     elif loop != 0:
# #         print(x * loop)
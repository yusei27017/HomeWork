
'''
input 5
print
*
**
***
****
*****
****
***
**
*
------------
*
**
*  *
*    *
*      *
*        *
*      *
*    *
*  *
**
*
'''
def print_delta(height):
    delta_array = ['*'*i for i in range(1, height+1)]
    for e in delta_array:
        print(e)
    delta_array.pop()
    for r_e in delta_array[::-1]:
        print(r_e)
    return


if __name__ == "__main__":
    print_delta(5)
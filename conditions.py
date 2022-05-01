from cgi import print_directory
import numbers



name=input('please inset your name:')
age=int(input(f'hello {name} could you please insert your age'))
age_res =18

if age>age_res:
    print('your ID will printed')
elif age<age_res:
    print(f'please come back in a{age_res-age} years')
import os

def key_search():
    temp='dir /B /o:D >all_files.txt'
    os.system(temp)
    
    print('\n')
    key = input('Enter key : ')
    fptr = open('all_files.txt','r')
    print('\n')

    flag =0
    
    for i in fptr:
        i=i.replace('\n','')
        temp=i
        i=i.replace(' ','_')
        i=i.split('.')
        j=i[0]
        j=j.split('_')
        for k in j:
            if k==key:
                flag=1
                print(temp)
        #print(j)
    if flag==0:
        print('\n NO RESULT FOUND\n')

    input('\npress any key to continue ... ')

def all_files():
    os.system('cls')
    print('\nfiles and subdirectories in the current directory : ')
    print('---------------------------------------------------\n')
    os.system('dir /o:D')
    save = input('\n Save (y/n) : ')

    if save =='y' or save=='Y':
        fname = input(' file name : ')
        temp = 'dir /o:D>'+fname+'.txt'
        os.system(temp)
        print('\n File saved ')
        input('press any key to continue ... ')

def hidden():
    os.system('cls')
    os.system('dir /A:H')
    input('\n\npress any key to continue ... ')

def search_file():
    print('\n current directory :\n')
    os.system('cd')
    
    fname = input('\nfile name : ')
    fname=fname.replace(' ','')
    fname=fname.split('.')
    
    temp='dir /B /o:D >all_files.txt'
    os.system(temp)

    fptr = open('all_files.txt','r')
    flag = False

    for i in fptr:
        i=i.replace('\n','')
        i=i.replace(' ','')
        temp=i
        i=i.split('.')
        if i[0] == fname[0]:
            print('\n',temp)
            flag = True
    if flag == False:
        print('File not found')
    input('\n\npress any key to continue ... ')

def menu():
    index=0
    os.system('cls')
    print('')
    print('[0] files and subdirectories ')
    print('[1] display hidden files ')
    print('[2] search for file')
    print('[3] search with keys ')
    print('[4] Available files ')
    print('[5] exit')
    print('\n')
    try:
        index = int(input('index : '))
    except (ValueError, UnboundLocalError):
        print('error')
        input('\n\npress any key to continue ... ')
        index=5
        

    if index == 0:
        all_files()
    elif index == 1:
        hidden()
    elif index == 2:
        search_file()
    elif index == 3:
        key_search(
    elif index ==5:
        exit()
    else:
        print('error')
        input('\n\npress any key to continue ... ')
        index=5
    

while True:
    menu()

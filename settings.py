from os.path import exists

num = int()
def file(data,mode):
    if mode == 0:
        f = open('isettings.txt', 'a')
        f.write(data)
        f.close()

    elif mode == 2:
        f1 = open('isettings.txt', 'r')
        return f1

    elif mode == 1:
        f2 =open('isettings.txt', 'w')
        f2.write(data)
        f2.close()

def intial_file():
    if  not exists('isettings.txt'):
        #defualt number
        num = 30
        reset = "no"
        focus = "off"
        data = f"num_of_review_words_per_day: {str(num)}" + f"\nreset_database: {reset}" + f"\nfocus_mode: {focus}"
        file(data,0)

def start(update):
        intial_file()
        set_data = list()
        f_data = file('',2)
        temp = str()
        temp = f_data.readline()
        set_data.append(temp[29:])
        temp = f_data.readline()
        set_data.append(temp[16:])
        temp = f_data.readline()
        set_data.append(temp[12:])

        if update == True:
            data = f"num_of_review_words_per_day: {str(set_data[0])}" + "reset_database: no" + f"\nfocus_mode: {str(set_data[2])}"
            file(data,1)

    #print(temp.find(" "))

        return set_data

#start(False)
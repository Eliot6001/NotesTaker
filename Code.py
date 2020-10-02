Choice = input("Hello\nHow can i help you today?\n1/New Data? 2/See already made ones")
def file_creator(file,mode):
        return open(file,mode)

def New():
    New_Note = input("What do you want to save:\n")

    def file_writer(file, input):
        return file.write(f"{input}\n")

    Opened_file = file_creator('Notes.txt','a')
    file_writer(Opened_file, New_Note)

    Opened_file.close()
def See_MadeOnes():
    Opened_f_readmode = file_creator('Notes.txt', 'r')
    print(Opened_f_readmode.read())
    Opened_f_readmode.close()

if Choice == '1':
    New()
elif Choice == '2':
    See_MadeOnes()
else:
    quit

import os, shutil

__author__ = 'Lindsay Ward'
string = "The Will and the Word.txt"


def fixed_file_name(name):
    new_name = list(name)
    new_name
    print(new_name)
    i = 0
    for character in name:
        if character.isupper() and i != 0:
            try:
                if new_name[i-1].islower():
                    print(new_name[i])
            except IndexError:
                continue
        i += 1
    return new_name


print(fixed_file_name(string))
# loop through each file in the (original) directory

def main():
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    for filename in os.listdir('.'):

        # ignore directories, just process files
        if not os.path.isdir(filename):

            #new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
            new_name = fixed_file_name(filename)
            print(new_name)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)


    # Processing subdirectories using os.walk()
    # os.chdir('..')
    # for dir_name, subdir_list, file_list in os.walk('.'):
    #     print("In", dir_name)
    #     print("\tcontains subdirectories:", subdir_list)
    #     print("\tand files:", file_list)


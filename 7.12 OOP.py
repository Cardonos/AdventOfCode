import pandas as pd


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

    def get_size(self):
        return self.size


class Folder:

    def __init__(self, name, supfolder):
        self.name = name
        self.supfolder = supfolder
        self.content = []

    def add_file(self, file):
        self.content.append(file)

    def add_folder(self, folder):
        self.content.append(folder)

    def folders(self, allsub):
        folders = []
        for i in self.content:
            if type(i) == Folder:
                folders.append(i)
                if allsub == True:
                    folders.extend(i.folders(True))
        return folders

    def down(self, foldername):
        for j in self.content:
            if j.name == foldername:
                return j

    def get_size(self):
        size = 0
        for k in self.content:
            size += k.get_size()
        return size


data = pd.read_csv('Inputs/Day 7.txt', names=['a', 'b', 'c'], header=None, sep=' ')
# turn commands into folder structure
root = Folder('/', None)
i = 0
loc = root
while i < len(data):
    if data.at[i, 'a'] == '$':  # start of command
        if data.at[i, 'b'] == 'cd':  # changing location to new directory
            if data.at[i, 'c'] == '..':  # changing up to superfolder
                loc = loc.supfolder
            elif data.at[i, 'c'] == '/':  # changing to root
                loc = root
            else:
                loc = loc.down(data.at[i, 'c'])  # changing down a folder
    elif data.at[i, 'a'] == 'dir':  # directory listed
        loc.add_folder(Folder(data.at[i, 'b'], loc))
    else:  # file listed
        loc.add_file(File(int(data.at[i, 'a']), data.at[i, 'b'], ))
    i += 1

filesystem = [root]
filesystem.extend(root.folders(True))  # build folder structure
sum = 0
for j in filesystem:  # get all folders under size 100000
    if j.get_size() < 100000:
        sum += j.get_size()
print(sum)  # Part 1 Answer

# Part 2
space = 70000000
needed_space = 30000000
free_space = space - root.get_size()  # calculate the current free space
needed_size = needed_space - free_space  # calculate the needed size to be deleted

bigger_folders = []
for j in filesystem:
    if j.get_size() > needed_size:  # get all folders bigger than the needed size
        bigger_folders.append([j.get_size()])  # generate a list of all folders bigger than the needed size
bigger_folders.sort()  # sort the list
print(bigger_folders[0])  # output the smallest folder

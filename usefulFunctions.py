'''
Hi there!
The first line of your code should be "from usefulFunctions import *"
To use a function, type <functionName>(<argumentsNames>).
You can add or tweak any function you want in this file.
If you don't want the message printed whenever you run your program, remove the last two lines of this program (else: print("blahblahblah"))
The bottom of the document also contains several templates for code (only one rn lol)
I've also included annotations for each line of the code

Here's a list of functions I added (<argugment> means it is optional) (I added some more later but I cba to update the descriptions, you're not gonna use those anyway):

answer = inputInt(message)
Will ask the user something. If the user does not enter an integer, it will keep asking them until they do. In order to ask the user "Enter a number: ", type u.inputInt("Enter a number: ")

list = make1DList(string)
Takes a string of a list (e.g.:"[1,2,3]") and turns it back into a list. This does not work if the list has strings with commas or is 2D. I'll work on that later (maybe).

pt(list1, list2, pos)
Removes whatever is at position pos in list1 and puts it in list2. To explain better let's say list1 = [1,2,3] and list[4,5,6]. pt(list1, list2, 0) would remove whatever is at position 0 in list1 (1 is at position 0) and put it in list2. After the function, list1 = [2,3] and list2 = [4,5,6,1]

var = switch(var)
Changes var from true to false if it is true, and from false to true if it is true, like an on-off switch.

printNice(list, headersList)
The best function here. Prints formatted 2d lists in a neat table. You need to input the list you want formatted and the table headers. For example, say I want to print the temperature in places, my headersList would be ["Place", "Temperature"]

createFile(fileName)
Creates a file.

deleteFile(fileName, <error>)
Deletes a file. Set error to true if you want an error to be returned. By default, error is set to false.

writeto(fileName, message, <overwrite>, <error>)
Writes message to the file. It will overwrite whatever is in the file, unless overwrite is set to false. By default, overwrite is set to true. Error will be printed if error = True, by defualt it is false. The error argument can only be set if the override argument is as well.

list = listFile(fileName, <split>, <error>)
Returns a list that is made from the file. Split is how the items in the list are separated. By default, split is set to ",". An error will be displayed if error == True, by default it is false. The error argument can only be set if split is set too.

killComputer(a)
Do it, I dare you.

connections, totalPlayers = createServer(port)
Creates a server after asking the user for a host IP. It returns client information in a 2d list (connection, address). connections[x][x][0] is the client IP address and connections[x][x][1] is the port. This is not completely robust, and incorrect input will possibly lead to errors.

s = joinServer()
Asks the user for the host IP and connects to that IP if possible. Otherwise, it will ask the user for the IP again.

bool = isFileOpen("filename")
Checks if a file is open via external process (ie not in python). It's very faulty since I copied it off the interent and I don't understand anything

stopMusic(<fade>)
Stops music from playing if there is any playing the music will fade out over the course of [fade] seconds, by default, fade is set to 0.

playMusic(music, volume, <fade>, <duration>)
Plays [music] (specify the directory) at loudness [volume] (0 = none, 1 = loudest), the music currently playing fades out over the course of [fade] seconds. By default, fade is set to 0. The music plays for [duration], which can only be entered after fade. By default, this is set to -1 (repeat)

drawStuff(screen, thing, position, size, coll)
Draws something in pygame, with hitboxes. This goes inside the while loop of the main program, but the file has to be loaded outside of the while loop. The size of the object must be inputted to help with the collision. Coll is what is going to collide with the object (must be an object class with an x, y, width and height value).

roundDown(num)
Jk. Try int(x)

mean(n), mode(n), range(n), median(n)
Return the mean, mode, range and medians of list n

list = intShimasu(list)
Turns all possible values into integers in a list

clearAll()
Clears the shell. MAC SUPPORT

MS1(), MS2(), MS3(), MS4()
sorts by those positions in a list

crop(image, rect, bg=1,1,1)
Crops an [image] using [rect] (x, y, width, height), the background is made transparent, all pixels of the shade RGB(1,1,1) are removed

pyCheck(fps, clock)
Gets framerate, keypresses and runs the mandatory if "event == pygame.QUIT:" loop

loadAll(folder, exception=[])
Loads all images in a folder, apart from those in the list [exception]

loadImages(images, folder="")
Loads multiple images ([images] is a list), can change the directory where the images are loaded from using [folder]

blitStuff(screen, things)
Blits multiple things onto a [screen]. Every value in [things] is made up of the image, the image's x position, and its y position
'''
# Setup, before the actual code -----------------------------------------------------------------------
import os, math, socket, ctypes, copy                                # Imports the necessary modules

try:                                                                 # Tries to import pygame, but if you don't have pygame installed it can't
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'                   # Hides the pygame message when loading the program
    import pygame
except:
    print("Pygame is not installed, pygame-related functions will crash your program")

# The actual code -------------------------------------------------------------------------------------
def inputInt(message):
    while True:                                                  # Repeats infinitely
        try:
            number = int(input(message))                         # Asks the user for a number and converts it into an integer
            return number                                        # Returns the user's input as an integer
            break
        except ValueError:                                       # If the user did not input an integer
            print("Please enter an integer!\n")                  # Ask the user for an integer again

def askyesno(message):
    while True:                                                  # Repeats infinitely
        answer = input(message)
        if answer in ["yes", "no", "y", "n"]:                    # If answer is yes, y, no or n
            return answer                                        # Then the answer is returned
            break
        else:
            print("Enter yes or no!\n")                          # If not, ask the user for input again

#Makes a string of a list into a list, COMMAS IN THE STRING WILL BREAK THIS FUNCTION
def make1DList(string):
    string = string[1:-1] + ","                                  # Removes the first and last character (they're square brackets) and adds a comma
    quotMarks = False
    list = []
    commaList = [-2]
    for i in range(len(string)):                                 # Repeats for every character in the string
        if string[i] == ",":                                     # If the character is a comma
            commaList.append(i)                                  # The position of it is added to a list. This list contains the position of every comma in the string

    for i in range(len(commaList)-1):                            # Repeats for how many commas there are
        pos1 = commaList[i]+2                                    # The first position of the value (after one comma)
        pos2 = commaList[i+1]                                    # The last position of the value (before the next comma)
        stringPart = str(string[pos1:pos2])                      # Gets the value inbetween those two commas
        try:
            stringPart = int(stringPart)                         # Tries to make the value an integer
        except:
            if stringPart[0] == "'" and stringPart[-1] == "'":   # If the first and last positions of the value are quotation marks/apostrophes, the program counts the value as a string
                stringPart = str(stringPart[1:-1])               # The quotation marks are removed
            elif str(stringPart) in ["True", "False"]:           # Otherwise, if the value is equal to True or False, it beomes boolean
                stringPart = bool(stringPart)

        list.append(stringPart)                                  # The value is added to the list

    return list

#Moves an item from one list to another
def pt(list1, list2, pos):
    list1.append(list2.pop(pos))                                 # Pretty self explanatory. The value at position POS is removed from list2 and added to list1
    return list1, list2

#Switches a true to a false and vice versa
def switch(var):
    if var == True:                                              # Also self explanatory
        var = False
    elif var == False:
        var = True
    return var

#Prints a formatted 2d list
def printNice(l, headersList):                                   # Holy crap, ready yourself for THIS. I wrote this and even I don't know what's going on lmao
    something = copy.deepcopy(l)
    listNew, values = [], []

    for i in range(len(l[0])):                                   # Repeats for the first list (1d list) in the array (2d list)
        listNew.append([])                                       # No idea what this does but it works so I don't wanna touch it. Probably creates a placeholder so values can be added later
        values.append(len(headersList[i]))                       # Adds the values from headersList into a list called values

    for i in range(len(l)):                                      # Repeats for the amount of lists in the array
        for j in range(len(l[i])):                               # Repeats for the amount of values in the lists in the array
            l[i][j] = str(l[i][j])                               # Makes every value a string
            listNew[j].append(l[i][j])                           # Voodoo magic. All I remember is that these five for loops switch the values of the array (ie the columns become rows and the rows become columns)

    for i in range(len(listNew)):                                # More voodoo magic
        for j in range(len(listNew[i])):
            if values[i] < len(listNew[i][j]):
                values[i] = len(listNew[i][j])

    print("| ", end = "")                                        # Prints | and doesn't go to the next line
    for i in range(len(headersList)):                            # Repeats for how many headers there are
        spaces = " "*(values[i]-len(headersList[i]))             # Gets the longest value, and that many spaces are added to the other values. Jonas has 2 more characters than Bob so 2 spaces are put after Bob BUT NOT YET
        finish = "" if len(headersList)-1 != i else "\n"         # If this is the last value in the row, it moves to the next line to print the next row. Otherwise, it keeps going on the same row
        print(headersList[i] + spaces + " | ", end = finish)     # This is where the value is printed. Ie: Bob + 2 spaces + |

    print("| ", end = "")                                        # Prints | and doesn't go to the next line
    for i in range(len(values)):                                 # Repeats for the amount of values in values
        print("-"*(values[i]) + " | ", end = "")                 # Prints the length of values (the longest value in the column) as hyphens (ie: instead of Bob it would be ---) plus |
    print()                                                      # New line

    for i in range(len(l)):                                      # Repeats for the lists in array L
        print("| ", end = "")                                    # Prints |
        for j in range(len(l[i])):                               # Repeats for every value in every list in L
            spaces = " "*(values[j]-len(l[i][j]))                # Gets the amount of spaces needed after the value. Same rule as above
            finish = "" if len(l[i])-1 != j else "\n"            # The program moves to the next line if that was the last value in the row
            print(l[i][j] + spaces + " | ", end = finish)        # Value and spaces are printed

    for i, thingy in enumerate(something, 0):
        for j, thing in enumerate(thingy, 0):
            l[i][j] = thing

#Creates a file
def createFile(fileName):
    file = open(fileName, "w")                                   # Opens an empty file. If it exists, it won't be created
    file.close()

#Deletes a file
def deleteFile(fileName, error="True"):
    try:
        os.remove(fileName)                                      # Deletes the file using the os module, if it exists
    except Exception as e:
        if error != True:
            pass
        else:
            print("There was an error with deleting the file {0}: {1}".format(fileName, e)) #Lolol I didn't even use f-strings back then

#Writes to a file
def writeTo(fileName, message, overwrite=True, error=False):
    if overwrite != True:                                        # If you do not want to overwrite the file
        try:
            with open(fileName) as file:                         # Opens file. This way, the file doesn't need to be closed (closes automatically)
                fr = file.read()                                 # File is read
            message = fr + message                               # Message is added to the file contents
        except Exception as e:
            if error:                                            # If the file couldn't be opened, error is printed (only if the user wanted the error to be printed)
                print("There was an error with writing to the file {0}: {1}".format(fileName, e))

    file = open(fileName, "w")                                   # Opens the file and writes the message to it
    file.write(message)
    file.close()

#Reads a file and creates a 2d list from it
def listFile(fileName, split=",", error=False):
    try:
        file = open(fileName ,"r")                               # Opens file
        list = []
        fl = file.readline()                                     # Reads line 1
        while fl != "":                                          # Keeps reading lines until the file is finished
            fl = fl.replace("\n","")                             # Gets rid of newline
            field = fl.split(split)                              # Splits the line by what the user wants it to be split by

            try:
                field.remove("")                                 # If the list is empty, it is removed from the list
            except Exception as e:
                pass

            list.append(field)                                   # Line is added to the list
            fl = file.readline()                                 # Next line is read

        file.close()
        return list
    except Exception as e:
        if error:                                                # Error message
            print("There was an error with reading the file {0}: {1}".format(fileName, e))
        else:
            pass

#Kills your computer
def killComputer():                                              # Haha files go brrr
    num = 0
    while True:
        num += 1
        write = str(num)
        for i in range(25):
            name = write*(i+1)
            file = open("{0}.txt".format(name), "w")
            file.close()

#Creates a server
def createServer(port):                                          # Gives me PTSD so I'm going to skip it
    host = input("Enter the IP: ")
    s = socket.socket()
    print("Waiting for clients to connect...")

    try:
        s.bind((host, port))
        s.listen(1)
    except Exception as e:
        print("Socket error:", e)

    connections = []
    for i in range(totalPlayers):
        conn, addr = s.accept()
        print("Connected to", addr[0], "on port", addr[1])
        connections.append([conn, addr])

    return connections, totalPlayers

#Joins a server
def joinServer():                                                # PTSD again
    while True:
        try:
            s = socket.socket()
            host = input("Enter the IP: ")
            print("Connecting...", end = " ")
            port = 5555
            s.connect((host, port))
            print("Connected.\nWaiting for everyone to connect...\n")
            s.send(str.encode("message"))
            return s
        except:
            print("Incorrect IP!")

def isFileOpen(fileName):                                        # Copied from stackoverflow
    EnumWindows = ctypes.windll.user32.EnumWindows               # All good programmers take inspiration :)
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)

    for openFile in titles:
        if f"{fileName}" in openFile:
            return True
            break
    return False

def stopMusic(fade=0):
    if pygame.mixer.music.get_busy():                            # Stops any music playing in pygame if there is any playing
        pygame.mixer.music.fadeout(fade)

def playMusic(music, volume, fade=0, duration=(-1)):             # Stops current music playing, starts new music
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(fade)

    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(duration)

def drawStuff(screen, thing, pos, size, player, horiCollision):  # Thank god I'm better at pygame now, this looks horrendous
    screen.blit(thing, pos)

    left = pos[0] - player.width                                 # NOT EVEN PYGAME.RECT()
    right = pos[0] + size[0]
    xMid = pos[0] + size[0]/2
    top = pos[1] - player.height
    bottom = pos[1] + size[1]
    yMid = pos[1] + size[1]/2

    sideCollision = True if top < player.y < bottom and not horiCollision else False
    horiCollision = True if left < player.x < right and not sideCollision else False

    if sideCollision and xMid < player.x < right:
        player.x = right
    elif sideCollision and left < player.x < xMid - player.width:
        player.x = left
    elif horiCollision and top < player.y < yMid:
        player.y = top
    elif horiCollision and yMid < player.y < bottom:
        player.y = bottom

    return horiCollision

def mean(n):
    total = 0
    for number in n:                                             # Repeats for every number in a list
        total += number                                          # Adds number to total
    total /= len(n)                                              # Divides total by amount of numbers

    return total

def mode(n):
    modes = [[0, 0]]
    for number in n:
        for mode in modes:
            if n.count(number) > mode[1]:                        # Counts how many times a number appears. If it appears the most:
                modes = [[number, n.count(number)]]              # The number and count of it is added here
            elif n.count(number) == mode[1]:
                modes.append([number, n.count(number)])
                break

    for mode in modes:
        while modes.count(mode) > 1:
            modes.pop(modes.index(mode))

    modes2 = []
    for mode in modes:
        modes2.append(mode[0])

    return sorted(modes2)

def findRange(n):
    n = sorted(n)
    range = abs(n[0] - n[-1])

    return range

def median(n):
    n = sorted(n)
    medianPos = (len(n) + 1)/2
    if int(medianPos) != medianPos:
        median = (n[int(medianPos)-1] + n[int(medianPos)])/2
    else:
        median = n[int(medianPos)-1]

    return median

def intShimasu(List):
    for i in range(len(List)):
        for j in range(len(List[i])):
            try:
                List[i][j] = int(List[i][j])
            except:
                pass
    return List

def clearAll():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def MS1(index):
    return index[0]

def MS2(index):
    return index[1]

def MS3(index):
    return index[2]

def MS4(index):
    return index[3]

def crop(image, rect, bg=(1, 1, 1)):
    surface = pygame.Surface((rect[2], rect[3]))
    surface.fill(bg)
    surface.set_colorkey(bg)
    surface.blit(image, (0, 0), rect)

    return surface.convert()

def pyCheck(fps, clock):
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
    if fps > -1:
        clock.tick(fps)

    return pygame.key.get_pressed()

def loadAll(folder, exceptions=[]):
    l = []
    for image in os.listdir(f"{folder}"):
        if os.path.isfile(f"{folder}/{image}") and image not in exceptions:
            l.append(pygame.image.load(f"{folder}/{image}").convert())
    return l

def loadImages(images, folder=""):
    loaded = []
    for image in images:
        if folder == "":
            loaded.append(pygame.image.load(f"image"))
        else:
            loaded.append(pygame.image.load(f"{folder}/{image}"))
    return loaded

def blitStuff(screen, things):
    for thing in things:
        screen.blit(thing[0], (thing[1], thing[2]))
'''
Plays music over a game background:
u.playMusic(music, volume, fade)

bg_image = pygame.image.load("bgimage.png")
notOver = True

while notOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notOver = False

    screen.blit(bg_image, (0,0))
    pygame.display.update() #Updates the sceen so changes are visible
'''

if __name__ != "__main__":
    print("This program is using usefulFunctions. Check usefulFunctions.py for the list of functions it creates\n")

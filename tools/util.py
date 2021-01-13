import random, string, os, sys



class Tool:
   
   def generatePassword():
        return "".join(random.choices(string.ascii_letters + string.digits, k=15))

   
   def multiple(folder):
      global empty
      try:
         value =input("How many copies of this file do you need: ")
         value = int(value)
         empty = []
         repeat = folder * value
      except ValueError:
         print("You have entered an invalid response please try again\n")
         value =input("How many copies of this file do you need: ")
         value = int(value)
         empty = []
         repeat = folder * value
      except ValueError as err:
         print(err)
         sys.exit()


      dup = 0

      for items in range (len(repeat)):
         dup += 1
         # print(dup)
         new_dup =str(dup)
         new_file =  new_dup+"__"+repeat[items] 
         empty.append(new_file)
      return(empty)
        




class Colours():

   WARNING = '\033[93m'
   SUCCESS = '\033[32m'
   END = '\033[0m'
   DANGER = '\033[31m'
   BOLD = '\033[1m'
   BLINK    = '\33[5m'


'''
==========================================================================
The below colours are here for reference sake and not used in this program
==========================================================================
========== See: https://en.wikipedia.org/wiki/ANSI_escape_code ===========
'''

'''



CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'



'''


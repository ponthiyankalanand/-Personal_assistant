import os
def garbage(filename):
   if os.path.exists(filename):
      os.remove(filename)
   else:
      print("The file does not exist") 


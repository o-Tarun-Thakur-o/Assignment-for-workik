import os
from zipfile import ZipFile, ZIP_DEFLATED 
import datetime
import pathlib
import shutil

api_Key = "AIzaSyB5V_qvKluc6-sRMbmqK7ow-MXZWEoTEHE"

sendAI_Specification = """
Note: only write the python code nothing else include other information in '#' and 
At the end of the code use an input command which exits the programme
specify any important packages that will be required using '#' and tell how to install them
"""

line = """

-------------------------------------------------------------------------------------------------------------

"""

disclaimer = """"
Note: The code that the ai generates will be very simple as it is open source and has limitations

                                    ***'Thanks for using'***
"""

ReadMe_Asset = """Before runnning The programme please check the code as Ai is not perfect and
Install all the packages that are told in the project itself, including how to install them

The programme has used Gemini Api gemini-1.5-flash Ai model
Get all the Documentation on how to use Gemini Api here --> https://ai.google.dev
"""

def formating_File(path):
  with open(path, 'r') as file:
    lines = file.readlines()
  with open(path, 'w') as file:
    for line in lines[1:-1]:
      file.write(line)

def create_File(filename,response,username):

  with open(f"Application/{username}/{filename}.py", 'w') as file:
    file.write(response.text)
    result = True

  formating_File(f"Application/{username}/{filename}.py")

  with open(f"Application/{username}/README.txt", 'w') as file:
    file.write(ReadMe_Asset)
    result = True

  folder = pathlib.Path(f"./Application/{username}/")
  zip_Path = f"Application/{username}_Zip.zip"
  with ZipFile(zip_Path, 'w', ZIP_DEFLATED) as zip:
    for file in folder.iterdir():
      zip.write(file)
      
  return result

def makeDir():
  Current_time = datetime.datetime.now()
  Time = Current_time.strftime("%H_%M_%S")
  UserName = input("Please enter username : ")
  os.makedirs("Application", exist_ok= False)
  os.makedirs(f"Application/{UserName}_{Time}")
  username = f"{UserName}_{Time}"
  return username
def deleteDir(username):
  delete_Folder = f"Application/{username}"
  shutil.rmtree(delete_Folder)



  

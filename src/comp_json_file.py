
from deepdiff import DeepDiff
import json, os


json_data_file1 = "file3.json"
json_data_file2 = "file1.json"

def json_fileexist_convto_dict(file_name):
    """
    If Data File Exists with Data load the data to Python Dictionary.
    Keyword arguments:
    -----------------
    f_name : string format.
        File Name stored in this module as Variable.
    Returns:
    --------
    Data File
        Json Data File been Parsed and returned as Python Dictionary File
    """

    if os.path.exists(file_name):
        with open(file_name, 'rt') as read_data_file:
            file_sz=os.path.getsize(file_name)
            if file_sz != 0:
               pars_data_file=json.load(read_data_file)
            else:
               pars_data_file='0'
    else:
        pars_data_file=''
    return pars_data_file

r1=json_fileexist_convto_dict(json_data_file1)
r2=json_fileexist_convto_dict(json_data_file2)

#If both files are valid call Deepdiff built-in function
if r1!='' and  r2!='' and r1!='0' and r2!='0':
    diff = DeepDiff(r1, r2, ignore_order=True) # compare the dictionaries

    #assert not diff, f"difference in response: {diff}"
    #print (diff)
    #diff Not Empty if any difference is found

    if len(diff) == 0:
      print("Json files are Similar")
    else:
      print("Json files are Different : " , diff )
else:
    #if any or both files are not found displays error message
    if r1=='' and r2!='':
      print ("Json Data File ", json_data_file1,  " Not Found")
    elif r2=='' and r1!='':
      print ("Json Data File ", json_data_file2, " Not Found")
    elif r2=='' and r1=='':
       print ("Json Data Files ", json_data_file1, ",", json_data_file2, " Not Found")
    #if files found with no data displays error message
    elif r1=='0' and r2!='0':
      print ("Json Data File ", json_data_file1,  " exists, but no data found in the file. Zero Bytes!")
    elif r2=='0' and r1!='0':
      print ("Json Data File ", json_data_file2, " exists, but no data found in the file. Zero Bytes!")
    elif r2=='0' and r1=='0':
       print ("Json Data Files ", json_data_file1, ",", json_data_file2, " exists, but no data found in both files. Zero Bytes!")
print ("--------------------------------------------------------", "\n                  Python Word Editor", 
"\n--------------------------------------------------------",
"\n1) Create a file",
"\n1) Open a file",
"\n--------------------------------------------------------")

user_option_choice = input("\nEnter a number option and press ENTER or type 'q' to quit: ")

if(user_option_choice == "1"):
  user_file_content = input("\nStart typing: ")

  user_file_name = input("\nEnter file name and press ENTER: ")

  try:
    text_file = open(user_file_name, "x")
  except FileExistsError:
    print("\nFile with this name already exists.")
  finally:
     text_file.write(user_file_content)
     print("\nFile created.")
     text_file.close()

elif(user_option_choice == "2"):
  user_file_name = input("\nEnter a file name plus the extension: ")
  try:
    text_file = open(user_file_name)
    
  except FileNotFoundError:
    print("\nFile with this name does not exist.")
  finally:
    contents = text_file.read()
    print(contents)
    text_file.close()
    
elif(user_option_choice == "q"):
  print("\nEnd.")

else:
  print("\nError.")
    
  
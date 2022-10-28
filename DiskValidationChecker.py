print ("========================================================            PythonCo. Disk Validation Cheker", 
"\n========================================================")

game_title = input("Enter in the name of the disk and press ENTER: ")
disk_number_input = input("Enter in the disk number and press ENTER: ")
disk_number = int(disk_number_input)

serial_number_input = input("Enter in the disk serial number and press ENTER: ")
serial_number = int(serial_number_input)

print ("\nRESULTS", 
"\n========================================================")

def check_game_title(game_title):
  if game_title in ["Pac Man World", "NHL ‘99’", "Game of Life", "Cardinal Syn"]:  
    print("On Disk List:                 TRUE")
    game_title_result=True
    return game_title_result
  else:
    print("On Disk List:                 FALSE")
    game_title_result=False
    return game_title_result

def check_disk_number(disk_number):
  if((disk_number >= 1496833) and (disk_number <= 5930214)):
    print("Disk Number Match:            TRUE")
    disk_number_result=True
    return disk_number_result
  else:
    print("Disk Number Match:            FALSE")
    disk_number_result=False
    return disk_number_result

def check_serial_number(serial_number):
  if serial_number in [40394, 69302, 76034, 40395, 22490]:  
    print("Disk Serial Number Match:     TRUE")
    serial_number_result=True
    return serial_number_result
  else:
    print("Disk Serial Number Match:     FALSE")
    serial_number_result=False
    return serial_number_result

def return_final_result(game_title_result, disk_number_result, serial_number_result):
  if (game_title_result) and (disk_number_result) and (serial_number_result):
    print("\nTHIS IS A GENUINE DISK")
  else:
    print("\nTHIS IS A NOT GENUINE DISK")

return_final_result(check_game_title(game_title), check_disk_number(disk_number), check_serial_number(serial_number))

    
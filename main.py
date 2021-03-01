import datetime

#GET INPUT VALUES
print ("*****************************************************\n"
      +"******WELCOME TO OUR PICO Y PLACA PREDITOR**********\n"
      +"*****************************************************")

license_number=input("\nInput a license number in format letters-numbers: ")
date_str=input("Input the date in format dd/mm/yy: ")
time_str=input("Input the time in format hh:mm: ")

#PICO Y PLACA RULES 
Mon=[1,2]
Tue=[3,4]
Wed=[5,6]
Thu=[7,8]
Fri=[9,0]


#OBJECT VARIABLES AND FUNCINALITY OF THE APPLICATION

#Variables     
date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
week_day=date_obj.strftime("%a")
last_digit=int(license_number[-1])
allow_messaje = "You can be on the road"
deny_messaje = "You are not allowed to be on the road"

#Functionality
if week_day == "Sat" or week_day == "Sun":
      print( allow_messaje)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
elif (time_str >= "7:00" and time_str <= "9:30") or (time_str >= "16:00" and time_str <= "19:30"): #times were "pico y placa" is activated
      
      if week_day == "Mon" and last_digit in Mon:                                                                                                                                                                                           
            print(deny_messaje)
      elif week_day == "Tue" and last_digit in Tue:
            print(deny_messaje)
      elif week_day == "Wed" and last_digit in Wed:
            print(deny_messaje)
      elif week_day == "Thu" and last_digit in Thu:
            print(deny_messaje)
      elif week_day == "Fri" and last_digit in Fri:
            print(deny_messaje)
      else:
            print(allow_messaje)
      
else:
      print(allow_messaje)             
      





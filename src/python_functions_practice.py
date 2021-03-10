def return_10():
    return 10

def add (num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1-num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1/num_2

def length_of_string(test_string):
    return len(test_string)

def join_string( string_1, string_2 ):
    return string_1+string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)
    
def number_to_full_month_name(month_number):
     import calendar
     return calendar.month_name[month_number]

# example answer-------------------------------
def number_to_full_month_name(month_number):
    if month_number == 1:
        return 'January'
    elif month_number == 3:
        return 'March'         
#-------------------------------------

def number_to_short_month_name(month_number):
     import calendar
     return calendar.month_abbr[month_number]

#example answer--------------------------------------------------

def number_to_short_month_name(month_number:
    short_month_name = number_to_full_month_name(month_numner)[]

#-----------------------------------------

# #Given the length of a side of a cube calculate the volume
#   @unittest.skip("delete this line to run the test")
#   def test_volume_of_cube(self):
#     #add test code here
#     pass

def cube_side(x):
    return x*x*x



def reversed_string(test_string):
    return test_string[::-1]

    # reversed(test_string) ???

# Create a function that given a list which represents street lights 
# given as a parameter(lights), determine if an outage has occurred. 
# A street with a total number of "F" greater than or equal to 2 returns 
# "Outage", anything below returns "Power"

# Example Input: lights = [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

# Example Input: lights = ['T', 'F', 'T']
# Example Output: "Power"


def power(lights):
    count = 0
    for i in lights:
        if i == "F" :
            count += 1
            if count >= 2:
                return "Outage"
            
    return "Power"
            

print(power(['T', 'F', 'T']))


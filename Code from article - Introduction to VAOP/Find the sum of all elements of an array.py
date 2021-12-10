# Find the sum of all elements of an array

# Start of VA-script #####
actions = {
    "Action_00":{
        "_action_description":{
            "_010":"--> init action",
            "_020":"--> Set array M, i = 0; sum = 0"
        },
        "Direction_10":"Action_10",  "_010":"Done"
    },
    "Action_10":{
        "_action_description":{
            "_010":"--> sum = sum + M[i]"
        },
        "Direction_10":"Action_20",  "_010":"Done"
    }, 
    "Action_20":{
        "_action_description":{
            "_010":"--> i = i + 1",
            "_020":"-->if i > len(M) - 1"
        },
        "Direction_10":"Action_END",  "_010":"Yes",
        "Direction_20":"Action_10",   "_020":"No"
    }
}
# End of VA-script #####

# Start of VA-box #####
# init block - Action_00
M = [1,2,7, -8]
sum = 0
i = 0
current_action = "Action_00"
direction = "Direction_10"

while 1 == 1:
    # define next action
    action = actions[current_action][direction]
    previous_action = current_action
    current_action = action    
    print(previous_action,direction,current_action, i, sum)
    print('------------------------')

    if current_action in actions:
        if current_action == "Action_10":
          # Start of Action_10
            sum = sum + M[i]  
            direction = "Direction_10" # Done
          # End of Action_10
        if current_action == "Action_20":
          # Start of Action_20
            i = i + 1 
            direction = "Direction_20" # No
            if i > len(M) - 1:
                direction = "Direction_10" # Yes
          # End of Action_20
        continue
    break # end of loop where 1 == 1

if current_action.find("END") == 0:
       print("\n\Error: current_action:[" + current_action + "]\n")
if current_action.find("END") != 0:
    print("\nsum is [" + str(sum) + ']')
    print('\nThe End')
    
# End of VA-box #####

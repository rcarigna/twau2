# REFERENCE FOR PERSISTING DATA: https://www.renpy.org/doc/html/persistent.html

def DialogueFramework(choices[], bool timer, persist)
    #Count how many choices are in array and execute a UI function based on choices
    if choices.count == 3:
        DialogueUI3(choices) #PARAM: choices array
    elif choices.count == 4:
        DialogueUI4(choices) #PARAM: choices array

    #Check if timer is true, execute timer
    if timer is true:
        timer(30) #PARAM:amount of time in seconds

    #Grab Choice that was selected
    menu:
        choices[1]:
          jump final_answer

        choices[2]:
          jump final_answer

        choices[3]:
          jump final_answer

        choices[4]:
          jump final_answer

    #Figure out how to grab the response with the jump and pass as choice variable to respond
    label final_answer:
        

    #Check if persist data is true
    if persist is true:
        persistData(choice) #PARAM: selected choice

    #Returned chosen item
    return choice

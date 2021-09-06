#SURESH SAHU 1901CE52
#TUT03
def output_individual_roll():
    import os
    try:
       os.mkdir("output_individual_roll")
    except FileExistsError:
        pass

    with open('regtable_old.csv', 'r') as f:
        for l in f:
            words = l.split(',')  
            del words[2]
            del words[4:8]
            if (words[0] =="rollno"):continue
            
            if(os.path.exists("output_individual_roll\\{}.csv".format(words[0]))):
                with open("output_individual_roll\\{}.csv".format(words[0]), 'a') as oir:
                    words=",".join(words)
                    oir.write(words)
            else :
                with open("output_individual_roll\\{}.csv".format(words[0]), 'w') as oir:
                    words=",".join(words)
                    oir.write("rollno,register_sem,subno,sub_type\n")
                    oir.write(words)            
    
    return

def output_by_subject():
    import os
    try:
       os.mkdir("output_by_subject")
    except FileExistsError:
        pass

    with open('regtable_old.csv', 'r') as f:
        for l in f:
            words = l.split(',')
            if (words[2] =="subno"):continue
            del words[4:8]
            del words[2]
            
            if(os.path.exists("output_by_subject\\{}.csv".format(words[2]))):
                with open("output_by_subject\\{}.csv".format(words[2]), 'a') as oir:
                    words=",".join(words)
                    oir.write(words)
            else :
                with open("output_by_subject\\{}.csv".format(words[2]), 'w') as oir:
                    words=",".join(words)
                    oir.write("rollno,register_sem,subno,sub_type\n")
                    oir.write(words)        
    return
# calling the function

output_individual_roll() 
output_by_subject()


import string
import socket
import os


def main():
# Set the path to the directory containing text files
    result = open("/home/data/result.txt", "w+")

    path = "/home/data"
    dir_list = os.listdir(path)
 
# List name of all the text file at location: /home/data
    result.write("List of Files in ")
    result.write(path)
    for x in dir_list:
        result.write(" \n")
        result.write(x)

# No of words in IF text file
    IF_file = open('/home/data/IF.txt','r')
    data = IF_file.read()
    word_IF_file=data.split()
    word_IF=[]
    for i in word_IF_file:
        jo=i.translate(str.maketrans('', '', string.punctuation))
        jo=jo.capitalize()
        word_IF.append(jo)
    result.write(" \n")
    result.write("Number of words in IF: "+str(len(word_IF)))
    result.write(" \n")

# No of words in Limerick text file
    Lime_file = open('/home/data/Limerick.txt','r')
    data = Lime_file.read()
    word_Lime_file=data.split()
    result.write("Number of words in Limerick: "+str(len(word_Lime_file)))
    

# Total no of words in both files
    result.write("\n")
    result.write("Total number of words in both files: "+str(len(word_IF) + len(word_Lime_file)))
    count_IF = []
    set1 = set(word_IF)

    for i in set1: 
        count_IF.append(word_IF.count(i))

    word_IF = list(set(word_IF))


    order_count_IF= sorted(count_IF,reverse=True)


# List the top 3 words with maximum number of counts in IF
    result.write("\n")
    result.write("List the top 3 words with maximum number of counts in IF:")
    j=0
    for j in range(0,3):
         for i in range(0,len(count_IF)):
             if(count_IF[i]== order_count_IF[j]):
                #  print(""+word_IF[i]+" - "+ str(count_IF[i]) )
                 result.write("\n")
                 result.write(""+word_IF[i]+" - "+ str(count_IF[i]) )
            
# IP address of the machine

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
 
    
    result.write("\n")
    result.write("IP Address of the machine: " + ip_address) 
    result.close()
    result_file = open('/home/data/result.txt','r')
    data_result = result_file.read()
    print(data_result)
    
    
if __name__ == "__main__":
    main()

# The data we need retrieve.
#1.  The total number of votes cast
#2.  A complete list of candiates who received votes
#3.  The percentage of votes each candidate won
#4.  The total number of votes each candidate won
#5.  The winner of the election based on popular vote.



# Import the datetime class from the datetime module.
#import os
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)


# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)







#Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
#Open the election results and read the file.
#with open(file_to_load) as election_data:
    # To do: perform analysis.
    #print(election_data)
#dir(os.path)

#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # Print the file object.
    # print(election_data)


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)









# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file
#outfile.close()


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Hello World")

# Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
# Write three counties to the file also works by...
    #txt_file.write("Arapahoe, Denver, Jefferson")

# Write three counties to the file by creating a new line with n
    #txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")











import re
import math
import numpy as np

class Logs_comparing:
    def read_log(self,filename ):
        # = input("Please enter log file path: ")
        filename = input("Please enter log file path: ")
        file = open(filename, "r")
        file_data = file.read()
        file_result = re.findall(r"0\.\d{13}",file_data)
        file_result = list(map(float, file_result))
        return file_result
    
    def avarege(self,log):
        return(math.fsum(log)/len(log))
    
    def difference(self, log1, log2):
        # create 2 lists for saving the difference
        dif_list = [None]*len(log1)

        #calculate the difference
        for i in range(len(log1)):
            dif_list[i] = log2[i] - log1[i]
        result_dif = math.fsum(dif_list)
        pos = 0
        neg = 0
        for i in dif_list:
            if i >= 0:
                pos = pos + 1
            else:
                neg = neg+1
        return result_dif/len(dif_list) , pos, neg

    def variance(self,x):
        return(np.var(x))
     
# Create object of the class
L = Logs_comparing()

#Read the log file. File path must be inputted by user 
file1 = L.read_log("C:\\Users\\gagoo\\Desktop\\Model1_Score.log")
file2 = L.read_log("C:\\Users\\gagoo\\Desktop\\Model2_Score.log")
file3 = L.read_log("C:\\Users\\gagoo\\Desktop\\Model3_Score.log")
release_file = L.read_log("C:\\Users\\gagoo\\Desktop\\Released_Score.log")

# Calculate avareges
av1 = L.avarege(file1)
av2 = L.avarege(file2)
av3 = L.avarege(file3)
rel_av = L.avarege(release_file)
print()
print("First version's avarege: ", av1)
print("Second version's avarege: ", av2)
print("Third version's avarege: ", av3)
print("Released version's avarege: ", rel_av)
print()

# Calculate differencies
dif1, pos1, neg1 = L.difference(file1,release_file)
dif2, pos2, neg2  = L.difference(file2,release_file)
dif3, pos3, neg3 = L.difference(file3,release_file)
print("Difference between release and first version,", dif1,"Positives: ", pos1,"Negatives: ", neg1)
print("Difference between release and second version,", dif2,"Positives: ", pos2,"Negatives: ", neg2)
print("Difference between release and third version,", dif3,"Positives: ", pos3,"Negatives: ", neg3)
print()
# Calculate variances
v1 = L.variance(file1) 
v2 = L.variance(file2)
v3 = L.variance(file3)
rel_v = L.variance(release_file)

print("Variance of log1: ", v1)
print("Variance of log2: ", v2)
print("Variance of log3: ", v3)
print("Variance of released version: ", rel_v)



# C:\\Users\\gagoo\\Desktop\\Model1_Score.log
# C:\\Users\\gagoo\\Desktop\\Model2_Score.log
# C:\\Users\\gagoo\\Desktop\\Model3_Score.log
# C:\\Users\\gagoo\\Desktop\\Released_Score.log 

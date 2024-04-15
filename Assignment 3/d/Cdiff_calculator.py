#Constants
Knj = 0.57
Kpj = 0.79
Cj = 2 #fF/um
Cjsw = 0.28 #fF/um
Kpjsw = 0.86
Knjsw = 0.61
lamda = 0.125 #um
#Calculators
def nmosCdiffCalculator(area,perimeter):
    Cdiff = (Cj * Knj * area * lamda**2) + (Cjsw * Knjsw * perimeter * lamda)
    return round(Cdiff,5) #fF

def pmosCdiffCalculator(area,perimeter):
    Cdiff = (Cj * Kpj * area * lamda**2) + (Cjsw * Kpjsw * perimeter * lamda)
    return round(Cdiff,5) #fF

#We first list and calculate all the nmos and then all the pmos transistors
transistors_type = ["NMOS" , "NMOS", "NMOS" ,"PMOS" ,"PMOS", "PMOS"]
transistors_name = [1,2,3,1,2,3]
transistors_source_area = [20 , 24 , 40 ,60, 60 , 60]
transistors_drain_area = [20, 24 , 24 ,100 ,60 ,100]

transistors_source_perimeter = [14, 6 ,18, 6, 6 ,6]
transistors_drain_perimeter = [10, 6 ,6 ,30, 6 ,30]

for i in range(0,len(transistors_drain_area)):
    if(transistors_type[i] == "NMOS"):
        Cs = nmosCdiffCalculator(transistors_source_area[i],transistors_source_perimeter[i])
        Cd = nmosCdiffCalculator(transistors_drain_area[i],transistors_drain_perimeter[i])
    else:
        Cs = pmosCdiffCalculator(transistors_source_area[i],transistors_source_perimeter[i])
        Cd = pmosCdiffCalculator(transistors_drain_area[i],transistors_drain_perimeter[i]) 

    print(transistors_type[i] + " " + str(transistors_name[i]) + " & " + str(transistors_source_area[i]) + " & " + str(transistors_drain_area[i]) + " & " +  str(transistors_source_perimeter[i]) + " & " + str(transistors_drain_perimeter[i]) + " & " + str(Cs) + " & " + str(Cd) + " & " + str(round(Cs + Cd,5))  + "\\\\" + "\n\hline")
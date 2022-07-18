print("Input Conversion: ",end=" ")
X = float(input())
print("Input number of Reactants: ",end=" ")
Reactants = int(input())
print("Input number of Products: ",end=" ")
Products = int(input())

R=[] 
P=[] 


print("First reactant stoichiometric coefficient is 1")
print("Insert",Reactants-1,"space separated values Stoichiometric coefficient of remaining reactants")

R.append(1)
inpuT = input()
j = 0
for i in inpuT.split(" "):
    R.append(int(i))
    j+=1

print("Insert",Products,"space separated values Stoichiometric coefficient of products")
b = input()
j=0
for i in b.split(" "):
    P.append(int(i))
    j+=1

for i in range(1,Reactants):
    R[i]=R[i]

for i in range(Products):
    P[i]=P[i]




print("Input Inlet temperature of reactants in Kelvin ",end=" ")
To = float(input())
print("Input Ambient temperaturein in Kelvin ",end=" ")
Ta = float(input())

CP = [] 
Sum_CP_Reactants=0
Sum_CP_Product=0

print("Insert",Reactants,"space separated values mean specific heat capacity of reactants")
inpuT = input()
j = 0
for i in inpuT.split(" "):
    CP.append(int(i))
    Sum_CP_Reactants+=(int(i)*R[j])
    j+=1

print("Insert",Products,"space separated values mean specific heat capacity of products")
b = input()
j=0
for i in b.split(" "):
    CP.append(int(i))
    Sum_CP_Product+=(int(i)*P[j])
    j+=1


DCp=Sum_CP_Product-Sum_CP_Reactants

Flow_rates = [] 

print("Insert",Reactants,"space separated values flowrate of reactants")
inpuT = input()
j = 0
for i in inpuT.split(" "):
    Flow_rates.append(int(i))

print("Insert",Products,"space separated values flowrate of products")
b = input()
j=0
for i in b.split(" "):
    Flow_rates.append(int(i))


Theta_Cpi = 0
Flowrate_of_first_reactant = Flow_rates[0]
for i in range(len(Flow_rates)):
    inpuT = (Flow_rates[i]*CP[i]/Flowrate_of_first_reactant)
    Theta_Cpi+=inpuT

print("Input Heat transfer area in m^2:",end=" ")
A = float(input())
Tr = 298
DHr = 0


print("Insert",Reactants,"space separated values for Standard enthalphy of reactants")
inpuT = input()
j = 0
for i in inpuT.split(" "):
    DHr-=(int(i)*R[j])
    j+=1


print("Insert",Products,"space separated values Standard enthalphy of products")
b = input()
j=0
for i in b.split(" "):
    DHr+=(int(i)*P[j])
    j+=1


print("type 'cstr' for CSTR and 'pfr' for PFR")

inpuT = input()
if inpuT == "cstr":
    print("type 'adiabatic' for ADIABATIC and 'non adiabatic' for NON-ADIABATIC")
    b = input()
    if b == "adiabatic":
        print("Temperature in K is",(-X*((DCp*Tr)-DHr) - (To*Theta_Cpi))/((-X*DCp)-(Theta_Cpi)))
    elif b == "non adiabatic":
        print("Input Overall heat transfer coefficient in Watt/m^2*K ",end=" ")
        U = float(input())
        print("Temperature in K is",(-X*((DCp*Tr)-DHr) - (U*A*Ta/Flow_rates[0]) - (To*Theta_Cpi))/((-X*DCp)-(U*A/Flow_rates[0])-(Theta_Cpi)))
    else:
        print("Incorrect input spelling")
elif inpuT == "pfr":
    print("Temperature in K is",(X*(-DHr)+(Theta_Cpi*To)+(X*DCp*Tr))/((Theta_Cpi)+(X*DCp)))
else:
    print("Incorrect input spelling")


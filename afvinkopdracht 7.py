
def lees_inhoud():
    with open('SC_expression.txt') as f:
        Lijst1 = []
        Lijst2 = []


        f.readline()
        for line in f:
            Lijst1.append(line.split(',')[0])
            Lijst2.append(float(line.split(',')[1]))


    return Lijst1, Lijst2

def gemiddelde(Lijst):
    totaal = 0

    Count = 0

    for i in Lijst:
        totaal += Lijst[Count]
        Count += 1

    average = totaal / Count

    print(average)
    return average

def groter(Lijst1, Lijst2):
    Lijst3 = []
    Count = 0

    for i in Lijst2:
        if Lijst2[Count] >= 50:
            Lijst3.append(Lijst1[Count])
        Count += 1
    print(Lijst3)
    return Lijst3
    
    
        
    
           
            
            





def main():
    Lijst1, Lijst2 = lees_inhoud()
    average = gemiddelde(Lijst2)
    Lijst3 = groter(Lijst1, Lijst2)
    



main()

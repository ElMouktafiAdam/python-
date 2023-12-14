Base=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvies=int(input("Enter le nombre de conviées a la fondue:"))

fromage=fromage * nbConvies / Base
eau=eau * nbConvies / Base
ail=ail * nbConvies / Base
pain=pain * nbConvies / Base
print("Pour faire une  fondue fribourgeoise pour" ,nbConvies, "personnes, il vous faut : ")
print("- ",fromage, "gr de fromage" )
print("- ",eau, "dl d'eau" )
print("- ",ail, "gousse d'ail" )
print("- ",pain, "gr de pain" )

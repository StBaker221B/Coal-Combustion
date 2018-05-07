
import copy
import sys,getopt

# f = open('21trj1e5','r')
inputfile = ""
outputfile = ""

def main(argv):
    inputfile = ""
    outputfile = ""
        
    try:
        opts, args = getopt.getopt(argv,"hi:o",["ifile=","ofile="])
    except getopt.GetoptError:
        print('read.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('read.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('inputfile：', inputfile)
    # print('输出的文件为：', outputfile)
    
    return inputfile, outputfile

if __name__ == "__main__":
   inputfile,outputfile = main(sys.argv[1:])

fname1 = inputfile + ".path"
print(fname1)
fpath = open(fname1,'a+')
fname2 = inputfile + ".molecules"
print(fname2)
fmol = open(fname2,'a+')
fname3 = inputfile + ".prod"
print(fname3)
fprod = open(fname3,'a+')
fname4 = inputfile + ".total"
print(fname4)
ftotal = open(fname4,'a+')

fname5 = inputfile + ".env"
print(fname5)
fenv = open(fname5,'a+')
fname6 = inputfile + ".struct"
print(fname6)
fstruct = open(fname6,'a+')

fname7 = inputfile + ".molsum"
print(fname7)
fmolsum = open(fname7,'a+')
fname8 = inputfile + ".reac"
print(fname8)
freac = open(fname8,'a+')


fmol.write(str('inputfile：' + inputfile) + "\n")
fpath.write(str('inputfile：'+ inputfile) + "\n")
fprod.write(str('inputfile：' + inputfile) + "\n")
ftotal.write(str('inputfile：' + inputfile) + "\n")

fenv.write(str('inputfile：' + inputfile) + "\n")
fstruct.write(str('inputfile：' + inputfile) + "\n")

fmolsum.write(str('inputfile：' + inputfile) + "\n")
freac.write(str('inputfile：' + inputfile) + "\n")

f = open(inputfile,'r')
# find the atom list
line = f.readline()

def readatoms(line):
    atomlist = {}
    # l = line.split()
    while(line):
        l = line.split()
        if(l[0][0] in "0123456789"):
            atomid = int(l[0])
            typenum = int(l[1])
            mass = float(l[2])
            if( abs(mass-12) < 0.5 ):
                element = "C"
            elif( abs(mass-1) < 0.5 ):
                element = "H"
            elif( abs(mass-16) < 0.5 ):
                element = "O"
            elif( abs(mass-14) < 0.5 ):
                element = "N"
            elif( abs(mass-32) < 0.5 ):
                element = "S"
            # elif( abs(mass-1) < 0.5 ):
            #     element = "H"
            atomlist[atomid] = [element, typenum, mass]
            # print(atomlist[atomid])

        elif( l[0] == "step:" ):
            return atomlist,line

        line = f.readline()

def molanalysis(molecules, atomid1, atomid2, atomlist):
    
    state = 0

    for molecule in molecules:
        if(atomid1 in molecule):
            if(atomid2 in molecule ):
                if( atomid2 not in molecule[atomid1][1]):
                    molecule[atomid1][1].append(atomid2)
                if( atomid1 not in molecule[atomid2][1]):
                    molecule[atomid2][1].append(atomid1)
                state == 1
            else:                
                molecule[atomid2] = [atomlist[atomid2],[atomid1]]
                molecule[atomid1][1].append(atomid2)
                state == 1
        elif(atomid2 in molecule):  
            molecule[atomid1] = [atomlist[atomid1],[atomid2]]
            molecule[atomid2][1].append(atomid1)
            state == 1
      
    if(state == 0 ):
        molecule = {}
        molecule[atomid1] = [atomlist[atomid1],[atomid2]]
        molecule[atomid2] = [atomlist[atomid2],[atomid1]]
        molecules.append(molecule)
        state == 1
    
    # al = set()
    # for mol in molecules:
    #     for atom in mol:
    #         mol[atom][1] = list(set(mol[atom][1])) # remove the redundant
    #         al.add(atom)

    # for atom in atomlist:
    #     if( atom not in al ):
    #         molecule = {}
    #         molecule[atom] = [atomlist[atomid1],[]]
    #         molecules.append(molecule)

    
    return molecules

def molcheck(molecules, atomlist):
    for mol1 in molecules:
        for mol2 in molecules:
            if (mol1 != mol2):
                # continue
                for atom in mol2:
                    if( (atom in mol1) and (atom != "COMP")):
                        for k,v in mol2.items():
                            if( k=="COMP"):
                                continue
                            elif(k not in mol1):
                                mol1[k] = v
                            elif(k in mol1):
                                mol1[k][1].extend(v[1]) # = mol1[k][1] if ( len(mol1[k][1]) >= len(v[1]) ) else v[1]
                        molecules.remove(mol2)
                        break
    
    al = set()
    for mol in molecules:
        for atom in mol:
            mol[atom][1] = list(set(mol[atom][1])) # remove the redundant
            al.add(atom)

    for atom in atomlist:
        if( atom not in al ):
            molecule = {}
            molecule[atom] = [atomlist[atom],[]]
            molecules.append(molecule)

    return molecules

def molcollect(molecules):
    moltotal = {}
    for mol in molecules:
        if(mol["COMP"] not in moltotal):
            moltotal[mol["COMP"]] = 1
        else:
            moltotal[mol["COMP"]] += 1
    return moltotal

def molformula(molecules):
    for molecule in molecules:
        c = 0
        h = 0
        o = 0
        n = 0
        s = 0
        for atomid in molecule:
            if( atomid != "COMP" ):
                element = molecule[atomid][0][0]
                if(element == "C" ):
                    c = c+1
                elif (element == "H" ):
                    h = h+1
                elif (element == "O" ):
                    o = o+1
                elif (element == "N" ):
                    n = n+1
                elif (element == "S" ):
                    s = s+1
        
        cn = "C"+str(c) if c else ""
        hn = "H"+str(h) if h else ""
        on = "O"+str(o) if o else ""
        nn = "N"+str(n) if n else ""
        sn = "S"+str(s) if s else ""
        comp = cn + hn + on + nn + sn
        '''
        if(c):
            comp += "C"
            comp += str(c)
            if(h):
                comp += "H"
                comp += str(h)
                if(o):
                    comp += "O"
                    comp += str(o)
            elif(o):
                comp += "O"
                comp += str(o)
        elif(h):
            comp += "H"
            comp += str(h)
            if(o):
                comp += "O"
                comp += str(o)
        elif(o):
            comp += "O"
            comp += str(o)
        '''
        molecule["COMP"] = comp
    return molecules

def prodtrack(interval):
    prodlist = []    
    for mol2 in interval[1]:
        prod = [[mol2["COMP"]]]
        # prod.append(mol2["COMP"])
        for mol1 in interval[0]:
            for atom2 in mol2:
                if( (atom2 in mol1) and (atom2 != "COMP") ):
                # t = reanalysis(mol1,mol2)
                # if(t == 1):
                    prod.append(mol1["COMP"])
        prodlist.append(prod)
    return prodlist


# def reanalysis(mol1, mol2):
#     for atom2 in mol2:
#         if ((atom2 in mol1) and (atom2 != "COMP") ):
#             return 1
#     return 0



# def prodtrack(path):
#     # prod = {}
#     prodlist = []    
#     for mol2 in path[1]:
#         prod = [[mol2["COMP"]]]
#         # prod.append(mol2["COMP"])
#         for mol1 in path[0]:
#             t = reanalysis(mol1,mol2)
#             if(t == 1):
#                 # reac.append(re)
#                 # prod.append(pr)
#                 prod.append(mol1["COMP"])
#         prodlist.append(prod)
#     return prodlist



def reacinteg(prodlist):
    pl = copy.deepcopy(prodlist)
    # remove the same reac & integ the reac sharing the same reactants
    # for prod1 in pl:
    i = 0
    while(i < len(pl)):
        prod1 = pl[i]
        pr1 = []
        pr1.extend(prod1[0])
        re1 = prod1[1:]
        t = i+1
        # for prod2 in pl:
        while(t < len(pl)):
            prod2 = pl[t]
            pr2 = []
            pr2.extend(prod2[0])
            re2 = prod2[1:]
            if( (pr1 == pr2) and (re1 == re2) ):
                pl.remove(prod2)
                continue
            # elif(pr1 != pr2):
            #     if(re1 == re2):
            #         p = []                
            #         p.extend(pr1)
            #         p.extend(pr2)
            #         prod1[0] = list(set(p))
            #         pl.remove(prod2)
            #         continue
            t += 1
        i += 1

    # for prod1 in pl:
    #     pr1 = []
    #     pr1.extend(prod1[0])
    #     re1 = prod1[1:]
    #     for prod2 in pl:
    #         pr2 = []
    #         pr2.extend(prod2[0])
    #         re2 = prod2[1:]
    #         if(pr1 == pr2):
    #             if(re1 == re2):
    #                 pl.remove(prod2)
    #                 continue
    #         elif(pr1 != pr2):
    #             if(re1 == re2):
    #                 p = []                
    #                 p.extend(pr1)
    #                 p.extend(pr2)
    #                 prod1[0] = list(set(p))
    #                 pl.remove(prod2)
    #                 continue

    # for prod1 in pl:
    #     for prod2 in pl:
    #         if(prod1 == prod2):
    #             pl.remove(prod2)

    for prod1 in pl:
        pr1 = []
        pr1.extend(prod1[0])
        re1 = prod1[1:]        
        for prod2 in pl:
            pr2 = []
            pr2.extend(prod2[0])
            re2 = prod2[1:] 
            if(pr1 != pr2):
                if( re1 == re2 ):
                    p = []                
                    p.extend(pr1)
                    p.extend(pr2)
                    prod1[0] = list(set(p))
                    pl.remove(prod2)
                    continue
            # inter = list( set(re1).intersection(set(re2) ) )
            # if( len(inter) > 0 ):
            #     p = []                
            #     p.extend(pr1)
            #     p.extend(pr2)
            #     prod1[0] = list(set(p))
            #     pl.remove(prod2)
            #     continue

    
    # for prod1 in pl:
    #     pr1 = []
    #     pr1.extend(prod1[0])
    #     re1 = prod1[1:]        
    #     for prod2 in pl:
    #         pr2 = []
    #         pr2.extend(prod2[0])
    #         re2 = prod2[1:]
    #         for(re in re1):
    #             if(re in re2):
    #                 prod1[0]

    for prod in pl:
        # pr = prod[0]
        # re = prod[1:]
        prod[1:] = list(set(prod[1:]))
        prod.insert(1,"<-")
        # prod = [pr]
        # prod.extend(re)
    return pl


# def reacinteg(prodlist):
#     pl = copy.deepcopy(prodlist)
#     i = 0
#     while(i < len(pl)):  
#     # for prod1 in pl:      
#         prod1 = pl[i]
#         pr1 = prod1[0]
#         re1 = prod1[1:]
#         # if( i < (len(pl)-1) ):
#         t = i+1
#         print(i)
#         while(t < len(pl)): 
#         # for prod2 in pl:
#             prod2 = pl[t]
#             pr2 = prod2[0]
#             re2 = prod2[1:]        
#             if( (pr1 == pr2) and (re1 == re2) ):
#                 # if( re1 == re2 ):
#                 pl.remove(prod2)                    
#                     # continue
#             else:
#                 t += 1
#                 # continue
#         # print("\n", pl,"\n")
#         i += 1

#     print("\n")
#     for i in pl:
#         print(i)
#     print("\n")

#     for prod1 in pl:
#         pr1 = []
#         pr1.extend(prod1[0])
#         re1 = prod1[1:]
        
#         for prod2 in pl:
#             pr2 = []
#             pr2.extend(prod2[0])
#             re2 = prod2[1:] 
#             if(pr1 != pr2):
#                 if( re1 == re2 ):
#                     p = []                
#                     p.extend(pr1)
#                     p.extend(pr2)
#                     prod1[0] = list(set(p))
#                     pl.remove(prod2)
#                     continue
                
#     return pl

# l = line.split()

atomlist = {}
molecules = []
interval = []

moltotal = {}
prodlist = []
pl = []

total = {}

while(line):
    l = line.split()
    if("simulation_name" in line):
        print(line)
        fmol.write(line)
        fpath.write(line)
        fprod.write(line)
        fenv.write(line)
        fstruct.write(line)
        fmolsum.write(line)
        freac.write(line)

        atomlist,line = readatoms(line)
        print(line)
        fmol.write(line)
        fpath.write(line)
        fprod.write(line)

        fenv.write(line)
        fstruct.write(line)

        fmolsum.write(line)
        freac.write(line)

        # break
        # continue
    
    elif( l[0] == "step:" ):
        # print(line)
        molecules = molcheck(molecules, atomlist )
        molecules = molcheck(molecules, atomlist )
        molecules = molcheck(molecules, atomlist )
        # molecules = molcheck(molecules)
        molecules = molformula(molecules)
        for mol in molecules:
            # print(mol["COMP"], mol)
            fmol.write(str(mol["COMP"]) + " " + str(mol) + "\n")

            if( (mol["COMP"] == "O2") or (mol["COMP"] == "C1O2") or (mol["COMP"] == "N2") ):
                for key in mol:
                    if(key != "COMP"):
                        fenv.write("\tParticleIdentifier == " + str(key) + " || \n" )
                # fenv.write(str(mol["COMP"]) + " " + str(mol) + "\n")
            else:
                for key in mol:
                    if(key != "COMP"):
                        fstruct.write("\tParticleIdentifier == " + str(key) + " || \n" )

        moltotal = molcollect(molecules)
        total[l[1]] = moltotal

        print(moltotal)
        fmol.write(str(moltotal) + "\n")
        fpath.write(str(moltotal) + "\n")
        fprod.write(str(moltotal) + "\n")
        fmolsum.write(str(moltotal) + "\n")
        
        if(len(interval) < 1 ):
            interval.append(molecules)
        else:
            interval.append(molecules)
            prodlist = prodtrack(interval)
            
            for prod in prodlist:
                # print(prod)
                fprod.write(str(prod) + "\n")
            pl = reacinteg(prodlist)

            interval[0] = interval[1]
            interval.pop()
        
            # print("\n the path")
            fpath.write(str("\n the path\n"))
            for prod in pl:
                # print(prod)
                fpath.write(str(prod) + "\n")
                pr = prod[0]
                re = prod[2:]
                if(pr != re):
                    freac.write(str(prod) + "\n")

        molecules = []
        moltotal = {}
        print("\n",line)
        fmol.write(str("\n" + line) + "\n")
        fpath.write(str("\n" + line) + "\n")
        fprod.write(str("\n" + line) + "\n")

        fenv.write(str("\n" + line) + "\n")
        fstruct.write(str("\n" + line) + "\n")

        fmolsum.write(str("\n" + line) + "\n")
        freac.write(str("\n" + line) + "\n")

    elif( (len(l) > 2)  and ("." not in l[1]) and ("." in l[2] ) and (l[0][0] in "0123456789" ) ):
        atomid1 = int(l[0])
        atomid2 = int(l[1])
        molecules = molanalysis(molecules, atomid1, atomid2, atomlist)
        
    line = f.readline()

# for key in atomlist:
#     print(key,atomlist[key])

molecules = molcheck(molecules, atomlist)
molecules = molcheck(molecules, atomlist)
# molecules = molcheck(molecules)
molecules = molformula(molecules)
for mol in molecules:
    # print(mol["COMP"], mol)
    fmol.write(str(mol["COMP"]) + " " + str(mol) + "\n")
    if( (mol["COMP"] == "O2") or (mol["COMP"] == "C1O2") or (mol["COMP"] == "N2") ):
        for key in mol:
            if(key != "COMP"):
                fenv.write("\tParticleIdentifier == " + str(key) + " || \n" )
        # fenv.write(str(mol["COMP"]) + " " + str(mol) + "\n")
    else:
        for key in mol:
            if(key != "COMP"):
                fstruct.write("\tParticleIdentifier == " + str(key) + " || \n")


moltotal = molcollect(molecules)

print(moltotal)
fmol.write(str(moltotal) + "\n")
fpath.write(str(moltotal) + "\n")
fprod.write(str(moltotal) + "\n")
fmolsum.write(str(moltotal) + "\n")

if(len(interval) < 1 ):
    interval.append(molecules)
else:
    interval.append(molecules)
    prodlist = prodtrack(interval)
    
    for prod in prodlist:
        # print(prod)
        fprod.write(str(prod) + "\n")
    pl = reacinteg(prodlist)

    interval[0] = interval[1]
    interval.pop()

    # print("\n the path")
    fpath.write(str("\n the path\n"))
    for prod in pl:
        # print(prod)
        fpath.write(str(prod) + "\n")
        pr = prod[0]
        re = prod[2:]
        if(pr != re):
            freac.write(str(prod) + "\n")
       


print(line)
fmol.write(line)
fpath.write(line)
fprod.write(line)


f.close()
fpath.close()
fmol.close()
fprod.close()
fstruct.close()
fenv.close()

fmolsum.close()
freac.close()

mollist = []
for step in total:
    # print(step,total[step])
    for mol in total[step]:
        if(mol not in mollist):
            mollist.append(mol)

ml = ""
for mol in mollist:
    ml += mol
    ml += "\t"
ftotal.write("step" + "\t" + ml + "\n")
for step in total:
    numlist = []
    for n in range( len(mollist) ):
        if(mollist[n] in total[step] ):
            numlist.append(total[step][mollist[n]] )
        else:
            numlist.append("0")
    nl = ""
    for num in numlist:
        nl += str(num)
        nl += "\t"
    ftotal.write(str(step) + "\t" + nl + "\n" )

ftotal.close()



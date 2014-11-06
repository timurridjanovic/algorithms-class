

def open_file(file):
    f = open(file, 'r')
    try:
        max1 = 0
        max2 = 0
        name1 = None
        name2 = None
        names = []
        for line in f:
            row = line.split(',')
            row = [row[0], row[1], int(row[2].replace('\n', ''))]
            if row[1] == 'F':
                names.append(row)
        return sorted(names, key=lambda x: x[2])[-2]
            
              
                
                
    
        print names
            
    finally:
        f.close()

        
print open_file('popular_names.txt')        




#or



def open_file2(file):
    f = open(file, 'r')
    try:
        max1 = 0
        max2 = 0
        name1 = None
        name2 = None
        names = []
        for line in f:
            row = line.split(',')
            row = [row[0], row[1], int(row[2].replace('\n', ''))]
            if row[1] == 'F':
                if row[2] > max1:
                    max2 = max1
                    name2 = name1
                    max1 = row[2]
                    name1 = row[0]

                elif row[2] > max2:
                    max2 = row[2]
                    name2 = row[0]
        return name2, max2
            
              
                
                
    
        print names
            
    finally:
        f.close()

        
print open_file2('popular_names.txt') 

# 1.) TALÁLD MEG EGY STRING ELŐFORDULÁSÁNAK INDEXEIT EGY LISTÁBAN:
# MEGOLDÁS 1.: FOR LOOP- range(len(X))-RE ÉS KIGYŰJTENI LISTÁBA
def finde(haystack,needle):
    solution = []
    for index in range(len(haystack )):
        if haystack[index] == needle:
            solution.append(index)
    return solution
        
    
print(finde(["c","o","d","e","c","o","o","l"], "o"))

# MEGOLDÁS 2.: FOR LOOP- range(len(X))-RE ÉS LIST COMPREHENSION
def finde2(haystack,needle):
    return [index for index in range(len(haystack)) if haystack[index] == needle]
    

print(finde2(["c","o","d","e","c","o","o","l"], "o"))

# 2.) A LISTÁBAN TÖBBSZÖR ELŐFORDULÓ ELEMEKHEZ FŰZZ SZÁMOKAT ELŐFORDULÁS SZERINT
# MEGOLDÁS: DICTIONARY-VEL.
def device_names_system(devicenames ):
    li1 = {}
    li2 = []
    for i in devicenames:
        if i not in li1:
            li1[i] = 0
            li2.append(i)
        else:
            li1[i] += 1
            li2.append(f"{i}{li1[i]}")
    return li2
            
        
print(device_names_system(['switch', 'tv', 'switch', 'tv', 'switch', 'tv']))

# 3.) STRINGBŐL A PÁROS SZÁMOK VAGY PÁRATLAN SZÁMOK ÖSSZEGE NAGYOBB-E
# https://www.codewars.com/kata/57f7b8271e3d9283300000b4/solutions/python

# MEGOLDÁS: 
def even_or_odd(s):
    diff = 0
    for char in s:
        num = int(char )
        diff += (-1) ** (num % 2) * num 
    return 'Even and Odd are the same' if diff == 0 else 'Even is greater than Odd' if diff > 0 else 'Odd is greater than Even'

MEGOLDÁS: 

def even_or_odd(s):
    n=sum(x * (-1 if x % 2 else 1) for x in map(int,s))
    return 'Even is greater than Odd' if n > 0 else \
           'Odd is greater than Even' if n < 0 else \
           'Even and Odd are the same'

# 4.) TIPIZÁLÁS

        j = 0
        shoot_row = 0
        for i in list_abc:
            if user_input_a.lower() == list_abc[j]:
                shoot_row = j
            j += 1

# 5.) TALÁLJUK MEG, HOGY KÉT ITERABLE ELEMEI KÖZÜL MELYEK VANNAK AZONOS HELYEN. 

# KÉT LOOPAL: A KÜLSŐ LOOP AZÉRT KELL, MERT ITERABLE VAN AZ ITERABLE-BAN

def solve(arr):
    abc = "abcdefghijklmnopqrstuvwxyz00000000000000000000000000000000000000000000000000000000000000000000"
    solution = []
    j = 0
    for i in arr:
        o = 0
        for index in range(len(arr[j])):
            if (arr[j][index]).lower() == abc[index]:
                o += 1
        solution.append(o)
        j += 1
    return solution
        
        


# solve(["abode","ABc","xyzD"]) = [4, 3, 1]

print(solve(["abode", "ABc", "xyzDasasaxyxyxaxadggfhfgdfsdfsdegfrggf"]))

# OKOSAN:
def solve(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]

# DICT:
def solve(arr):
    def cou(arg):
        al = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
              'w': 23, 'x': 24, 'y': 25, 'z': 26}
        num = 0
        arg = ("".join(arg)).lower()
        for x in range(len(arg)):
            if x + 1 == al[arg[x]]:
                num += 1
        return num

    res=[]
    for x in range(len(arr)):
        res.append(cou(arr[x]))
    return res



# FONTOS INDEX ERROR:
def solve(arr):
    solution = []
    j = 0
    for i in arr:
        for i in arr[j]:
            absolut = abs(i)
            print(absolut)
            solution.append(absolut)
            j += 1
            print(j)
            if j == 2:
                break
    print(solution)
        


solve([[10,-15],[-1,-3]])

10
1
15
2


def solve(arr ):
    solution = []
    j = 0
    for i in arr:
        for i in arr[j]:
            absolut = abs(i)
            print(absolut)
            solution.append(absolut)
        j += 1
    print(solution)
        


solve([[10,-15],[-1,-3]])

10
15
1
3
[10, 15, 1, 3]



def solve(arr):
    solution = []
    maxi = []
    j = 0
    for i in arr:
        for i in arr[j]:
            absolut = abs(i)
            print(absolut)
            solution.append(absolut)
        maxi.append(max(solution))
        solution.clear()
        j += 1
    print(maxi)
    final = 0
    for i in range (len(maxi)):
        try:
            final = maxi[i] * maxi[i+1]
            maxi[i] = final
            del maxi[i+1]
        except:
            None
    maximum = maxi[0]*maxi[1]
    return maximum

        


print(solve([[10,-15],[-1,-3], [1,2]]))

def solve(arr):
    
    p, q = 1, 1
    
    for k in arr:
        
        x, y = max(k), min(k)
        
        a = p * x
        b = q * x
        c = p * y
        d = q * y
        
        p = max(a, b, c, d)
        q = min(a, b, c, d)
            
    return max(p, q)

10
10
-15
-15
-10
15
-30
45
90
-60
45
-30
90


def solve(st,k ):
    letters = "abcdefghijklmnopqrstuvwxyz"
    st_list = list(st)
    st_list_ghost = st_list.copy()
    trash = []
    to_be_compared_index = 0
    counter = 0
    if k >= len(st):
        return ""
    else:
        while counter < k:
            for index in range(len(st_list)):
                if st_list[index] == letters[to_be_compared_index]:
                    del (st_list_ghost[index-(len(trash))])
                    trash.append(st_list[index])
                    counter += 1
                if counter == k:
                    break
            st_list = st_list_ghost
            st_list_ghost = st_list.copy()
            trash.clear()
            print(trash)
            print(counter)
            print(st_list)
            to_be_compared_index += 1
        print(st_list)
        return "".join(st_list)

# Egyet mindig meghagyós probléma és az out of range probléma oka = törlök az eredeti listából a for loopban!
# Megoldás: ghost lista, ami minden egyes for loop után lecseréli az eredeti listát. A ghost listából mindig annyit törlök, mint a trash hossza, de a trash-t is looponként üríteni kell
# while loopban for loop
# két index két különböő listában összehasonlítás

print(solve('aaabbbccc', 5))

def draw_triangle(height, border_color = "1", fill_color = "1"):
    matrix = height * [7 * [border_color]]
    try:
        if (height) > 3:
            matrix[3: (len(matrix))-1] = (height - 4) * [[border_color] + 5 * [fill_color] + [border_color]]
    except:
        print("Error!")
    # Nagyon fontos, hogy ne csak a sorok legyenek megadva sliceinghoz, hanem az elején (height-4) az oszlopok száma is, ami a slicinggal érintett
    matrix[0] = 3 * ["0"] + [border_color] + 3 * ["0"]
    matrix[1] = 2 * ["0"] + [border_color] + [fill_color] + [border_color] + 2 * ["0"]
    matrix[2] = 1 * ["0"] + [border_color] + 3 * [fill_color] + [border_color] + 1 * ["0"]
    for row in matrix:
        print(" ".join(row))
    return matrix

def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


def draw_christmas_tree(blocks, border_color = "1", fill_color = "1"):
    height = 3 * blocks
    width = 3 + (2 * blocks)
    matrix = height * [width * [border_color]]
    fill_variable = 1
    zero_variable = 0
    for index in range(len(matrix)):
        try: 
            if index == 0:
                matrix[index] = (width // 2 - zero_variable) * ["0"] + [border_color] + (width // 2 - zero_variable) * ["0"]
            if index == 1:
                matrix[index] = (width // 2 - zero_variable - 1) * ["0"] + [border_color] +  fill_variable * [fill_color] + [border_color] + (width // 2 - zero_variable - 1) * ["0"]
            if index == 2:
                matrix[index] = (width // 2 - zero_variable - 2) * ["0"] + [border_color] +  (fill_variable + 2) * [fill_color] + [border_color] + (width // 2 - zero_variable - 2) * ["0"]
            if (index) >= 5:
                if (index) % 3 == 2:
                    matrix[index - 2] = (width // 2 - zero_variable - 1) * ["0"] + [border_color] +  fill_variable * [fill_color] + [border_color] + (width // 2 - zero_variable - 1) * ["0"]
                    matrix[index - 1] = (width // 2 - zero_variable - 2) * ["0"] + [border_color] +  (fill_variable + 2) * [fill_color] + [border_color] + (width // 2 - zero_variable - 2) * ["0"]
                    matrix[index] = (width // 2 - zero_variable - 3) * ["0"] + [border_color] +  (fill_variable + 4) * [fill_color] + [border_color] + (width // 2 - zero_variable - 3) * ["0"]
                    fill_variable += 2
                    zero_variable += 1
        except IndexError:
            None
        matrix[-1] = width * [border_color]
    for row in matrix:
        print(" ".join(row))
    return matrix
    
# If statementek után növelem a dinamikus változót
# A nagyobb szekvenciával ifezek (3-mal osztva), és az alapján változtatom a közben (a 3 -as szekvencián belül előtte!) lévőket is, mielőtt a dinamikus változó megnőne. És fontos az ifes feltételben a maradék is


def remove_url_anchor(url):
    url_list = list(url)
    solution_list = []
    for index in range(len(url_list)):
        if url_list[index] == "#":
            solution_list += url_list[:index]
            break
        if not "#" in url_list:
            solution_list = url_list
    return "".join(solution_list)

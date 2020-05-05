

data_dict = {}
data_dict['Tetrahedron'] = 4
data_dict['Cube'] = 6
data_dict['Octahedron'] = 8
data_dict['Dodecahedron'] = 12
data_dict['Icosahedron'] = 20




number_of_polyhedrons = int(input())
list_of_polyhedrons = []
i = 1
while i <= number_of_polyhedrons:
    l = input()
    if l:
        list_of_polyhedrons.append(l)
    else:
        break
    i+=1




def get_count(list_of_polyhedrons):
    result = 0
    for polyhedron in list_of_polyhedrons:
        result = result + int(data_dict.get(polyhedron))
    return result


print(get_count(list_of_polyhedrons))




    



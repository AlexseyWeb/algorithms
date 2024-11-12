class Vector:
    def add_vectors(self, v1, v2):
        return (v1[0] + v2[0], v1[1] + v2[1])

first_vector = (3, 4)
second_vector = (-1, 2)

vec = Vector()
print(vec.add_vectors(first_vector, second_vector))    



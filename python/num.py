import numpy as np

#0 
array = np.array([1, 2, 3, 4, 5])
print(array)
array *= 2
print(array)


#1
array1 = np.array([[['A' , 'B' , 'C' ] ,['D' , 'E' , 'F' ] ,['G' , 'H' , 'I' ] ] ,
                  [['J' , 'K' , 'L' ] ,['M' , 'N' , 'O' ] ,['P' , 'Q' , 'R' ]] ,
                  [['S' , 'T' , 'U' ] ,['V' , 'W' , 'X' ] ,['Y' , 'Z' , ' ' ]]] ,)
print(array1.size) , print(array1.shape) , print(array1.ndim) , print(array1 [0][0][0]) #output A 
print(array1 [0 , 0 , 1]) #output B

#2
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9] , [10, 11, 12]]) #array[start:stop:step]
print(array2[0]) ,print(array2[1:4])  , print(array2[::2])  , print(array2[-1])

#3
array3 = np.array([1, 2, 3])
print(array3 + 1) , print(array3 * 2) , print(array3 - 1) , print(array3 // 2) , print(array3 ** 2) , print(np.sqrt(array3)) , print(np.exp(array3)) 

#4
array4 = np.array([1,2,3])
array5 = np.array([4,5,6])
print(array4 + array5) , print(array4 * array5) , print(array4 - array5) , print(array4 // array5) , print(array4 ** array5), print(np.sqrt(array4) + np.sqrt(array5)) , print (array4+array5 >= 10)

#5
array6 = np.array([[1, 2, 3 , 4] ])
array7 = np.array([[1],[2],[3],[4] ])
print(array6.shape) , print(array7.shape)
print(array6 * array7)

#6
ages = np.array([[22, 19, 24, 25, 26, 24, 25, 21],
                 [55 , 58, 60, 61, 62, 63, 64, 65]])
teen = ages[ages <= 22] 
adult = ages[ages > 22]
print(teen) , print(adult)


#7
rng = np.random.default_rng()
print(rng.integers(low=1, high=100, size=(3,2)))
fruits = np.array(["🍌" , "🍉" ,"🍓" ,"🥥" , "🥑"])
fruits = rng.choice(fruits , size=(3,3))
print(fruits)
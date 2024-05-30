def twoSum(target, *args):
    liste = list()
    for arg in args:
        liste.append(arg)

    for i in range(len(liste)):
        j = len(liste) -1
        while j > i:
            if liste[i]+liste[j] == target:
                print([liste[i],liste[j]])
            j -= 1

twoSum(9,2,7,3,6,2,4,1,5)

#   It is not like leetcode style but this is my solution. 



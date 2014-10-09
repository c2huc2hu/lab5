#question 1: part 1

def sort_a(list):
    if list  == (sorted(list)):
        return True
    else:
        return False

def sort_b(list):
    list1 = list[:]
    list1.sort()
    if list == list1:
        return True
    else:
        return False

#question 1: part 2
def sort_for(list):
    for i in range (len(list)):
        if list[i] == min(list):
            list.remove(list[i])
            return True
        else:
            return False

#question 2: part a

pets = [["Shoji", "cat", 18], ["Hanako", "dog", 15], ["Sir Toby", "cat", 10],
["Sachiko", "cat", 7], ["Sasha", "dog", 3], ["Lopez", "dog", 13]]

def separate(pets):
    for i in range(len(pets)):
        print(pets[i])

#question 2: part b

def second_element(pets):
    for i in range(len(pets)):
        print(pets[i][1])


#question 2: part c
def ages(pets):
    a = 0
    for i in range(len(pets)):
        a += pets[i][2]
    return a

#question 2: part d
def dogs(pets):
    count = 0
    i = 0
    while i < len(pets):     
        if pets[i][1] == "dog":
            count += 1
            i += 1
        else:
            i += 1
    return count

great = [[1,3,5], [2,4,6], [3,6,9], [9,5,1]]

#question 3: BAD
def nested_lengths(L):
    a = []
    for i in range(len(L)):
        a += len[i]
        print (a)

if __name__ == '__main__':
    #question 1: part 1
    print(sort_a([1,2,3,4,5]))
    print(sort_a([6,5,4,3,2]))
    
    print(sort_b([1,2,3,4,5]))
    print(sort_b([6,5,4,3,2]))
    
    #question 1: part 2
    print(sort_for([1,2,3,4,5]))
    print(sort_for([6,5,4,3,2]))
    
    #question 2: part a
    separate(pets)
    
    #question 2: part b
    second_element(pets)
    
    #question 2: part c
    print(ages(pets))
    
    #question 2: part d
    print(dogs(pets))
    
    #question 3:
    print(nested_lengths(great))

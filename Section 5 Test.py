#Question 1
print("Question 1:")
st = "Print only the words that start with s in this sentence"
st = st.split()

for word in st:
    if word[0].lower() == 's':
        print(word)
print("\n")

#Question 2
print("Question 2:")
even_numbers = [x for x in range(0,11) if x%2 == 0]
print(even_numbers)
print("\n")

#Question 3
print("Question 3:")
div_by_3 = [x for x in range(1,51) if x%3 == 0]
print(div_by_3)
print("\n")

#Question 4
print("Question 4:")
st = "Print every word in this sentence that has an even number of letters"
st = st.split()
new_st = [index +" is even!" for index in st if len(index)%2 == 0]
print(new_st)
print("\n")

#Question 5
print("Question 5:")
integers = list(range(1,101))
answer = []
for num in integers:
    if num%3 == 0 and num%5 == 0:
        answer.append("FizzBuzz")
    elif num%5 == 0:
        answer.append("Buzz")
    elif num%3 == 0:
        answer.append("Fizz")
    else: answer.append(num)
print(answer)
print("\n")

#Question 6
print("Question 6:")
st = "Create a list of the first letters of every word in this string"
st = st.split()
st = [letter[0] for letter in st]
print(st)
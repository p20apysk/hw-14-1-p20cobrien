# CTO 3/16/20
# Question 1
library = {"Harry Potter": "J.K. Rowling", "The Lord of the Rings": "J.R.R Tolkien", "The Hunger Games": "Suzanne Collins", "The Chronicles of Narnia": "C.S. Lewis"}

# Question 2
print(library["Harry Potter"],library["The Lord of the Rings"], library["The Hunger Games"], library["The Chronicles of Narnia"])

# Question 3
[print(key)for key, value in library.items()]
# Question 4
print("Harry Potter" in library)

# Question 5
print("Star Wars" not in library)

# Question 6
library["Unwanteds"] = "Lisa McMann"

# Question 7
print(len(library))

# Question 8
print(library["The Chronicles of Narnia"])

# Question 9
print(library)

# Question 10
del library["The Chronicles of Narnia"]
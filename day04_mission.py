#7.9
surprise = ["Groucho", "Chico", "Harpo"]
surprise[2] = surprise[2].lower()
surprise_string = ''.join(surprise[2])
surprise_string = surprise_string[::-1]
surprise_string = surprise_string.capitalize()
surprise[2] = surprise_string
print(surprise)










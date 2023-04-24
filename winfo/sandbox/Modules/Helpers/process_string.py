def process_string(string):
  string_thing = str(string)
  print(string_thing)
  print("Length: ")
  print(len(string_thing))
  print("First character: ")
  print(string_thing[0])
  print("Last character: ")
  print(string_thing[-1])
  print("First 3 characters: ")
  print(string_thing[0:3])
  print("Last 3 characters: ")
  print(string_thing[-3:])
  print("Every other character: ")
  print(string_thing[::2])
  print("Every other character, starting at the second character: ")
  print(string_thing[1::2])
  print("Capitalized: ")
  print(string_thing.capitalize())
  print("Lowercase: ")
  print(string_thing.lower())
  print("Uppercase: ")
  print(string_thing.upper())
  print("Titlecase: ")
  print(string_thing.title())
  print("Reversed: ")
  print(string_thing[::-1])
  print("Reversed, starting at the second character: ")
  print(string_thing[-1:0:-1])
  print("Reversed, starting at the second character, every other character: ")
  print(string_thing[-1:0:-2])
  print("camelCase: ")
  print(string_thing.title().replace(" ", ""))
  print("snake_case: ")
  print(string_thing.lower().replace(" ", "_"))
  print("kebab-case: ")
  print(string_thing.lower().replace(" ", "-"))
  print("Pig Latin: ")
  print(string_thing[1:] + string_thing[0] + "ay")
  print("Casefold: ")
  print(string_thing.casefold())
  print("Centered: ")
  print(string_thing.center(20))
  print("Centered, with a *: ")
  print(string_thing.center(20, "*"))
  print("Counting the number of e's: ")
  print(string_thing.count("e"))
  print("Finding the first e: ")
  print(string_thing.find("e"))
  print("Finding the last e: ")
  print(string_thing.rfind("e"))
  print("Replacing all e's with a *: ")
  print(string_thing.replace("e", "*"))
  print("Replacing all e's with a * and counting the number of replacements: ")
  print(string_thing.replace("e", "*", 1))
  print("Encoding: ")
  print(string_thing.encode())
  print("Checking if the string ends with 'ing': ")
  print(string_thing.endswith("ing"))
  print("Joining the string with a *: ")
  print("*".join(string_thing))
  print("Checking if the string is alphanumeric: ")
  print(string_thing.isalnum())
  print("Formatting: ")
  print("Hello, my name is {0}.".format(string_thing))
  print("Splitting the string into a list: ")
  print(string_thing.split())
  print("Verifying that the string is a string: ")
  print(string_thing.isalpha())
  print("Checking if the string is a digit: ")
  print(string_thing.isdigit())
  print("Checking if the string is a decimal: ")
  print(string_thing.isdecimal())
  print("Using the isidentifier() method: ")
  print(string_thing.isidentifier())
  print("Using the islower() method: ")
  print(string_thing.islower())
  print("Using the isnumeric() method: ")
  print(string_thing.isnumeric())
  print("Using the isprintable() method: ")
  print(string_thing.isprintable())
  print("Using the isspace() method: ")
  print(string_thing.isspace())
  print("Using the istitle() method: ")
  print(string_thing.istitle())
  print("Using the isupper() method: ")
  print(string_thing.isupper())
  print("Adding an exclamation point: ")
  string_thing = string_thing + "!"
  print("Final string_thing: ")
  print(string_thing)
  return string_thing
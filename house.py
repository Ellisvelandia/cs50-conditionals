name = input("whats your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermaine":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffinfor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
  case "Harry" | "Hermione" | "Ron":
    print("Gryffindor")
  # case "hermione":
  #     print("Gryffindor")
  # case "Ron":
  #     print("Gryffindor")
  case "Draco":
    print("Slytherin")
  case _:
    print("Who?")  
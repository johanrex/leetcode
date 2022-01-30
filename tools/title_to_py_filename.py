import sys

title = sys.argv[1]
filename = "p" + title.replace(" ", "_").replace(".", "").lower() + ".py"

print(filename)

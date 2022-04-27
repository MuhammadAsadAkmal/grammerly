# **********Group members *********
# Shoaib ur rehman
# summiya nawaz
# bilal ahmed
# *******************************

import language_tool_python

tool = language_tool_python.LanguageTool("en-US")


data = input("Enter text: ")
matches = tool.check(data)

for i in range(len(matches)):
    print("****************************")
    print("Mistake no " + str(i + 1))
    print("****************************")
    print(matches[i])
print("****************************")
print("Correct Sentence")
print(tool.correct(data))
print("****************************")

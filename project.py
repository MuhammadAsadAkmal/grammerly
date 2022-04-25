import language_tool_python

# import pandas as pd

tool = language_tool_python.LanguageTool("en-US")


with open("sample-2mb-text-file.txt", "r") as f:
    data = f.readlines()
matches = tool.correct(data)


print(matches)

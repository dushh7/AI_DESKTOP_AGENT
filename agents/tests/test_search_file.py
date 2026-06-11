from tools.search_file import search_file

results = search_file(
    "D:\\",
    "notes"
)

for item in results:
    print(item)
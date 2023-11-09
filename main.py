from wwr import extract_wwr_jobs

keyword = input("what do you want to search for?")

wwrs = extract_wwr_jobs(keyword)

print(wwrs)

file_path = r"C:\Users\seonhong.jang\Desktop\개인폴더\extractors\python.csv"

file = open(file_path, "w")

file.write("Position,Company,Location,URL\n")

for wwr in wwrs:
    file.write(f"{wwr['position']},{wwr['company']},{wwr['region']},{wwr['link']}\n")

file.close()


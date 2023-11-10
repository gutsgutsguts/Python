def save_to_file(wwrs):
    file_path = r"C:\Users\seonhong.jang\Desktop\개인폴더\extractors\python.csv"

    file = open(file_path, "w")

    file.write("Position,Company,Location,URL\n")

    for wwr in wwrs:
        file.write(f"{wwr['position']},{wwr['company']},{wwr['region']},{wwr['link']}\n")

    file.close()
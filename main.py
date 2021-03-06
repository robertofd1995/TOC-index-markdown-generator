import os
import codecs

name_of_file = "index.md"
route = r'C:\Users\rober\Documents\Github\My_Voto_Documentation'
deepLevel = 1


def create_element_list(file_name):
    myFile.write("* [" + file_name.replace(".md", "") + "]" + "(/" + file_name + ")\n")


def create_header_list(route, deep_level):
    str = "#" * deep_level + route + "\n"
    myFile.write(str)


def write_files_in_directory(list_of_files):
    for file in list_of_files:
        if file.endswith(".md"):
            create_element_list(file)
            print(file)


def write_index_of_directory(route, deep_level):
    if deep_level == 1:
        myFife = codecs.open(name_of_file, "a", "utf-8-sig")

        # Si ya existe un fichero TOC lo eliminamos
        if os.stat(name_of_file).st_size != 0:
            os.remove(name_of_file)

    if deep_level != 1:
        # Vamos a la ruta de donde queremos generar el indice
        os.chdir(route)

    deep_level_now = deep_level

    myFile.write("\n")
    create_header_list(os.path.relpath(".", ".."), deep_level)

    listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]

    # Explora por archivos

    if listOfFiles:
        print(" \nfiles : ")
        write_files_in_directory(listOfFiles)

    listOfDirs = [f for f in os.listdir() if (os.path.isdir(f) and not f == ".git")]

    if listOfDirs:
        # Explora por directorios y ir hacia ellos  y repetir
        print("\nDIRS : ")
        for dir in listOfDirs:

            route_directory = os.path.join(route, dir)

            if os.path.isdir(route_directory):
                deep_level_now += 1

                write_index_of_directory(route_directory, deep_level_now)

            deep_level_now -= 1


if __name__ == '__main__':
    os.chdir(route)
    myFile = codecs.open(name_of_file, "a", "utf-8-sig")

    write_index_of_directory(route, deepLevel)

    myFile.close()

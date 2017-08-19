
# For what is this program ?

This program will search for all the markdown files and subfolders in a folder and it will create an index


Example of directory :

    Book
    - README.md
        Chapter_1
        - part_1.md
        - part_1_2.md
        Chapter 2
        - part_2.md
            Chapter2_1
            - part2_2.md

OutPut :  (index.md)

    #Book
    * README.md
    ## Chapter_1
    * part_1.md
    * part_1_2.md
    ## Chapter_2
    * part_2.md
    ### Chapter2_1
    * part2_2.md


## How to use

To use just change the route to point to the directory on the script and execute the program

## Warning

All folders and files cannot contain white spaces , if so the index file will need to be fixed manually

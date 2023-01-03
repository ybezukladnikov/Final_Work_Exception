from pathlib import Path
import os


class ReadWriteFile:

    # def check_file(self, surname):
    #
    #     path = Path("repository")
    #
    #     for filename in os.listdir(path):
    #         print(filename[:-4])
    #         if filename[:-4] == surname:
    #             return True
    #     return False


    def write_file(self, directory):
        name_file = directory['Surname']
        path_to_file = Path("repository",f"{name_file}.txt")
        try:
            with open(path_to_file, "a") as f:
                for value in directory.values():
                    f.write(f"<{value}>")
                f.write("\n")
        except FileNotFoundError:
            print('At the root of the project, create a directory named => repository')










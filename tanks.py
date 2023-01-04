from os import path
import model
import view














if __name__ == "__main__":
    map_folder = "maps"
    map_file_name = "map_1.txt"
    map_full_name = (path.join(map_folder, map_file_name))

    field = model.Field(map_full_name)
    print(field.field)

from pathlib import Path
import os

class Consts:
    datamaker_folder = "RomanDictionary/DataMaker/"
    data_folder = "RomanDictionary/Data/"
    slash = "/"

if os.name == "nt":
    Consts.slash = "\\"
else:
    Consts.slash = "/"

library_dir = str(Path(__file__).parent.parent.resolve()) + Consts.slash

Consts.datamaker_folder = library_dir + "DataMaker" + Consts.slash
Consts.data_folder = library_dir + "Data" + Consts.slash
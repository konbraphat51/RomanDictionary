from pathlib import Path

class Consts:
    datamaker_folder = "RomanDictionary/DataMaker/"
    data_folder = "RomanDictionary/Data/"

library_dir = Path(__file__).parent.parent
Consts.datamaker_folder = str(library_dir / "DataMaker/") + "\\"
Consts.data_folder = str(library_dir / "Data/") + "\\"
from pathlib import Path
from Detect import detect

DATA_TO_READ = "data"

if __name__ == "__main__":
    directory = DATA_TO_READ
    img_list = Path(directory).glob('*.jpg')

    images = []
    for img_path in img_list:
        print(f"{img_path} : {detect(str(img_path))}")


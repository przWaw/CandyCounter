from pathlib import Path

from Detect import detect

DIRECTORY = "data"


if __name__ == "__main__":
    directory = DIRECTORY
    img_list = Path(directory).glob('*.jpg')
    for img_path in img_list:
        print(f"{img_path} : {detect(str(img_path))}")

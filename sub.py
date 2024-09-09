from __future__ import annotations
import sys
from PIL import Image
from PIL.ImageChops import subtract
from PIL.Image import Image as ImgType


def main() -> int:
    args = sys.argv
    assert len(args) == 3
    image1: ImgType = Image.open(args[1])
    image2: ImgType = Image.open(args[2])
    print(f"subtracting Image:{image1} from {image2}")
    channel = input("Channel(r,g,b,a): ").upper()
    composit: ImgType = subtract(image1, image2, scale=(1/255), offset=128)
    if channel in "RGBA" and channel:
        composit = composit.getchannel(channel)
    else:
        print("Outputing All Channels")
    composit.save("out.png")
    print("saved to new image")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

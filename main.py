import os
import time
from typing import Generator

from PIL import Image


FPS = 30


def frames(path: str) -> Generator[Image.Image, None, None]:
    for filename in sorted(os.listdir(path)):
        yield Image.open(f"{path}/{filename}")


if __name__ == "__main__":
    start = time.time()

    for i, frame in enumerate(frames("frames"), start=1):
        output = ""
        for y in range(frame.height):
            for x in range(frame.width):
                pixel = frame.getpixel((x, y))
                if sum(pixel) >= 510:
                    output += "# "
                elif sum(pixel) >= 255:
                    output += "* "
                else:
                    output += "  "
            output += "\n"
        frame.close()
        print(output)

        # Account for the time it took to display the frame
        delta = (i * 1 / FPS) - (time.time() - start)
        time.sleep(abs((1 / FPS) + delta))

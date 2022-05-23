import numpy as np
import PIL.Image
import io

def get_resized_chessboard_from_buffer(buffer):
    img_data = PIL.Image.open(io.BytesIO(buffer.read())).convert('RGB')
    return img_data.resize([256, 256], PIL.Image.BILINEAR)

def get_chessboard_tiles_from_buffer(file):
    img_data = get_resized_chessboard_from_buffer(file)
    img_data = img_data.convert('L', (0.2989, 0.5870, 0.1140, 0))
    chessboard_256x256_img = np.asarray(img_data, dtype=np.uint8)
    # 64 tiles in order from top-left to bottom-right (A8, B8, ..., G1, H1)
    tiles = [None] * 64
    for rank in range(8): # rows/ranks (numbers)
        for file in range(8): # columns/files (letters)
            sq_i = rank * 8 + file
            tile = np.zeros([32, 32, 3], dtype=np.uint8)
            for i in range(32):
                for j in range(32):
                    tile[i, j] = chessboard_256x256_img[
                        rank*32 + i,
                        file*32 + j,
                    ]
            tiles[sq_i] = PIL.Image.fromarray(tile, 'RGB')
    return tiles
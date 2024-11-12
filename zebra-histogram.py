import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# デスクトップ上の指定されたTIFFファイルを読み込み
file_path = 'XX:¥¥YYYY¥¥ZZZZ¥¥FILENAME'
# Input your folder including image sequence

img = Image.open(file_path)

# 画像をnumpy配列に変換
img_array = np.array(img)

# 赤と緑のチャンネルを分離
red_channel = img_array[:, :, 0]
green_channel = img_array[:, :, 1]

# 各X位置に対してY軸方向の輝度の総和を計算
red_intensity_sum = np.sum(red_channel, axis=0)
green_intensity_sum = np.sum(green_channel, axis=0)

# 各チャンネルの最小値を基準にして相対的な輝度を計算
red_relative_intensity = red_intensity_sum - np.min(red_intensity_sum)
green_relative_intensity = green_intensity_sum - np.min(green_intensity_sum)

# 結果をプロット
plt.figure(figsize=(10, 6))
plt.plot(red_relative_intensity, color='red', label='Red Channel', linestyle='-', marker='o', markersize=0)
plt.plot(green_relative_intensity, color='green', label='Green Channel', linestyle='-', marker='o', markersize=0)
plt.xlabel('X-axis')
plt.ylabel('Relative Sum of Intensities along Y-axis')
plt.title('Relative Sum of Red and Green Intensities along Y-axis (by X position)')
plt.legend()
plt.show()

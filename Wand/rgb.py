import plotly.express as px
import numpy as np

r = 255
g = 255
b = 222


def show():
    img_rgb = np.array([[[r, g, b], [r, g, b], [r, g, b]],
                        [[r, g, b], [r, g, b], [r, g, b]]], dtype=np.uint8)
    fig = px.imshow(img_rgb)
    fig.show()
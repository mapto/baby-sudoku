#!/usr/bin/env python3

from sudoku import Sudoku
import gradio as gr
from datetime import datetime

css = """
footer {
    visibility: hidden;
}
"""

html_templ = "<table>{contents}</table>"
row_templ = "<tr><td>{contents}</td></tr>"

def baby_sudoku(size: int = 2, diff: float = 0.5) -> list[list[str]]:
    mstart = ord('\U0001F346')
    map = {i: f"{chr(mstart + i)}" for i in range(1,size**2+1)}
    map[None] = "&nbsp;"
    s = Sudoku(size, seed=datetime.now().timestamp()).difficulty(diff)
    pictures = [[map[e] for e in row] for row in s.board]
    rows = [row_templ.format(contents="</td><td>".join(row)) for row in pictures]
    return html_templ.format(contents="</tr><tr>".join(rows))

with gr.Blocks(css=css) as demo:
    fn=baby_sudoku,
    with gr.Row():
        size = gr.Slider(value=2, label="Size", step=1, minimum=2, maximum=4)
        diff = gr.Slider(value=0.5, label="Difficulty", step=.1, minimum=.1, maximum=.9)
    result = gr.HTML(label="Results")
    # head=html_head,

    params = {
        "fn": baby_sudoku,
        "inputs": [size,diff],
        "outputs": [result],
    }
    demo.load(**params)
    size.change(**params)
    diff.change(**params)

demo.launch(server_port=7861, server_name="0.0.0.0", show_api=False)

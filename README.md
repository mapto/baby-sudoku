# baby-sudoku
A Sudoku with images, meant for children of pre-school age

This is a very simple application that generates sudoku games, using [py-sudoku](https://pypi.org/project/py-sudoku) and [gradio](https://www.gradio.app).

[baby-sudoku.ipynb](./baby-sudoku.ipynb) and [app.py](./app.py) are basically the same code, that could be run in different ways. The remaining files serve the possibility to run this as a standalone web server. To run the server, install [docker compose](https://docs.docker.com/compose/) and run:

    docker compose up

Then open your browser at http://localhost:8781
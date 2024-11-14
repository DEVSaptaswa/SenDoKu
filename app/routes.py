from flask import render_template, request, redirect, url_for, jsonify
from app import app
from solver import solve
from grids import generate_sudoku
import copy

grid = []
@app.route("/")
def index():
    return render_template('home.html')

@app.route("/play")
def board_solve():
    unsolved_board=generate_sudoku()
    board=copy.deepcopy(unsolved_board)
    solve(board)
    L=[]
    for i in range(len(unsolved_board)):
        for j in range(len(unsolved_board[i])):
            if unsolved_board[i][j] == 0:
                L.append(board[i][j])
    print(L)
    return render_template('game.html', grid=unsolved_board, answer=L, solvedGrid=board)

@app.route("/solve")
def get_board():
    L=[]
    for _ in range(9):
        l=[]
        for _ in range(9):
            l.append(0)
        L.append(l)
    print(L)
    return render_template('sudoku.html', grid=L)

@app.route('/process_data', methods=['POST', 'GET'])
def process_data():
    data = request.get_json()

    cell_values = data['cellValues']

    grid = []
    for i in range(0, 81, 9):
        row = cell_values[i:i+9]
        grid.append(row)
    solve(grid)
    print(grid)

    return jsonify({'result': grid})
from eightQueens import EightQueens
from board import Board


def main(size):
    b = Board(size)
    x = EightQueens(b)

    [print(i) for i in x.outputs]

    print("-----------------------------")
    print("Number of iterations: " + str(len(x.outputs)))
    print("Final board: ")
    print(x.outputs[-1])


if __name__ == "__main__":
    size = int(input("Enter the size of the board: "))
    main(size)

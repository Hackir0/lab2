def create_chessboard(n, m):
    chessboard = []

    try:
        for i in range(n):
            row = []
            for j in range(m):

                if (i + j) % 2 == 0:
                    row.append(".")
                else:
                    row.append("*")
            chessboard.append(row)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        return chessboard


try:
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
except ValueError:
    print("Ошибка ввода: введите целые числа.")
else:
    chessboard = create_chessboard(n, m)

for row in chessboard:
    print(" ".join(row))
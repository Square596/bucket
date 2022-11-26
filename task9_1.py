from numpy import mean, var


def analysis_coroutine():
    data = []
    while True:
        current_input = yield
        try:
            data.append(float(current_input))
        except ValueError:
            if current_input == 'mean':
                print(mean(data))
            elif current_input == 'var':
                print(var(data))
            elif current_input == 'exit':
                exit()

            else:
                raise ValueError("Incorrect input! It should be int, float or 'mean' or 'var'")


if __name__ == '__main__':
    cor = analysis_coroutine()
    next(cor)
    while True:
        cor.send(input())

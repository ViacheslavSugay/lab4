from src.simulation import run_simulation


def main():
    while True:
        user_input = input("Введите seed, 'exit' или нажмите Enter для случайной симуляции: ").strip()

        if user_input.lower() == "exit":
            print("Симуляция завершена")
            break
        elif user_input == "":
            run_simulation()
        else:
            try:
                seed = int(user_input)
                run_simulation(seed=seed)
            except ValueError:
                print("Ошибка: введите число, 'exit' или нажмите Enter")


if __name__ == "__main__":
    main()
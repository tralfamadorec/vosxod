from statemachine import StateMachine, State

class FullProgramFSM(StateMachine):
    """
    полный конечный автомат всей консольной программы.
    состояния:
    - Главное меню
    - Подменю каждого задания
    - Действия внутри заданий
    - Выход
    """
    # главное меню
    main_menu = State(initial=True)

    # состояния задания1
    task1_menu = State()
    task1_input_manual = State()
    task1_input_random = State()
    task1_execute = State()
    task1_show_result = State()

    # состояния задания5
    task5_menu = State()
    task5_input_manual = State()
    task5_input_random = State()
    task5_execute = State()
    task5_show_result = State()

    # состояния задания8
    task8_menu = State()
    task8_input_manual = State()
    task8_input_random = State()
    task8_execute = State()
    task8_show_result = State()

    # конечное состояние
    exit_state = State(final=True)

    # переходы из главного меню
    to_task1 = main_menu.to(task1_menu)
    to_task5 = main_menu.to(task5_menu)
    to_task8 = main_menu.to(task8_menu)
    to_exit = main_menu.to(exit_state)

    # задание1: переходы
    t1_to_input_manual = task1_menu.to(task1_input_manual)
    t1_to_input_random = task1_menu.to(task1_input_random)
    t1_to_execute = task1_menu.to(task1_execute)
    t1_to_show_result = task1_menu.to(task1_show_result)
    t1_back = task1_menu.to(main_menu)

    # возврат из действий в меню задания 1
    t1_input_manual_done = task1_input_manual.to(task1_menu)
    t1_input_random_done = task1_input_random.to(task1_menu)
    t1_execute_done = task1_execute.to(task1_menu)
    t1_show_result_done = task1_show_result.to(task1_menu)

    # задание5: переходы
    t5_to_input_manual = task5_menu.to(task5_input_manual)
    t5_to_input_random = task5_menu.to(task5_input_random)
    t5_to_execute = task5_menu.to(task5_execute)
    t5_to_show_result = task5_menu.to(task5_show_result)
    t5_back = task5_menu.to(main_menu)

    t5_input_manual_done = task5_input_manual.to(task5_menu)
    t5_input_random_done = task5_input_random.to(task5_menu)
    t5_execute_done = task5_execute.to(task5_menu)
    t5_show_result_done = task5_show_result.to(task5_menu)

    # задание8: переходы
    t8_to_input_manual = task8_menu.to(task8_input_manual)
    t8_to_input_random = task8_menu.to(task8_input_random)
    t8_to_execute = task8_menu.to(task8_execute)
    t8_to_show_result = task8_menu.to(task8_show_result)
    t8_back = task8_menu.to(main_menu)

    t8_input_manual_done = task8_input_manual.to(task8_menu)
    t8_input_random_done = task8_input_random.to(task8_menu)
    t8_execute_done = task8_execute.to(task8_menu)
    t8_show_result_done = task8_show_result.to(task8_menu)
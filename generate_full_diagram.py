from fsm_full import FullProgramFSM
from statemachine.contrib.diagram import DotGraphMachine

if __name__ == "__main__":
    fsm = FullProgramFSM()
    graph = DotGraphMachine(fsm)
    graph().write_png("../full_fsm_diagram.png")
    print("✅ Полная схема FSM сохранена как full_fsm_diagram.png в корне репозитория")
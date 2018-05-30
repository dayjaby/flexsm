import time
from flexsm import StateMachine, State, Transition, addTransition

root = State("root")
state2 = State("state 2")
state1 = State("state 1")

@addTransition(state=root)
class WaitForXToBecomeSmall(Transition):
    def getNextState(self, x):
        if x>15:
            return root
        else:
            return state1

@addTransition(state=state1, next=state2)
class Wait1Dot5Seconds(Transition):
    def check(self, time_in_state, x):
        return time_in_state > 1.5 and x == 14

    def onTrigger(self, time_in_state, x):
        print("We are in this boring state since {:.2f} seconds".format(time_in_state))

sm = StateMachine(root)
sm.update("y", 17)
print("Changed y to 17, current state={}".format(sm.current_state))
sm.update("x", 19)
print("Changed x to 19, current state={}".format(sm.current_state))
sm.update("x", 15)
print("Changed x to 15, current state={}".format(sm.current_state))
sm.update("x", 14)
print("Changed x to 14, current state={}".format(sm.current_state))
for i in range(20):
    time.sleep(0.1)
print("I slept two seconds, current state={}".format(sm.current_state))


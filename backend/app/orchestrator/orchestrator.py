from app.orchestrator.executor import Executor
from app.orchestrator.intent_parser import IntentParser
from app.orchestrator.planner import Planner


class Agent:

    def __init__(self):

        self.parser = IntentParser()

        self.planner = Planner()

        self.executor = Executor()

    def run(self, message: str):

        intent = self.parser.parse(message)

        plan = self.planner.create_plan(intent)

        result = self.executor.execute(plan)

        return result
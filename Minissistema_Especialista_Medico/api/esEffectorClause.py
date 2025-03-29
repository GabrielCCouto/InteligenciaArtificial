from api.esClause import Clause

class EffectorClause(Clause):
    truth = True
    consequent = True
    object = None

    def __init__(self, e_name, args):
        self.ruleRefs = []
        self.effectorName = e_name
        self.arguments = args

    def display(self):
        return "effector(" + self.effectorName + "," + self.arguments + ") "

    def perform(self, rb):
        self.object = rb.get_effector_object(self.effectorName)
        self.object.effector(self, self.effectorName, self.arguments)
        return self.truth

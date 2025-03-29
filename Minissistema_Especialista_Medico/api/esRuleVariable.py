from api.esVariable import Variable

class RuleVariable(Variable):
    promptText = 'used to prompt user for value'
    ruleName = ''
    value = None

    def __init__(self, rb, name):
        super().__init__(name)
        self.rb = rb
        self.rb.add_variable(self)
        self.clauseRefs = []

    def set_value(self, value):
        self.value = value
        self.update_clauses()

    def ask_user(self):
        print("Ask User for Value")
        print(self.promptText)
        answer = input()
        self.set_value(answer)
        return self.value

    def add_clause_ref(self, ref):
        self.clauseRefs.append(ref)

    def update_clauses(self):
        for clause in self.clauseRefs:
            clause.check()

    def set_rule_name(self, rule_name):
        self.ruleName = rule_name

    def set_prompt_text(self, prompt_text):
        self.promptText = prompt_text

    def get_prompt_text(self):
        return self.promptText

    def compute_statistics(self, in_value):
        return in_value

    def normalize(self, in_value, out_array, inx):
        return inx

class Clause:
    def __init__(self, lhs, cond, rhs):
        self.lhs = lhs
        self.cond = cond
        self.rhs = rhs
        self.lhs.add_clause_ref(self)
        self.rule_refs = []
        self.truth = None
        self.consequent = False

    def __str__(self):
        return self.lhs.name + ' ' + self.cond.__str__() + ' ' + self.rhs + " "

    def add_rule_ref(self, ref):
        self.rule_refs.append(ref)

    def check(self):
        if self.consequent:
            self.truth = None
            return self.truth
        if self.lhs.value is None:
            self.truth = None
            return self.truth
        else:
            both_numeric = True
            lhs_numeric_value = None
            rhs_numeric_value = None
            try:
                lhs_numeric_value = float(self.lhs.value)
                rhs_numeric_value = float(self.rhs)
            except Exception as e:
                both_numeric = False
            if self.cond.index == 1:
                if both_numeric:
                    self.truth = lhs_numeric_value == rhs_numeric_value
                else:
                    self.truth = self.lhs.value.lower() == self.rhs.lower()
            elif self.cond.index == 2:
                if both_numeric:
                    self.truth = lhs_numeric_value > rhs_numeric_value
                else:
                    self.truth = self.lhs.value.lower() > self.rhs.lower()
            elif self.cond.index == 3:
                if both_numeric:
                    self.truth = lhs_numeric_value < rhs_numeric_value
                else:
                    self.truth = self.lhs.value.lower() < self.rhs.lower()
            elif self.cond.index == 4:
                if both_numeric:
                    self.truth = lhs_numeric_value != rhs_numeric_value
                else:
                    self.truth = self.lhs.value.lower() != self.rhs.lower()
            return self.truth

    def set_consequent(self):
        self.consequent = True

    def get_rule(self):
        if self.consequent:
            return self.rule_refs[0]
        else:
            return None

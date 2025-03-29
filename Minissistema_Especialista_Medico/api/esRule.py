from api.esClause import Clause


class Rule:
    fired = False

    def __init__(self, rb, name, lhs, rhs):
        if isinstance(lhs, Clause):
            self.rb = rb
            self.name = name
            self.antecedents = [None]
            self.antecedents[0] = lhs
            lhs.add_rule_ref(self)
            self.consequent = rhs
            rhs.add_rule_ref(self)
            rhs.set_consequent()
            rb.rule_list.append(self)
            self.truth = None
        else:
            self.__init__0(rb, name, lhs, rhs)

    def __init__0(self, rb, name, lhs_clauses, rhs):
        self.rb = rb
        self.name = name
        self.antecedents = []
        for x in range(len(lhs_clauses)):
            self.antecedents.append(None)

        i = 0
        while i < len(lhs_clauses):
            self.antecedents[i] = lhs_clauses[i]
            self.antecedents[i].add_rule_ref(self)
            i += 1
        self.consequent = rhs
        rhs.add_rule_ref(self)
        rhs.set_consequent()
        rb.rule_list.append(self)
        self.truth = None

    def num_antecedents(self):
        return len(self.antecedents)

    @staticmethod
    def check_rules(clause_refs):
        for clause in clause_refs:
            for rule in clause.rule_refs:
                rule.check()

    def check(self):
        self.rb.trace("\nTesting rule " + self.name)
        for i in range(len(self.antecedents)):
            if self.antecedents[i].truth is None:
                self.truth = None
                return self.truth
            if self.antecedents[i].truth:
                continue
            else:
                self.truth = False
                return self.truth
        self.truth = True
        return self.truth

    def fire(self):
        self.rb.trace("\nFiring rule " + self.name)
        self.truth = True
        self.fired = True
        if self.consequent.lhs is None:
            self.consequent.perform(self.rb)
        else:
            self.consequent.lhs.set_value(self.consequent.rhs)
            self.check_rules(self.consequent.lhs.clauseRefs)

    def back_chain(self):
        self.rb.trace("Evaluating rule " + self.name)
        print("\nEvaluating rule " + self.name)
        for i in range(len(self.antecedents)):
            if self.antecedents[i].truth is None:
                self.rb.backward_chain(self.antecedents[i].lhs.name)
            if self.antecedents[i].truth is None:
                self.antecedents[i].lhs.ask_user()
                self.truth = self.antecedents[i].check()
            if self.antecedents[i].truth:
                continue
            else:
                self.truth = False
                return self.truth
        self.truth = True
        return self.truth

    def display(self, log):
        log.append('\nRule-' + self.name + ":")
        i = 0
        first_time = True
        while i < len(self.antecedents):
            if first_time:
                aux = 'IF '
                first_time = False
            else:
                aux = ''
            next_clause = self.antecedents[i]
            if (i + 1) < len(self.antecedents):
                log.append(aux + ' ' + next_clause.__str__() + " AND")
            else:
                log.append(aux + ' ' + next_clause.__str__())
            i += 1
        log.append("THEN " + self.consequent.__str__())

    def reset(self):
        self.fired = False

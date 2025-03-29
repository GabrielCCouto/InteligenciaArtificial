from api.esRuleBase import RuleBase

class BooleanRuleBase(RuleBase):
    name = ''
    variable_list = {}
    clause_var_list = []
    rule_list = []
    conclusion_var_list = []
    rule_ptr = None
    clause_ptr = None
    goal_clause_stack = []
    effectors = {}
    sensors = {}
    factList = []
    log = []

    def set_display(self, text):
        self.log = text

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def trace(self, text):
        if self.log is not None:
            self.log.append(text)

    def display_variables(self, text):
        for k, v in self.variable_list.items():
            text.append(v.name + " value = " + str(v.value))
        text.append("--------------------------------------")

    def display_rules(self, text):
        text.append("\n" + self.name + " Rule Base: " + "\n")
        for temp in self.rule_list:
            temp.display(text)
        if self.factList is not None:
            for temp in self.factList:
                temp.display(text)

    def display_conflict_set(self, rule_set):
        self.trace("\n" + " -- Rules in conflict set:\n")
        for temp in rule_set:
            self.trace(temp.name + "(" + str(temp.num_antecedents()) + "), ")

    def reset(self):
        self.trace(
            "\n --- Setting all " + str(self.name) + " variables to null")
        for k, v in self.variable_list.items():
            v.set_value(None)
        if self.factList is not None:
            for temp in self.factList:
                temp.fired = False
        for temp in self.rule_list:
            temp.reset()

    def backward_chain(self, goal_var_name):
        goal_var = self.variable_list[goal_var_name]
        for goal_clause in goal_var.clauseRefs:
            if not goal_clause.consequent:
                continue
            self.goal_clause_stack.append(goal_clause)
            goal_rule = goal_clause.get_rule()
            rule_truth = goal_rule.back_chain()

            if rule_truth is None:
                self.trace("\nRule " + goal_rule.name +
                           " is null, can't determine truth value.")
            elif rule_truth:
                goal_var.set_value(goal_clause.rhs)
                goal_var.set_rule_name(goal_rule.name)
                self.goal_clause_stack.pop()
                self.trace("\nRule " + goal_rule.name + " is true, setting " +
                           goal_var.name + ": = " + str(goal_var.value))
                if len(self.goal_clause_stack) == 0:
                    self.trace(
                        "\n +++ Found Solution for goal: " + goal_var.name)
                    break
            else:
                self.goal_clause_stack.pop()
                self.trace("\nRule " + goal_rule.name +
                           " is false, can't set " + goal_var.name)
        if goal_var.value is None:
            self.trace("\n +++ Could Not Find Solution for goal: " +
                       goal_var.name)

    def match(self, test):
        match_list = []
        for test_rule in self.rule_list:
            if test:
                test_rule.check()
            if test_rule.truth is None:
                continue
            if test_rule.truth and not test_rule.fired:
                match_list.append(test_rule)
        self.display_conflict_set(match_list)
        return match_list

    @staticmethod
    def select_rule(rule_set):
        max2 = None
        first_time_only = True
        best_rule = None
        for next_rule in rule_set:
            if first_time_only:
                first_time_only = False
                best_rule = next_rule
                max2 = best_rule.num_antecedents()
            num_clauses = next_rule.num_antecedents()
            if num_clauses > max2:
                max2 = num_clauses
                best_rule = next_rule
        return best_rule

    def forward_chain(self):
        conflict_rule_set = self.match(True)
        while len(conflict_rule_set) > 0:
            selected = self.select_rule(
                conflict_rule_set)  # select the "best" rule
            selected.fire()
            conflict_rule_set = self.match(False)

    def add_effector(self, obj, effector_name):
        if self.effectors is None:
            self.effectors = {}
        self.effectors[effector_name] = obj

    def get_effector_object(self, effector_name):
        return self.effectors[effector_name]

    def add_sensor(self, obj, sensor_name):
        if self.sensors is None:
            self.sensors = {}
        self.sensors[sensor_name] = obj

    def get_sensor_object(self, sensor_name):
        return self.sensors[sensor_name]

    def initialize_facts(self):
        if self.factList is not None:
            for fact in self.factList:
                fact.asserts(self)

    def add_fact(self, fact):
        if self.factList is None:
            self.factList = []
        self.factList.append(fact)

    def add_variable(self, variable):
        self.variable_list[variable.get_name()] = variable

    def get_variables(self):
        return self.variable_list.copy()

    def get_goal_variables(self):
        goal_vars = []
        for k, v in self.variable_list.items():
            goal_clauses = v.clauseRefs
            if (goal_clauses is not None) and (len(goal_clauses) != 0):
                goal_vars.append(v)
        return goal_vars

    def get_variable(self, name):
        if name in self.variable_list:
            return self.variable_list[name]
        return None

    def set_variable_value(self, name, value):
        variable = self.get_variable(name)
        if variable is not None:
            variable.set_value(value)
        else:
            print("BooleanRuleBase: Can't set value, variable "
                  + name + " is not defined!")

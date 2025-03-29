class Fact:
    fired = False

    def __init__(self, rb, name, f):
        self.rb = rb
        self.name = name
        self.fact = f
        self.rb.add_fact(self)
        self.truth = None

    def asserts(self, rb):
        if self.fired:
            return
        rb.trace("\nAsserting fact " + self.name)
        self.truth = True
        self.fired = True
        if self.fact.lhs is None:
            self.fact.perform(rb)
        else:
            self.fact.lhs.set_value(self.fact.rhs)

    def display(self, log):
        log.append(self.name + ": ")
        log.append(self.fact.__str__() + "\n")

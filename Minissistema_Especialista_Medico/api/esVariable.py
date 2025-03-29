class Variable:
    labels = None
    column = -1

    def __init__(self, name):
        self.name = name
        self.value = None

    def get_name(self):
        return self.name

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_labels(self, new_labels):
        self.labels = []
        tok = new_labels.split(' ')
        for x in tok:
            self.labels.append(x)

    def get_label(self, index):
        return str(self.labels[index])

    def get_labels(self):
        return self.labels.copy()

    def get_labels_as_string(self):
        label_list = ''
        for x in self.labels:
            label_list += x + ' '
        return label_list

    def get_index(self, label):
        index = -1
        if self.labels is None:
            return index
        i = 0
        while i < len(self.labels):
            if label == self.labels[i]:
                index = i
                break
            i += 1
        return index

    def categorical(self):
        if self.labels is not None:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def to_string(self):
        return self.name

    def set_column(self, column):
        self.column = column

    def compute_statistics(self, in_value):
        pass

    def normalize(self, in_value, out_array, inx):
        pass

    @staticmethod
    def normalized_size():
        return 1

    @staticmethod
    def get_decoded_value(act, index):
        return str(act[index])

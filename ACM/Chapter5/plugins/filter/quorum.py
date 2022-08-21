def quorum(list_of_machines):

    n = len(list_of_machines)
    quorum = n / 2 + 1

    return quorum

class FilterModule(object):
    def filters(self):
        return {
            'quorum': quorum,
        }


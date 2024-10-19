class InMemoryToDoRepository:
    def __init__(self):
        self.todos = {}
        self.current_id = 0

    def next_id(self):
        self.current_id += 1
        return self.current_id

    def save(self, todo):
        self.todos[todo.id] = todo

    def get_all(self):
        return list(self.todos.values())

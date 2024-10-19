from todo import ToDo

class ToDoUseCase:
    def __init__(self, repository):
        self.repository = repository

    def add_todo(self, title):
        new_todo = ToDo(id=self.repository.next_id(), title=title)
        self.repository.save(new_todo)

    def get_todos(self):
        return self.repository.get_all()

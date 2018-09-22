class Task:

    templates = []

    def __init__(self, title: str):
        self.title = title
        self.description = ""
        self.due_date = ""
        self.start_date = ""
        self.visible = True
        self.labels = []
        self.task_list = TaskList(self.title)

    def save_template(self):
        templates.append(self)

    @classmethod
    def from_template(cls, index):
        if not templates:
            print("No templates saved.")
            return None
        else:
            return cls(templates[index].title)
    pass


class TaskList:

    templates = []

    def __init__(self, title: str):
        self.title = title
        self.tasks = []

    def add(self, title: str):
        self.tasks.append(Task(title))

    def remove(self, title: str):
        for element in self.tasks:
            if element.title == title:
                self.tasks.remove(element)
                break
        else:
            print("Task with title \"", title, "\" does not exist.")

    def save_template(self):
        templates.append(self)

    @classmethod
    def from_template(cls, index):
        if not templates:
            print("No saved templates.")
            return None
        else:
            return cls(templates[index].title)


if __name__ == "__main__":
    my_list = TaskList("my_list")
    my_list.add("Do the dishes")
    my_list.add("Walk the dog")
    my_list.remove("Do the dishes")
    my_list.remove("Feed the cat")
    my_list.remove("Walk the dog")
    my_list.remove("Feed the cat")

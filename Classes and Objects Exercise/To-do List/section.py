class Section:
    def __init__(self, name: str,):
        self.name = name
        self.tasks = []
        self.tasks_names = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        self.tasks_names.append(new_task.name)
        return f'Task Name: {new_task.name} - Due Date: {new_task.due_date} is added to the section'

    def complete_task(self, task_name):
        if task_name not in self.tasks_names:
            return f'Could not find task with the name {task_name}'
        search_index = self.tasks_names.index(task_name)
        current_task = self.tasks[search_index]
        current_task.completed = True
        self.tasks[search_index] = current_task
        return f'Completed task {task_name}'

    def clean_section(self):
        for index in range(len(self.tasks)):
            current_task = self.tasks[index]
            current_state = current_task.completed
            if current_state:
                self.tasks[index] = "-"
        number_of_removals = self.tasks.count("-")
        while "-" in self.tasks:
            search_index = self.tasks.index("-")
            self.tasks.pop(search_index)
            self.tasks_names.pop(search_index)
        return f'Cleared {number_of_removals} tasks.'

    def view_section(self):
        return_details = []
        for el in self.tasks:
            return_details.append(el.details())
        final_details = "\n".join(return_details)
        return f'Section {self.name}:\n{final_details}'

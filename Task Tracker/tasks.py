class Task:
    
    all_task = []
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.status = "Not Complete"
        Task.all_task.append(self)
        
    @classmethod
    def view_all_tasks(cls):
           return Task.all_task
    
    @classmethod         
    def complete_task(cls,title):
        for index, task in enumerate(cls.all_task, start=1):
            if task.status == 'Not Complete':
                if task.title == title:
                    task.status = 'Complete'
                    print("Completed")
                else:
                    print("No task with this name")
            else:
                print("Task already completed")
    @classmethod
    def remove_completed(cls):
        for task in cls.all_task:
            if task.status == "Complete":
                cls.all_task.remove(task)
                print("Task removed")
            
    @classmethod
    def delete_task(cls,title):
        for task in cls.all_task:
            if task.title == title:
                cls.all_task.remove(task)
                print("Task removed")
        
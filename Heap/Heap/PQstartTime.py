class Task:
    def __init__(self, task_id, priority, execution_time, deadline):
        # Initialize task attributes
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.deadline = deadline

class MaxHeap:
    def __init__(self, tasks=[]):
        # Initialize max heap with tasks and build the heap
        self.data = tasks
        self._build_heap()
        self.time = 0
        self.start_time = None
        self.end_time = None
    
    def get_count(self):
        # Get the number of tasks in the heap
        return len(self.data)
    
    def _parent(self, idx):
        # Get the parent index of a given index
        return (idx - 1) // 2
    
    def _lchild(self, idx):
        # Get the left child index of a given index
        return 2 * idx + 1
    
    def _rchild(self, idx):
        # Get the right child index of a given index
        return 2 * idx + 2
    
    def _swap(self, i, j):
        # Swap elements at indices i and j
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def _build_heap(self):
        # Build the heap from the tasks
        length = len(self.data)
        start = (length - 2) // 2
        for idx in range(start, -1, -1):
            self._down_heap(idx, length)
    
    def _up_heap(self, j):
        # Perform up-heap operation
        parent = self._parent(j)
        if j > 0 and self.data[j].priority > self.data[parent].priority:
            self._swap(j, parent)
            self._up_heap(parent)

    def _down_heap(self, idx, length):
        # Perform down-heap operation
        if self._lchild(idx) < length:
            left = self._lchild(idx)
            big_child = left
            if self._rchild(idx) < length:
                right = self._rchild(idx)
                if self.data[right].priority > self.data[left].priority:
                    big_child = right
            if self.data[big_child].priority > self.data[idx].priority:
                self._swap(big_child, idx)
                self._down_heap(big_child, length)
    
    def add_task(self, task):
        # Add a task to the max heap and perform up-heap operation
        self.data.append(task)
        self._up_heap(len(self.data) - 1)
    
    def get_highest_priority_task(self):
        # Get the task with the highest priority
        return self.data[0]
    
    def set_schedule_time(self, start_time, end_time):
        # Set the schedule time range
        self.start_time = start_time
        self.end_time = end_time

    def get_schedule(self):
        # Get the schedule of tasks within the specified time range
        if self.start_time is None or self.end_time is None:
            return []

        self.time = self.start_time
        scheduled_tasks = []

        while not self.is_empty() and self.time < self.end_time:
            task = self.get_highest_priority_task()

            if self.time + task.execution_time <= task.deadline:
                task.turnaround_time = self.time + task.execution_time
            else:
                task.turnaround_time = task.deadline

            task.waiting_time = task.turnaround_time - task.execution_time

            scheduled_tasks.append(task)
            self.time = task.turnaround_time
            self.data.pop(0)
        return scheduled_tasks

    def is_empty(self):
        # Check if the max heap is empty
        return len(self.data) == 0


# Example usage:

task1 = Task(101, 7, 4, 10)
task2 = Task(102, 9, 5, 15)
task3 = Task(103, 5, 3, 12)
task4 = Task(104, 8, 7, 20)
task5 = Task(105, 6, 10, 25)

task_queue = MaxHeap()
task_queue.add_task(task1)
task_queue.add_task(task2)
task_queue.add_task(task3)
task_queue.add_task(task4)
task_queue.add_task(task5)

task_queue.set_schedule_time(0, 30)  

scheduled_tasks = task_queue.get_schedule()
for task in scheduled_tasks:
    print(f"Task Id={task.task_id}, Waiting Time={task.waiting_time}, Turnaround Time={task.turnaround_time}")

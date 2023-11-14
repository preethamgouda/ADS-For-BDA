class Job:
    def __init__(self, job_id, priority, execution_time):
        self.job_id = job_id
        self.priority = priority
        self.execution_time = execution_time
        self.waiting_time = 0
        self.turnaround_time = 0

class PriorityQueue:
    def __init__(self, jobs=[]):
        self.tasks = jobs
        self.clock = 0
        self._build_heap()

    def get_job_count(self):
        return len(self.tasks)

    def _parent_index(self, idx):
        return (idx - 1) // 2

    def _left_child_index(self, idx):
        return 2 * idx + 1

    def _right_child_index(self, idx):
        return 2 * idx + 2

    def _swap(self, i, j):
        self.tasks[i], self.tasks[j] = self.tasks[j], self.tasks[i]

    def _build_heap(self):
        length = len(self.tasks)
        start = (length - 2) // 2
        for idx in range(start, -1, -1):
            self._down_heap(idx, length)

    def _up_heap(self, j):
        parent = self._parent_index(j)
        if j > 0 and self.tasks[j].priority > self.tasks[parent].priority:
            self._swap(j, parent)
            self._up_heap(parent)

    def _down_heap(self, idx, length):
        if self._left_child_index(idx) < length:
            left = self._left_child_index(idx)
            big_child = left
            if self._right_child_index(idx) < length:
                right = self._right_child_index(idx)
                if self.tasks[right].priority > self.tasks[left].priority:
                    big_child = right
            if self.tasks[big_child].priority > self.tasks[idx].priority:
                self._swap(big_child, idx)
                self._down_heap(big_child, length)

    def add_job(self, job):
        self.tasks.append(job)
        self._up_heap(len(self.tasks) - 1)

    def get_highest_priority_job(self):
        return self.tasks[0]

    def execute_job(self):
        job = self.tasks[0]
        self._swap(0, len(self.tasks) - 1)
        self.tasks.pop()
        self._down_heap(0, len(self.tasks))
        self.clock += job.execution_time
        job.turnaround_time = self.clock
        job.waiting_time = job.turnaround_time - job.execution_time
        return job

    def is_empty(self):
        return len(self.tasks) == 0


job1 = Job(1, 5, 3)
job2 = Job(2, 8, 4)
job3 = Job(3, 3, 2)
job4 = Job(4, 10, 5)

job_queue = PriorityQueue()
job_queue.add_job(job1)
job_queue.add_job(job2)
job_queue.add_job(job3)
job_queue.add_job(job4)

highest_priority_job = job_queue.get_highest_priority_job()
print(f"Highest Priority Job: Job ID={highest_priority_job.job_id}, Priority={highest_priority_job.priority}")

while not job_queue.is_empty():
    current_job = job_queue.execute_job()
    print(f"Job ID={current_job.job_id}, Waiting Time={current_job.waiting_time}, Turnaround Time={current_job.turnaround_time}")

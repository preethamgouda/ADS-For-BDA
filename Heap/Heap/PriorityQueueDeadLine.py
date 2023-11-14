class Job:
    def __init__(self, job_id, priority, execution_time, deadline):
        # Initialize job attributes
        self.job_id = job_id
        self.priority = priority
        self.execution_time = execution_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.deadline = deadline

class PriorityQueue:
    def __init__(self, jobs=[]):
        # Initialize priority queue with jobs and build the heap
        self.tasks = jobs
        self._build_heap()
        self.clock = 0
    
    def get_job_count(self):
        # Get the number of jobs in the queue
        return len(self.tasks)
    
    def _parent_index(self, idx):
        # Get the parent index of a given index
        return (idx - 1) // 2
    
    def _left_child_index(self, idx):
        # Get the left child index of a given index
        return 2 * idx + 1
    
    def _right_child_index(self, idx):
        # Get the right child index of a given index
        return 2 * idx + 2
    
    def _swap(self, i, j):
        # Swap elements at indices i and j
        self.tasks[i], self.tasks[j] = self.tasks[j], self.tasks[i]
    
    def _build_heap(self):
        # Build the heap from the tasks
        length = len(self.tasks)
        start = (length - 2) // 2
        for idx in range(start, -1, -1):
            self._down_heap(idx, length)
    
    def _up_heap(self, j):
        # Perform up-heap operation
        parent = self._parent_index(j)
        if j > 0 and self.tasks[j].priority > self.tasks[parent].priority:
            self._swap(j, parent)
            self._up_heap(parent)
    
    def _down_heap(self, idx, length):
        # Perform down-heap operation
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
        # Add a job to the priority queue and perform up-heap operation
        self.tasks.append(job)
        self._up_heap(len(self.tasks) - 1)
    
    def get_highest_priority_job(self):
        # Get the job with the highest priority
        return self.tasks[0]
    
    def execute_job(self):
        # Execute a job, update clock, and perform down-heap operation
        job = self.tasks[0]
        if self.clock + job.execution_time <= job.deadline:
            job.turnaround_time = self.clock 
            job.waiting_time = job.turnaround_time - job.execution_time
            self.clock += job.execution_time
        else:
            print("Missed the deadline")
        self._swap(0, len(self.tasks) - 1)
        self.tasks.pop()
        self._down_heap(0, len(self.tasks))
        
        return job

    def is_empty(self):
        # Check if the priority queue is empty
        return len(self.tasks) == 0


# Example usage:

job1 = Job(101, 9, 4, 20)
job2 = Job(102, 7, 5, 25)
job3 = Job(103, 6, 3, 15)
job4 = Job(104, 10, 6, 30)

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

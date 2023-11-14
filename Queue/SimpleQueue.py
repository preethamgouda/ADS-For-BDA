class SimpleQueueModified:
    def __init__(self):
        self.queue_data = []
        self.element_count = 0

    def get_element_count(self):
        return self.element_count

    def is_queue_empty(self):
        return self.element_count == 0

    # Adding element to front
    def enqueue(self, element):
        self.queue_data.append(element)
        self.element_count += 1
        return self.element_count

    # To remove element from rear
    def dequeue(self):
        if not self.is_queue_empty():
            self.element_count -= 1
            return self.queue_data.pop(0)
        else:
            return None

    # To get element at rear
    def peek(self):
        if not self.is_queue_empty():
            return self.queue_data[0]
        else:
            return None

    def print_elements(self):
        return self.queue_data

import multiprocessing


class ProcessManager:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.pool = multiprocessing.Pool(processes=num_processes)

    def worker_function(self, arg):
        # This is the worker function that will be called by each process
        # Do some processing with arg and return the result
        print("arg:", arg)
        return arg * arg

    def process_data(self, data):
        # This method will spawn new processes and call worker_function for each chunk of data
        chunk_size = len(data) // self.num_processes
        results = []
        for i in range(self.num_processes):
            chunk = data[i * chunk_size : (i + 1) * chunk_size]
            result = self.pool.apply_async(self.worker_function, (chunk,))
            results.append(result)
        # Collect the results from each process
        output = [result.get() for result in results]
        return output


if __name__ == "__main__":
    data = list(range(10))
    manager = ProcessManager(num_processes=4)
    output = manager.process_data(data)
    print(output)

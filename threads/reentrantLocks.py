"""
What if 2 threads are trying to acquire a lock
but 1 thread is calling another thread inside of it as a function call
Hence Thread 2 would be stuck, as thread 1 wouldn't have released its lock

"""
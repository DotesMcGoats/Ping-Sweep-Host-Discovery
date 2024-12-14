import time
import threading
import logging


logging.basicConfig(filename='function_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


def timer(update_callback):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = [None]  # Use a list to store the result so it can be modified within the thread
            state = {'i': 0, 'total_ips': 0, 'formatted_time': '00:00:00'}  # Shared state for progress

            def run_func():
                result[0] = func(state, *args, **kwargs)

            # Run the decorated function in a separate thread
            func_thread = threading.Thread(target=run_func)
            func_thread.start()

            # Loop to print the elapsed time every second
            while func_thread.is_alive():
                elapsed_time = time.time() - start_time
                state['formatted_time'] = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                update_callback(state['formatted_time'], state['i'], state['total_ips'])
                time.sleep(1)

            # Ensure the final elapsed time is printed
            elapsed_time = time.time() - start_time
            state['formatted_time'] = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            update_callback(state['formatted_time'], state['i'], state['total_ips'])

            return result[0]

        return wrapper
    return decorator

def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.info(f"Function '{func.__name__}' started.")
        try:
            result = func(*args, **kwargs)
            success = True
        except Exception as e:
            logging.error(f"Function '{func.__name__}' failed with error: {e}")
            success = False
            result = None
        end_time = time.time()
        elapsed_time = end_time - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        logging.info(f"Function '{func.__name__}' completed. Success: {success}. Time taken: {formatted_time} seconds. Output: {result}")
        return result
    return wrapper
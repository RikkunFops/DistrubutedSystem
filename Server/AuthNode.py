import socket
import socketserver
import Server.ServerLib as ServerLib
import queue
import threading

Auth_Queue = queue.Queue()

def handle_auth_request(username, password):
    if is_valid_input(username, password):
        Auth_Queue.put((username, password))
        return "Request added to queue"
    else:
        return "invalid credentials"
    
def is_valid_input(username, password):



    auth_worker_thread = threading.Thread(target=authorization_worker)
    auth_worker_thread.daemon = True  # This makes the thread exit when the main program exits
    auth_worker_thread.start()


def authorization_worker():
    while True:
        username, password = Auth_Queue.get()
        # Perform authentication and authorization checks here
        if is_authorized(username, password):
            # Grant access
            print(f"Access granted for {username}")
        else:
            # Deny access
            print(f"Access denied for {username}")
        Auth_Queue.task_done()

def is_authorized(username, password):

    if (username, password) == ("Admin", "Admin"):
        return True
    else:
        return False
    # Implement your authorization logic here
    # Check the username and password against your system's rules
    # Return True if authorized, False if not

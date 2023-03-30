# HowTo: script-template that fits to sqe & code

import cadquery as cq

if 'log' not in globals():
    def log(message):
        return

if 'show_object' not in globals():
    def show_object(self, name, options={}, **kwargs):
        return
    
if 'debug' not in globals():    
    def debug(self, obj, args={}):
        return
    
def echo(message):
    print(message)   # code: goes to console, sqe: goes to parent-shell
    log(message)     # sqe:  goes only log-viewer
    return
    
def job():
    # define model here
    return

if __name__ == "__main__" or __name__ == "temp":
    echo("main")
    job()
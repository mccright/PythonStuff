# Short Reminders  

### Use sys.exit(), not exit() or quit()  
A call to [sys.exit()](https://docs.python.org/3/library/sys.html#sys.exit) is translated into an exception so that clean-up handlers ([finally](https://docs.python.org/3/reference/compound_stmts.html#finally) clauses of [try](https://docs.python.org/3/reference/compound_stmts.html#try) statements) can be executed, and so that a debugger can execute a script without running the risk of losing control. The [os._exit()](https://docs.python.org/3/library/os.html#os._exit) function can be used if it is absolutely positively necessary to exit immediately (for example, in the child process after a call to [os.fork()](https://docs.python.org/3/library/os.html#os.fork)).  

[exit()](https://docs.python.org/2/library/constants.html#exit) and [quit()](https://docs.python.org/3/library/constants.html#quit) raise the SystemExit exception.  They exist to support interactive Python in the interpreter.  They rely the site module and should only be used in the interpreter and not in production code.  

See also: [https://docs.python.org/3/library/exceptions.html#SystemExit](https://docs.python.org/3/library/exceptions.html#SystemExit) and https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used/19747562#19747562  


### One-Liner to set up my virtual environment  
```bash
python3 -m virtualenv --python="$(command -v python3)" .env && 
  source .env/bin/activate && 
  python3 -m pip install --upgrade pip virtualenv && 
  python3 -m pip install --upgrade setuptools wheel && 
  python3 -m pip install -r requirements.txt 
```

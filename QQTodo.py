"""
The purpose of this code is to create a working todo list manager program for my own use.
Requrements:
	Text based
	Each task must have a project and a context
	Projects are noted with a leading '+'
	Contexts are notes with a leading '@'
		i.e. Buy a new trashcan +home @store
	Tasks are either True (to be done) or False (done)
"""

class Todo:
	""" A todo item with the following properties
		task: the description of the task itself as a string
		project: the project associtated with this task as a string
		context: the context in which the taks is most likely done as a string
		state: the state of doneness of the task as a boolean T/F
	"""
	def __init__(self, task, project, context, state):
		"""return a ToDo that is a *taks* with a *project* and a *context* and a state of True (all
		new tasks are in a state of 'to be done' by default.
		"""
		self.task = task
		self.project = project
		self.context = context
		self.state = True
		

newtask = input(str("What is the task?\n"))
newproject = input(str("What is the project associated with this task? \n")) 
newcontext = input(str("Where can this taks be done? \n"))
state = True

newTask = Todo(newtask, newproject, newcontext, True)

"""
newTask = Todo("Find out how to make this work", "+QQTodo", "@everywhere", True)
"""

print ("This is your new task:", newTask.task, newTask.project, newTask.context)

from pymongo import MongoClient
from flask import Flask

client = MongoClient('localhost', 27017)
db = client.caveTalk
app = Flask(__name__)


@app.route('/set/<name>/<task>/<subTasks>')
def set(name, task, subTasks):
    print name
    print task
    print subTasks
    taskList = []
    for subTask in subTasks.split(','):
        taskList.append(subTask)
    dictionary = {"name": name, "task": task, "list": taskList}

    db.tasks.insert(dictionary)
    return 'success'


@app.route('/getName/<name>')
def getName(name):
    results = ""
    for task in db.tasks.find({"name": name}):
        print task['list'][0]
        task = str(task)
        results += task
    return results


@app.route('/getTask/<taskName>')
def getTask(taskName):
    results = ""
    for task in db.tasks.find({"task": taskName}):
        task = str(task)
        results += task
        print task
    return results


if __name__ == '__main__':
    app.run(debug=True)

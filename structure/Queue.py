class Queue:
    def __init__(self) -> None:
        self.list = []

    def push(self, item):
        self.list.append(item)
    def pop(self):
        item = self.list[0]
        self.list.pop(0)
        print(item)
        return item
    def getList(self):
        return self.list


pepa = Queue()
pepa.push("1111")
pepa.push("2222")
pepa.push("3333")
pepa.pop()
print(pepa.getList())
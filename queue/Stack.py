class Stack:
    def __init__(self) -> None:
        self.list = []

    def push(self, item):
        self.list.append(item)
    def pop(self):
        index = len(self.list)-1
        item = self.list[index]
        self.list.pop(index)
        print(item)
        return item
    def getList(self):
        return self.list


pepa = Stack()
pepa.push("1111")
pepa.push("2222")
pepa.push("3333")
pepa.pop()
print(pepa.getList())
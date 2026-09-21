class person:
    def __init__(self, name, occuption):
        self.name = name
        self.occuption = occuption
    @property
    def show(self):
        return 10 * 20
    @show.setter
    def show2(self, value):
        return 10 * value

a = person("mushfika", "software engineer")

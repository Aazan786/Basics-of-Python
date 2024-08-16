class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) +1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __len__(self):
        return len(self.__tags)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()]= count
    
    def __iter__(self):
        return (self.__tags)
    


cloud = TagCloud()
print(cloud["Python"])
#print(len(tags))
cloud.add("python")
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)
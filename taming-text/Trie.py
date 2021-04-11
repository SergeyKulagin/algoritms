# todo double check
class Node:
    def __init__(self, isWord: bool = False, suffix: str = None) -> None:
        self.isWord = isWord
        self.suffix = suffix
        self.children = (None, dict())[suffix is None]

    def __repr__(self) -> str:
        return "isWord=" + str(self.isWord) + ", suffix=" + str(self.suffix)

    def addWord(self, word: str, index: int = 0):
        if index == len(word):
            self.isWord = True
            return

        if self.suffix is not None:
            if word[index:] == self.suffix:
                return
            temp_suffix = self.suffix
            self.suffix = None
            self.children = dict()
            self.addWord(temp_suffix, 0)

        sym = word[index]
        child = self.children.get(sym)
        if child is None:
            if index + 1 == len(word):
                self.children[sym] = Node(isWord=True)
            else:
                self.children[sym] = Node(isWord=False, suffix=word[(index + 1):])
            return

        child.addWord(word=word[(index + 1):])


root = Node(suffix="")
root.addWord("hello")
root.addWord("he")
root.addWord("hell")
print(root)

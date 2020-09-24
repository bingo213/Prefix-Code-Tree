class PrefixCodeTree:
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = str(data)
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = PrefixCodeTree(newNode)
        else:
            t = PrefixCodeTree(newNode)
            t.left = self.left
            self.left = t
    def insertRight(self,newNode):
        if self.right == None:
            self.right = PrefixCodeTree(newNode)
        else:
            t = PrefixCodeTree(newNode)
            t.right = self.right
            self.right = t
    def insert(self, codeword, symbol):
        for i in range (0, len(codeword)-1):
            if codeword[i] == 0:
                if self.left == None:
                    self.insertLeft('')
                self = self.left
            else:
                if self.right == None:
                    self.insertRight('')
                self = self.right
        if codeword[len(codeword)-1] == 0:
            self.insertLeft(symbol)
        else:
            self.insertRight(symbol)
    def decode(self, encodedData, datalen):
        data = ""
        for byte in encodedData:
            data += f'{byte:0>8b}'

        root = self
        res = ''
        for i in range (0, datalen):
            if int(data[i]) == 0:
                root = root.left
            else:
                root = root.right
            if root.left == None and root.right == None:
                res += root.data
                root = self
        return res

'''Thử nghiệm:
codeTree = PrefixCodeTree()
codebook = {
    'x1': [0],
    'x2': [1, 0, 0],
    'x3': [1, 0, 1],
    'x4': [1 , 1]
}
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

data = b'\xd2\x9f\x20' 
print(codeTree.decode(data, 21))

==> output: x4x1x2x3x1x1x4x4x2x2 '''




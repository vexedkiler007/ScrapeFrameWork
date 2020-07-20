

class Script:
    # @staticmethod
    def indeed():
        print('test2')


# defs = [i for i in dir(Script) if "__" not in i]
# print(defs)

methods_list = [obj for obj in Script.__dict__.items() if "__" not in obj[0]]

for method in methods_list:
    method[1]()

# https://gist.github.com/strager/aa1f1cd7b6971587e3e72519d93ab120
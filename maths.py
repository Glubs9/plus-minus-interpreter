class abs_node:
    #for all nodes on the tree
    def __init__(self):
        pass
    def get_val(self):
        pass

class func_node:
    def __init__(self, a, b, f):
        self.a = a
        self.b = b
        self.f = f
    def get_val(self):
        return self.f(self.a.get_val(), self.b.get_val())
    def __str__(self):
        return str(self.a) + str(self.f) + str(self.b)

class num:
    def __init__(self, num):
        self.num = int(num)
    def get_val(self):
        return self.num
    def __str__(self):
        return str(self.num)

def get_inner(arr, pos):
    tmp = pos + 1
    am = 1
    while am != 0:
        if arr[tmp] == ")":
            am-=1
        if arr[tmp] == "(":
            am += 1
        tmp+=1
    return tmp-1

def test(val):
    return val in ["(", ")", "+", "-"]

def separate(str_in):

    ret = []
    prev = []

    for n in str_in:
        if test(n):
            if prev != []:
                ret.append("".join(prev))
                prev = []
            ret.append(n)
        else:
            prev.append(n)

    return ret if prev == [] else ret + ["".join(prev)]

def build_nums(str_in):
    top = []
    pos = 0
    for n in range(len(str_in)):
        top.append(str_in[n] if test(str_in[n]) else num(str_in[n]))
    return top

def build_brackets(arr_in):
    top = arr_in
    nex = []
    n = 0
    while n < len(top):
        if top[n] == "(":
            tmp = get_inner(top, n)
            nex.append(build_brackets(top[n+1:tmp]))
            n = tmp
        else:
            nex.append(top[n])
        n += 1
    return nex

def build_funcs(ast_in):

    if isinstance(ast_in, num):
        return ast_in
    if len(ast_in) == 1 and isinstance(ast_in[0], num):
        return ast_in[0]
    if len(ast_in) == 1:
        return build_funcs(ast_in[0])

    n = 3
    ret = func_node(
            build_funcs(ast_in[0]),
            build_funcs(ast_in[2]),
            (lambda a, b : a + b) if ast_in[1] == "+" else (lambda a, b : a - b)
    )

    while n < len(ast_in):
        ret = func_node(
                ret,
                build_funcs(ast_in[n+1]),
                (lambda a, b : a + b) if ast_in[n] == "+" else (lambda a, b : a - b)   
        )
        n+=2
    return ret

def compose(*argv):
    funcs = argv
    def ret_f(*argv, **kwargs):
        ret = funcs[0](*argv, **kwargs)
        for n in funcs[1:]:
            ret = n(ret)
        return ret
    return ret_f

def remove_spaces(str_in):
    return [n for n in str_in if n != " "]

def maths(str_in):
    return compose(remove_spaces, separate, build_nums, build_brackets, build_funcs, lambda a : a.get_val())(str_in)

inp = input("enter maths: ")
print(maths(inp))

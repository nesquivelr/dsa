"""TODO"""
def is_delim(c: str):
    return c == " "

def is_op(c: str):
    return c in "+-*/"

def is_unary(c: str):
    return c in "+-"

def priority(op: str):
    if op < 0:
        return 3
    if chr(op) in "*/":
        return 2
    if chr(op) in "+-":
        return 1
    return -1

def process_op(st: list, op: str):
    if op < 0:
        l = st.pop()
        match -op:
            case "+":
                st.append(l)
            case "-":
                st.append(-l)
    else:
        r = st.pop()
        l = st.pop()
        match op:
            case "+":
                st.append(l+r)
            case "-":
                st.append(l-r)
            case "*":
                st.append(l*r)
            case "/":
                st.append(l/r)

def evaluate(s: str):
    st = []
    op = []
    may_be_unary = True
    for i in range(len(s)):
        if is_delim(s[i]):
            continue
        if s[i] == "(":
            op.append("(")
            may_be_unary = True
        elif s[i] == ")":
            while op[-1] != "(":
                process_op(st, op[-1])
                op.pop()
            op.pop()
            may_be_unary = False
        elif is_op(s[i]):
            cur_op = ord(s[i])
            if may_be_unary and is_unary(cur_op):
                cur_op = -cur_op
            while len(op)!=0 and (
                  (cur_op>=0 and priority(op[-1]) >= priority(cur_op)) or
                  (cur_op<0 and priority(op[-1]) > priority(cur_op))
            ):
                process_op(st, op[-1])
                op.pop()
            op.append(cur_op)
            may_be_unary = True
        else:
            number = 0
            while i < len(s) and s[i].isnumeric():
                number = number * 10 + ord(s[i]) - ord("0")
                i += 1
            i -= 1
            st.append(number)
            may_be_unary = False
    while op:
        process_op(st, op[-1])
        op.pop()
    return st[-1]


if __name__ == "__main__":
    print(evaluate("1 + 2 * (3 - 4 * 5 + 2) / 2"))

from collections import Counter, defaultdict
import operator


def get_max_pow(n: int):
    value = 1
    while value < n:
        if 2**value >= n:
            return value
        value += 1

def create_table(counter: Counter, bits: int):
    current_bit = 0
    table = defaultdict(lambda: 0)
    for key in counter.keys():
        table[key] = bin(current_bit)[2:].zfill(bits)
        current_bit += 1
    return table


def fixed_sized_codes(message: str):
    counter = Counter(message)
    unique_values = len(counter)
    max_pow = get_max_pow(unique_values)
    table = create_table(counter, max_pow)
    new_message = ''
    for char in message:
        new_message += table[char]

    inv_table = {v: k for k, v in table.items()}
    return inv_table, new_message

def decode_fixed_codes(table, message: str):
    decoded_message = ''
    for idx in range(0, len(message), 3):
        current_char = slice(idx, idx+3)
        decoded_message += str(table[message[current_char]])
    return decoded_message

class Node:
    def __init__(self, value: str, frequency: int, left=None, right=None, huffman: str=''):
        self.value = value
        self.frequency = frequency
        self.huffman = huffman
        self.left = left
        self.right = right

def get_codes(node, value, table):
    new_value = value + node.huffman
    if node.left:
        get_codes(node.left, new_value, table)
    if node.right:
        get_codes(node.right, new_value, table)
    if not node.left and not node.right:
        table[node.value] = new_value
    return table


def variable_sized(message: str):
    counter = Counter(message)
    nodes = []
    for key, value in counter.items():
        nodes.append(Node(key, value))

    while len(nodes) != 1:
        node_left = min(nodes, key=operator.attrgetter('frequency'))
        node_left.huffman = '0'
        nodes.remove(node_left)
        node_right = min(nodes, key=operator.attrgetter('frequency'))
        node_right.huffman = '1'
        nodes.remove(node_right)
        father = Node(
            node_left.value+node_right.value,
            node_left.frequency+node_right.frequency,
            node_left,
            node_right
        )
        nodes.append(father)
    table = dict()
    table = get_codes(nodes[0], '', table)
    new_message = ''
    for char in message:
        new_message += table[char]

    inv_table = {v: k for k, v in table.items()}
    return inv_table, new_message

def decode_variable_codes(table, message:str):
    decoded_message = ''
    message_len = len(message)
    i = 0
    while i < message_len:
        j = i+1
        while j <= message_len:
            current_bits = message[i:j]
            if current_bits in table:
                decoded_message += str(table[current_bits])
                break
            j += 1
        i = j
    return decoded_message

if __name__ == '__main__':
    message = 'BCCABBDDAECCBBAEDDCC'
    print(message)
    table, enc_message = fixed_sized_codes(message)
    dec_message = decode_fixed_codes(table, enc_message)
    print(enc_message)
    print(table)
    print(dec_message)
    table, enc_message = variable_sized(message)
    dec_message = decode_variable_codes(table, enc_message)
    print(enc_message)
    print(table)
    print(dec_message)

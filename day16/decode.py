#!/usr/bin/env python3

from functools import reduce

# Helper functions
def b2int(binary):
    return int(binary, 2)

def main():
    f = open('input.txt', 'r').readline().strip()
    inp = bin(int(f, 16))[2:].zfill(len(f) * 4)

    packet, leftover = parse_packets(inp)
    # packet.debug()
    print('Part 1:', packet.get_version())
    print('Part 2:', packet.get_value())

class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.result = None
        self.subpackets = []

    def read_literal(self, data):
        index = 0
        literal = ''
        while True:
            literal += data[index + 1: index + 5]
            if data[index] == '0':
                break
            index += 5

        self.result = b2int(literal)
        return data[index + 5:]

    def debug(self):
        print(f'Version: {self.version}, Type: {self.type}, Literal: {self.result}')
        for s in self.subpackets:
            s.debug()
    
    def get_version(self):
        if self.type != 4:
            self.version += sum(s.get_version() for s in self.subpackets)
        return self.version
    
    def larger(self):
        sp1, sp2 = self.subpackets
        return 1 if sp1.get_value() > sp2.get_value() else 0
    
    def smaller(self):
        sp1, sp2 = self.subpackets
        return 1 if sp1.get_value() < sp2.get_value() else 0
    
    def equal(self):
        sp1, sp2 = self.subpackets
        return 1 if sp1.get_value() == sp2.get_value() else 0

    def get_value(self):
        t = self.type
        subpack_vals = [s.get_value() for s in self.subpackets]
        if t == 0:
            return sum(subpack_vals)
        if t == 1:
            return reduce((lambda x, y: x * y), subpack_vals)
        if t == 2:
            return min(subpack_vals)
        if t == 3:
            return max(subpack_vals)
        if t == 5:
            return self.larger()
        if t == 6:
            return self.smaller()
        if t == 7:
            return self.equal()
        # If t == 4
        return self.result

def parse_packets(data):
    version = b2int(data[:3])
    type = b2int(data[3:6])

    packet = Packet(version, type)

    if type == 4:
        bits_left = packet.read_literal(data[6:])
        return packet, bits_left
    return parse_subpacket(data[6:], packet)

def parse_subpacket(data, packet):
    type_id = data[0]
    if type_id == '0':
        overall_len = b2int(data[1: 16])
        subpackets = data[16: 16+overall_len]
        leftover = data[16+overall_len:]

        while len(subpackets) != 0:
            subpacket, subpackets = parse_packets(subpackets)
            packet.subpackets.append(subpacket)

    else:
        num_subpackets = b2int(data[1:12])
        leftover = data[12:]

        for i in range(num_subpackets):
            subpacket, leftover = parse_packets(leftover)
            packet.subpackets.append(subpacket)

    return packet, leftover


if __name__ == '__main__':
    main()

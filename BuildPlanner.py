#!/usr/bin/env python2.7

import copy

blueprintFilename = "blueprint.txt"



def new_grid3d(length, width, depth, fillValue):
    return new_grid(length, width, new_list(depth, fillValue))

def new_grid(length, width, fillValue):
    return new_list(length, new_list(width, fillValue))

def new_list(length, fillValue):
    return [copy.deepcopy(fillValue) for _ in range(0,length)]


class InvalidBlockPlacement(Exception):
    def __init__(self, blocks):
        super("These blocks are floating: {}".format(",".join(blocks)))


class Block:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)


def load_blueprint():
    with open(blueprintFilename, 'r') as bpf:
        blocks = map(lambda y: map(lambda x: x.split(','), y),
                     map(lambda x: x.split('\n'),
                         bpf.read().split("\n--\n")))
        xSize = len(blocks)
        ySize = len(blocks[0])
        zSize = len(blocks[0][0])
        nuBlocks = [[]]
        for x in range(0, xSize):
            for y in range(0, ySize):
                for z in range(0, zSize):
                    if blocks[z][y][x] == 1:
                        nuBlocks.append(Block (x, y, z))
        return blocks, xSize, ySize, zSize


def sep_layers(blocks):
    layers = new_list(10, [])
    for b in blocks:
        layers[b.z].append(b)
    return layers


def list_invalid_blocks(blocks, x_size, y_size):
    invalid_blocks = []
    is_supported = new_grid(x_size, y_size, True)
    for layer in sep_layers(blocks):
        next_is_supported = new_grid(x_size, y_size, False)
        for b in layer:
            if is_supported[b.x][b.y]:
                next_is_supported[b.x][b.y] = True
            else:
                invalid_blocks.append(b)

        is_supported = copy.deepcopy(next_is_supported)

    return invalid_blocks

def plan_construction(blocks):
    #sorting blocks into construction order
    tempList = []
    for z in range(0, 11):
        for y in range(12, -1, -1):
            for x in range(0, 11):
                for block in blocks:
                    if block.x == x and block.y == y and block.z == z:
                        tempList.append(block)
    return tempList

def execute_construction(instructionSet):
    #move torso
    #move elbow
    #move wrist
    
    #move yz stabilizer
    #move xy stabilizer
    #move gripper
    
                        
if __name__ == "__main__":
    blocks, x_size, y_size, z_size = load_blueprint()
    invalid_blocks = list_invalid_blocks(blocks, x_size, y_size)
    if len(invalid_blocks) != 0:
        raise InvalidBlockPlacement(invalid_blocks)
    else:
        print "This structure is possible to build."
    instructionSet = plan_construction(blocks)
    execute_construction(instructionSet)

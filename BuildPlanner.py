#!/usr/bin/env python2.7

blueprintFilename = "blueprint.txt"

class InvalidBlockPlacement (Exception):
    def __init__ (self, blocks):
        super.__init__("These blocks are not supported: {}".format(",".join(blocks)))

def load_blueprint ():
    with open(blueprintFilename, 'r') as bpf:
        blocks = map(lambda y: map(lambda x: x.split(','), y),
                      map(lambda x:x.split('\n'),
                           bpf.read().split("\n--\n")
                           )
                      )
        xSize = len (blocks)
        ySize = len (blocks[0])
        zSize = len (blocks[0][0])
        nuBlocks = [[]]
        for x in range(0, xSize):
            for y in range(0, ySize):
                for z in range(0, zSize):
                    if blocks[z][y][x] == 1:
                        nuBlocks[len(nuBlocks)] = (x,y,z)
        return blocks, xSize, ySize, zSize


def sep_layers (blocks):
    layers = [[]]
    for b in blocks:
        layers[b[2]][len(layers[b[2]])] = b
    return layers


def list_invalid_blocks (blocks, xSize, ySize):
    invalid_blocks = []

    is_suborted = [[]]
    for x in range(0, xSize):
        for y in range(0, ySize):
            is_suborted[x][y] = True

    next_is_suborted = [[]]
    for x in range(0, xSize):
        for y in range(0, ySize):
            next_is_suborted[x][y] = False

    for layer in sep_layers (blocks):
        next_is_suborted = [[]]
        for x in range(0, xSize):
            for y in range(0, ySize):
                next_is_suborted[x][y] = False

        for b in layer:
            if ~is_suborted[b[0]][b[1]]:
                invalid_blocks[len(invalid_blocks)] = b
            else:
                next_is_suborted[b[0]][b[1]] = True

        is_suborted = next_is_suborted

    return invalid_blocks

if __name__ == "__main__":
    blocks, x_size, y_size, z_size = load_blueprint()
    invalid_blocks = list_invalid_blocks(blocks, x_size, y_size)
    if len(invalid_blocks) != 0:
        raise InvalidBlockPlacement(invalid_blocks)
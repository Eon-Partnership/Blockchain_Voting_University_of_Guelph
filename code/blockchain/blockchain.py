from block import Block
from exceptions.block_exception import BlockException

class BlockChain():
    def __init__(self) -> None:
        self.blocks = []

    def add_block(self, block: Block):
        # Appending the block to the chain
        if block.block_header.previous_block_hash == None: # Genesis Block
            self.blocks.append(block)
        else: # Non-Genesis Block
            last_block = self.blocks[-1]

            if last_block.block_header.current_block_hash == block.block_header.previous_block_hash:
                self.blocks.append(block)
            else:
                raise BlockException("The new block doesn't include the correct previous block hash")
# MIXBOX Inverse 2024

## Color Mixing Operations

This project is based on MIXBOX(SOTA, published on ACM Computer Graphics, 2022)

MIXBOX  is about mixing colors using forward operation in latent space. Input the 3 three RGB colors and their weights, to compute the 1 target color.

Our goal is to input the 3 three RGB colors and 1 target color, Inversely compute the weights. Both computations(forward and inverse) require converting rgb into the latent space, as its THE space where unlinear colors can opearte linearly.

# 目前问题

原论文在进行rgb to latent 转换的时候， 为了实时渲染 使用一个64 位 LUT来用空间换时间.  这个compressed lut 大小为 920kb，无法deploy在esp32上，会overflow by 700 kb bytes

现在需要减少一半精度到32， 大小也随之变为1/8, to about 98kb.

More specifically, 把原来的built-in compressed lut in 64 bit, 先decompress, 再downsample，然后使用（hopefully）相同的流程compress为compressed lut in 32 bit. swap 掉64bit的版本.

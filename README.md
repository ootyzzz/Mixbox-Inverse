# MIXBOX Inverse 2024

## Color Mixing Operations

This project is based on MIXBOX(SOTA, published on ACM Computer Graphics, 2022)

MIXBOX  is about mixing colors using forward operation in latent space. Input the 3 three RGB colors and their weights, to compute the 1 target color.

Our goal is to input the 3 three RGB colors and 1 target color, Inversely compute the weights. Both computations(forward and inverse) require converting rgb into the latent space, as its THE space where unlinear colors can opearte linearly.

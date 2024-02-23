This folder contains implementation of MISTY using pure C.

- `BlockCipherCommon.h` and `BlockCipherCommon.c` provides a template for block cipher algorithm.
  - Note: You **SHOULD** register you own `KeySet` struct into `BlockCipherCommon.h`. (e.g., `typedef MistyKeySet KeySet;`)
  - Note: `BlockCipherCommon.c` uses OpenMPI to accelerate `for` loops.
- `MistyComponents.h` contains declaration of `MistyKeySet` struct and functions in `MistyComponents.c`.
- `MistyComponents.c` contains definition of basic components, block encryt/decrypt and key scheduling progress.
- `MistyAPI.h` represents the way of creating a CipherState of MISTY, which can be treated as an encapsulation.

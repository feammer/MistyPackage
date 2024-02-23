#pragma once
#ifndef BLOCK_CIPHER_COMMON_H
#define BLOCK_CIPHER_COMMON_H

#include <stdio.h> // perror
#include <stdlib.h> // malloc
#include <stdint.h>
#include <memory.h> // memcpy
#include <omp.h>

typedef enum MODE { ECB = 0, CBC = 1, CFB = 2, OFB = 3, CTR = 4 } MODE;

#include "MistyComponents.h"
typedef MistyKeySet KeySet;

typedef void (*BlockOperation)(const KeySet key_set, const uint8_t* in, uint8_t* out);
typedef struct _CipherState CipherState;
typedef void (*CipherOperation)(const CipherState* self, const uint8_t* in, uint8_t* out, const int64_t data_len);

typedef struct {
	BlockOperation block_encrypt;
	BlockOperation block_decrypt;
	size_t block_len;
} BlockState;

typedef struct _CipherState {
	const BlockState block_state;
	const CipherOperation encrypt;
	const CipherOperation decrypt;
	const KeySet key_set;
	MODE mode;
	const uint8_t* iv;
} CipherState;

void cipher_encrypt(const CipherState* self, const uint8_t* in, uint8_t* out, const int64_t data_len);
void cipher_decrypt(const CipherState* self, const uint8_t* in, uint8_t* out, const int64_t data_len);
void u8arr_xor(const uint8_t* src, const size_t len, uint8_t* dst);

#endif // BLOCK_CIPHER_COMMON_H

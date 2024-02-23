#include "BlockCipherCommon.h"

void cipher_encrypt(const CipherState* self, const uint8_t* in, uint8_t* out, const int64_t data_len) {
	size_t block_len = self->block_state.block_len;
	if (data_len % block_len != 0) {
		perror("data_len % block_len != 0\n");
		return;
	}
	BlockOperation encrypt_func = self->block_state.block_encrypt;
	KeySet key_set = self->key_set;
	switch (self->mode)
	{
	case ECB: {
		int64_t offset = 0;
#pragma omp parallel for
		for (offset = 0; offset < data_len; offset += block_len) {
			encrypt_func(key_set, in + offset, out + offset);
		}
		break;
	}
	case CBC: {
		uint8_t* in_var = (uint8_t*)malloc(sizeof(uint8_t) * data_len);
		if (in_var != NULL)
		{
			memcpy(in_var, in, sizeof(uint8_t) * data_len);
		}
		else
		{
			perror("memory alloc opration failed\n");
		}
		u8arr_xor(self->iv, block_len, in_var);
		encrypt_func(key_set, in_var, out);
		for (int64_t offset = block_len; offset < data_len; offset += block_len) {
			u8arr_xor(out + offset - block_len, block_len, in_var + offset);
			encrypt_func(key_set, in_var + offset, out + offset);
		}
		break;
	}
	case CFB:
		break;
	case OFB:
		break;
	case CTR:
		break;
	default:
		break;
	}
}

void cipher_decrypt(const CipherState* self, const uint8_t* in, uint8_t* out, const int64_t data_len) {
	size_t block_len = self->block_state.block_len;
	if (data_len % block_len != 0) {
		perror("data_len % block_len != 0\n");
		return;
	}
	BlockOperation decrypt_func = self->block_state.block_decrypt;
	KeySet key_set = self->key_set;
	switch (self->mode)
	{
	case ECB: {
		int64_t offset = 0;
#pragma omp parallel for
		for (offset = 0; offset < data_len; offset += block_len) {
			decrypt_func(key_set, in + offset, out + offset);
		}
		break;
	}
	case CBC: {
		uint8_t* in_var = (uint8_t*)malloc(sizeof(uint8_t) * data_len);
		if (in_var != NULL)
		{
			memcpy(in_var, in, sizeof(uint8_t) * data_len);
		}
		else
		{
			perror("memory alloc opration failed\n");
		}
		decrypt_func(key_set, in_var, out);
		u8arr_xor(self->iv, block_len, out);
		for (int64_t offset = block_len; offset < data_len; offset += block_len) {
			decrypt_func(key_set, in_var + offset, out + offset);
			u8arr_xor(in_var + offset - block_len, block_len, out + offset);
		}
		break;
	}
	case CFB:
		break;
	case OFB:
		break;
	case CTR:
		break;
	default:
		break;
	}
}

void u8arr_xor(const uint8_t* src, const size_t len, uint8_t* dst) {
	for (size_t i = 0; i < len; i++)
	{
		dst[i] ^= src[i];
	}
}
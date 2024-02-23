#pragma once
#ifndef MISTY_API_H
#define MISTY_API_H

#include "MistyComponents.h"

#define MISTY
#include "BlockCipherCommon.h"

CipherState New(const uint8_t* key, const MODE mode, const uint8_t* iv);

CipherState New(const uint8_t* key, const MODE mode, const uint8_t* iv) {
	const BlockState block_state = {
		.block_encrypt = Misty1BlockEncrypt,
		.block_decrypt = Misty1BlockDecrypt,
		.block_len = 8
	};
	CipherState cipher_state = {
		.block_state = block_state,
		.encrypt = cipher_encrypt,
		.decrypt = cipher_decrypt,
		.key_set = KeyScheduling(key),
		.mode = mode,
		.iv = iv
	};
	return cipher_state;
}

#endif  // MISTY_API_H
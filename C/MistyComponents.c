#include "MistyComponents.h"

/*
:param in: 16 bits, split into left(9 bits) and right(7 bits)
:param KI: 16 bits, split into left(9 bits) and right(7 bits)
:return: 16 bits
*/
EXPORT_PREFIX uint16_t FI(const uint16_t input, const uint16_t KI) {
	uint16_t _S7[] = {
		27,  50,  51,  90,  59,  16,  23,  84,  91,  26,  114, 115, 107, 44,  102,
		73,  31,  36,  19,  108, 55,  46,  63,  74,  93,  15,  64,  86,  37,  81,
		28,  4,   11,  70,  32,  13,  123, 53,  68,  66,  43,  30,  65,  20,  75,
		121, 21,  111, 14,  85,  9,   54,  116, 12,  103, 83,  40,  10,  126, 56,
		2,   7,   96,  41,  25,  18,  101, 47,  48,  57,  8,   104, 95,  120, 42,
		76,  100, 69,  117, 61,  89,  72,  3,   87,  124, 79,  98,  60,  29,  33,
		94,  39,  106, 112, 77,  58,  1,   109, 110, 99,  24,  119, 35,  5,   38,
		118, 0,   49,  45,  122, 127, 97,  80,  34,  17,  6,   71,  22,  82,  78,
		113, 62,  105, 67,  52,  92,  88,  125 };
	uint16_t _S9[] = {
		451, 203, 339, 415, 483, 233, 251, 53,  385, 185, 279, 491, 307, 9,   45,
		211, 199, 330, 55,  126, 235, 356, 403, 472, 163, 286, 85,  44,  29,  418,
		355, 280, 331, 338, 466, 15,  43,  48,  314, 229, 273, 312, 398, 99,  227,
		200, 500, 27,  1,   157, 248, 416, 365, 499, 28,  326, 125, 209, 130, 490,
		387, 301, 244, 414, 467, 221, 482, 296, 480, 236, 89,  145, 17,  303, 38,
		220, 176, 396, 271, 503, 231, 364, 182, 249, 216, 337, 257, 332, 259, 184,
		340, 299, 430, 23,  113, 12,  71,  88,  127, 420, 308, 297, 132, 349, 413,
		434, 419, 72,  124, 81,  458, 35,  317, 423, 357, 59,  66,  218, 402, 206,
		193, 107, 159, 497, 300, 388, 250, 406, 481, 361, 381, 49,  384, 266, 148,
		474, 390, 318, 284, 96,  373, 463, 103, 281, 101, 104, 153, 336, 8,   7,
		380, 183, 36,  25,  222, 295, 219, 228, 425, 82,  265, 144, 412, 449, 40,
		435, 309, 362, 374, 223, 485, 392, 197, 366, 478, 433, 195, 479, 54,  238,
		494, 240, 147, 73,  154, 438, 105, 129, 293, 11,  94,  180, 329, 455, 372,
		62,  315, 439, 142, 454, 174, 16,  149, 495, 78,  242, 509, 133, 253, 246,
		160, 367, 131, 138, 342, 155, 316, 263, 359, 152, 464, 489, 3,   510, 189,
		290, 137, 210, 399, 18,  51,  106, 322, 237, 368, 283, 226, 335, 344, 305,
		327, 93,  275, 461, 121, 353, 421, 377, 158, 436, 204, 34,  306, 26,  232,
		4,   391, 493, 407, 57,  447, 471, 39,  395, 198, 156, 208, 334, 108, 52,
		498, 110, 202, 37,  186, 401, 254, 19,  262, 47,  429, 370, 475, 192, 267,
		470, 245, 492, 269, 118, 276, 427, 117, 268, 484, 345, 84,  287, 75,  196,
		446, 247, 41,  164, 14,  496, 119, 77,  378, 134, 139, 179, 369, 191, 270,
		260, 151, 347, 352, 360, 215, 187, 102, 462, 252, 146, 453, 111, 22,  74,
		161, 313, 175, 241, 400, 10,  426, 323, 379, 86,  397, 358, 212, 507, 333,
		404, 410, 135, 504, 291, 167, 440, 321, 60,  505, 320, 42,  341, 282, 417,
		408, 213, 294, 431, 97,  302, 343, 476, 114, 394, 170, 150, 277, 239, 69,
		123, 141, 325, 83,  95,  376, 178, 46,  32,  469, 63,  457, 487, 428, 68,
		56,  20,  177, 363, 171, 181, 90,  386, 456, 468, 24,  375, 100, 207, 109,
		256, 409, 304, 346, 5,   288, 443, 445, 224, 79,  214, 319, 452, 298, 21,
		6,   255, 411, 166, 67,  136, 80,  351, 488, 289, 115, 382, 188, 194, 201,
		371, 393, 501, 116, 460, 486, 424, 405, 31,  65,  13,  442, 50,  61,  465,
		128, 168, 87,  441, 354, 328, 217, 261, 98,  122, 33,  511, 274, 264, 448,
		169, 285, 432, 422, 205, 243, 92,  258, 91,  473, 324, 502, 173, 165, 58,
		459, 310, 383, 70,  225, 30,  477, 230, 311, 506, 389, 140, 143, 64,  437,
		190, 120, 0,   172, 272, 350, 292, 2,   444, 162, 234, 112, 508, 278, 348,
		76,  450 };
	uint16_t L = (input >> 7) & 0x1FF;
	uint16_t R = input & 0x7F;
	// Round 1
	L = _S9[L] ^ R;
	L ^= R;
	R ^= L;
	L ^= R;
	// Round 2
	L = _S7[L] ^ (R & 0x7F);
	L ^= ((KI >> 9) & 0x7F);
	R ^= KI & 0x1FF;
	L ^= R;
	R ^= L;
	L ^= R;
	// Round 3
	L = _S9[L] ^ R;
	L ^= R;
	R ^= L;
	L ^= R;
	uint16_t output = (L << 9) | R;
	return output;
}

/*
:param in: 4 bytes (32 bits), split into left(16 bits) and right(16bits)
:param KO: [KO_1, KO_2, KO_3, KO_4], 16 bits each
:param KI: [KI_1, KI_2, KI_3], 16 bits each
:return: 4 bytes (32 bits)
*/
EXPORT_PREFIX uint32_t FO(const uint32_t input, const uint16_t KO[4], const uint16_t KI[3]) {
	uint16_t L = (uint16_t)((input >> 16) & 0xFFFF);
	uint16_t R = (uint16_t)(input & 0xFFFF);
	// Round 1
	L = FI(L ^ KO[0], KI[0]) ^ R;
	L ^= R;
	R ^= L;
	L ^= R;
	// Round 2
	L = FI(L ^ KO[1], KI[1]) ^ R;
	L ^= R;
	R ^= L;
	L ^= R;
	// Round 3
	L = FI(L ^ KO[2], KI[2]) ^ R;
	L ^= R;
	R ^= L;
	L ^= R;

	L ^= KO[3];
	uint32_t output = (((uint32_t)L) << 16) | ((uint32_t)R);
	return output;
}

/*
:param in: 32 bits, split into left(16 bits) and right(16 bits)
:param KL: [KL_1, KL_2], 16 bits each
:return: 4 bytes 32 bits
*/
EXPORT_PREFIX uint32_t FL(const uint32_t input, const uint16_t KL[2]) {
	uint16_t L = (uint16_t)((input >> 16) & 0xFFFF);
	uint16_t R = (uint16_t)(input & 0xFFFF);
	R ^= L & KL[0];
	L ^= R | KL[1];
	uint32_t output = (((uint32_t)L) << 16) | ((uint32_t)R);
	return output;
}

/*
:param in: 32 bits, split into left(16 bits) and right(16 bits)
:param KL: [KL_1, KL_2], 16 bits each
:return: 4 bytes 32 bits
*/
EXPORT_PREFIX uint32_t FL_inv(const uint32_t input, const uint16_t KL[2]) {
	uint16_t L = (uint16_t)((input >> 16) & 0xFFFF);
	uint16_t R = (uint16_t)(input & 0xFFFF);
	L ^= R | KL[1];
	R ^= L & KL[0];
	uint32_t output = (((uint32_t)L) << 16) | ((uint32_t)R);
	return output;
}

EXPORT_PREFIX MistyKeySet KeyScheduling(const uint8_t key[16]) {
	uint16_t origin_key[8] = { 0 };
	uint16_t derive_key[8] = { 0 };
	for (uint8_t i = 0; i < 8; i++) {
		origin_key[i] |= ((uint16_t)key[2 * i]) << 8;
		origin_key[i] |= ((uint16_t)key[2 * i + 1]);
	}
	MistyKeySet key_set = { {0}, {0}, {0} };
	for (int i = 0; i < 8; i++) {
		derive_key[i] = FI(origin_key[i], origin_key[(i + 1) % 8]);
	}
	for (int i = 0; i < 8; i++) {
		key_set.KO[i][0] = origin_key[(i) % 8];
		key_set.KO[i][1] = origin_key[(i + 2) % 8];
		key_set.KO[i][2] = origin_key[(i + 7) % 8];
		key_set.KO[i][3] = origin_key[(i + 4) % 8];
		key_set.KI[i][0] = derive_key[(i + 5) % 8];
		key_set.KI[i][1] = derive_key[(i + 1) % 8];
		key_set.KI[i][2] = derive_key[(i + 3) % 8];
	}
	for (int i = 1; i <= 10; i++) {
		if (i % 2 == 0) {
			key_set.KL[i - 1][0] = derive_key[i / 2 + 2 - 1];
			key_set.KL[i - 1][1] = origin_key[(i / 2 + 4 - 1) % 8];
		}
		else {
			key_set.KL[i - 1][0] = origin_key[(i + 1) / 2 - 1];
			key_set.KL[i - 1][1] = derive_key[((i + 1) / 2 + 6 - 1) % 8];
		}
	}
	return key_set;
}

EXPORT_PREFIX void Misty1BlockEncrypt(const MistyKeySet key_set, const uint8_t* in, uint8_t* out) {
	uint32_t L = ((uint32_t)in[0] << 24) | ((uint32_t)in[1] << 16) | ((uint32_t)in[2] << 8) | ((uint32_t)in[3]);
	uint32_t R = ((uint32_t)in[4] << 24) | ((uint32_t)in[5] << 16) | ((uint32_t)in[6] << 8) | ((uint32_t)in[7]);
	for (int i = 0; i < 8; i++) {
		// FL Layer
		if (i % 2 == 0) {
			L = FL(L, key_set.KL[i]);
			R = FL(R, key_set.KL[i + 1]);
		}
		// Round Function Layer
		R ^= FO(L, key_set.KO[i], key_set.KI[i]);
		L ^= R;
		R ^= L;
		L ^= R;
	}
	// Extra FL Layer
	L = FL(L, key_set.KL[8]);
	R = FL(R, key_set.KL[9]);
	L ^= R;
	R ^= L;
	L ^= R;
	out[0] = (uint8_t)((L >> 24) & 0xff);
	out[1] = (uint8_t)((L >> 16) & 0xff);
	out[2] = (uint8_t)((L >> 8) & 0xff);
	out[3] = (uint8_t)(L & 0xff);
	out[4] = (uint8_t)((R >> 24) & 0xff);
	out[5] = (uint8_t)((R >> 16) & 0xff);
	out[6] = (uint8_t)((R >> 8) & 0xff);
	out[7] = (uint8_t)(R & 0xff);
}

EXPORT_PREFIX void Misty1BlockDecrypt(const MistyKeySet key_set, const uint8_t* in, uint8_t* out) {
	uint32_t L = ((uint32_t)in[0] << 24) | ((uint32_t)in[1] << 16) | ((uint32_t)in[2] << 8) | ((uint32_t)in[3]);
	uint32_t R = ((uint32_t)in[4] << 24) | ((uint32_t)in[5] << 16) | ((uint32_t)in[6] << 8) | ((uint32_t)in[7]);
	// Extra FL Layer
	L ^= R;
	R ^= L;
	L ^= R;
	L = FL_inv(L, key_set.KL[8]);
	R = FL_inv(R, key_set.KL[9]);
	for (int i = 7; i >= 0; i--) {
		// Round Function Layer
		L ^= R;
		R ^= L;
		L ^= R;
		R ^= FO(L, key_set.KO[i], key_set.KI[i]);
		// FL Layer
		if (i % 2 == 0) {
			L = FL_inv(L, key_set.KL[i]);
			R = FL_inv(R, key_set.KL[i + 1]);
		}
	}
	out[0] = (uint8_t)((L >> 24) & 0xff);
	out[1] = (uint8_t)((L >> 16) & 0xff);
	out[2] = (uint8_t)((L >> 8) & 0xff);
	out[3] = (uint8_t)(L & 0xff);
	out[4] = (uint8_t)((R >> 24) & 0xff);
	out[5] = (uint8_t)((R >> 16) & 0xff);
	out[6] = (uint8_t)((R >> 8) & 0xff);
	out[7] = (uint8_t)(R & 0xff);
}

void u8arr_to_u64(const uint8_t in[8], uint64_t* out) {
	*out = 0;
	*out |= ((uint64_t)in[0]) << 56;
	*out |= ((uint64_t)in[1]) << 48;
	*out |= ((uint64_t)in[2]) << 40;
	*out |= ((uint64_t)in[3]) << 32;
	*out |= ((uint64_t)in[4]) << 24;
	*out |= ((uint64_t)in[5]) << 16;
	*out |= ((uint64_t)in[6]) << 8;
	*out |= ((uint64_t)in[7]) << 0;
}

void u64_to_u8arr(const uint64_t* in, uint8_t out[8]) {
	out[0] = (uint16_t)((*in >> 56) & 0xFF);
	out[1] = (uint16_t)((*in >> 48) & 0xFF);
	out[2] = (uint16_t)((*in >> 40) & 0xFF);
	out[3] = (uint16_t)((*in >> 32) & 0xFF);
	out[4] = (uint16_t)((*in >> 24) & 0xFF);
	out[5] = (uint16_t)((*in >> 16) & 0xFF);
	out[6] = (uint16_t)((*in >> 8) & 0xFF);
	out[7] = (uint16_t)((*in >> 0) & 0xFF);
}
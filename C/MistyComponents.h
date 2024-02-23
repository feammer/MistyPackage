#pragma once
#ifndef MISTY_COMPONENTS_H
#define MISTY_COMPONENTS_H

#include <stdint.h>

#ifdef EXPORT_PREFIX
#undef EXPORT_PREFIX
#endif  // EXPORT_PREFIX

#ifdef _WIN32
#define EXPORT_PREFIX __declspec(dllexport)
#elif __linux__
#define EXPORT_PREFIX
#else
#define EXPORT_PREFIX
#endif  // _WIN32

typedef struct {
	uint16_t KO[8][4];
	uint16_t KI[8][3];
	uint16_t KL[10][2];
} MistyKeySet;

EXPORT_PREFIX uint16_t FI(const uint16_t, const uint16_t);
EXPORT_PREFIX uint32_t FO(const uint32_t, const uint16_t[4], const uint16_t[3]);
EXPORT_PREFIX uint32_t FL(const uint32_t, const uint16_t[2]);
EXPORT_PREFIX uint32_t FL_inv(const uint32_t, const uint16_t[2]);
EXPORT_PREFIX MistyKeySet KeyScheduling(const uint8_t[16]);
EXPORT_PREFIX void Misty1BlockEncrypt(const MistyKeySet, const uint8_t* in, uint8_t* out);
EXPORT_PREFIX void Misty1BlockDecrypt(const MistyKeySet, const uint8_t* in, uint8_t* out);
void u8arr_to_u64(const uint8_t in[8], uint64_t* out);
void u64_to_u8arr(const uint64_t* in, uint8_t out[8]);

#endif  // MISTY_COMPONENTS_H
def S7(x: int) -> int:
    x0, x1, x2, x3, x4, x5, x6 = [(x >> i) & 1 for i in range(7)]
    y0 = x0 ^ (x1 & x3) ^ (x0 & x3 & x4) ^ (x1 & x5) ^ (x0 & x2 & x5) ^ (x4 & x5) ^ (x0 & x1 & x6) ^ (x2 & x6) ^ (
            x0 & x5 & x6) ^ (x3 & x5 & x6) ^ 1
    y1 = (x0 & x2) ^ (x0 & x4) ^ (x3 & x4) ^ (x1 & x5) ^ (x2 & x4 & x5) ^ x6 ^ (x0 & x6) ^ (x3 & x6) ^ (
            x2 & x3 & x6) ^ (x1 & x4 & x6) ^ (x0 & x5 & x6) ^ 1
    y2 = (x1 & x2) ^ (x0 & x2 & x3) ^ x4 ^ (x1 & x4) ^ (x0 & x1 & x4) ^ (x0 & x5) ^ (x0 & x4 & x5) ^ (x3 & x4 & x5) ^ (
            x1 & x6) ^ (x3 & x6) ^ (x0 & x3 & x6) ^ (x4 & x6) ^ (x2 & x4 & x6)
    y3 = x0 ^ x1 ^ (x0 & x1 & x2) ^ (x0 & x3) ^ (x2 & x4) ^ (x1 & x4 & x5) ^ (x2 & x6) ^ (x1 & x3 & x6) ^ (
            x0 & x4 & x6) ^ (x5 & x6) ^ 1
    y4 = (x2 & x3) ^ (x0 & x4) ^ (x1 & x3 & x4) ^ x5 ^ (x2 & x5) ^ (x1 & x2 & x5) ^ (x0 & x3 & x5) ^ (x1 & x6) ^ (
            x1 & x5 & x6) ^ (x4 & x5 & x6) ^ 1
    y5 = x0 ^ x1 ^ x2 ^ (x0 & x1 & x2) ^ (x0 & x3) ^ (x1 & x2 & x3) ^ (x1 & x4) ^ (x0 & x2 & x4) ^ (x0 & x5) ^ (
            x0 & x1 & x5) ^ (x3 & x5) ^ (x0 & x6) ^ (x2 & x5 & x6)
    y6 = (x0 & x1) ^ x3 ^ (x0 & x3) ^ (x2 & x3 & x4) ^ (x0 & x5) ^ (x2 & x5) ^ (x3 & x5) ^ (x1 & x3 & x5) ^ (
            x1 & x6) ^ (x1 & x2 & x6) ^ (x0 & x3 & x6) ^ (x4 & x6) ^ (x2 & x5 & x6)
    y = (y6 << 6) | (y5 << 5) | (y4 << 4) | (y3 << 3) | (y2 << 2) | (y1 << 1) | (y0 << 0)
    return y


def S9(x: int) -> int:
    x0, x1, x2, x3, x4, x5, x6, x7, x8 = [(x >> i) & 1 for i in range(9)]
    y0 = (x0 & x4) ^ (x0 & x5) ^ (x1 & x5) ^ (x1 & x6) ^ (x2 & x6) ^ (x2 & x7) ^ (x3 & x7) ^ (x3 & x8) ^ (x4 & x8) ^ 1
    y1 = (x0 & x2) ^ x3 ^ (x1 & x3) ^ (x2 & x3) ^ (x3 & x4) ^ (x4 & x5) ^ (x0 & x6) ^ (x2 & x6) ^ x7 ^ (x0 & x8) ^ (
            x3 & x8) ^ (x5 & x8) ^ 1
    y2 = (x0 & x1) ^ (x1 & x3) ^ x4 ^ (x0 & x4) ^ (x2 & x4) ^ (x3 & x4) ^ (x4 & x5) ^ (x0 & x6) ^ (x5 & x6) ^ (
            x1 & x7) ^ (x3 & x7) ^ x8
    y3 = x0 ^ (x1 & x2) ^ (x2 & x4) ^ x5 ^ (x1 & x5) ^ (x3 & x5) ^ (x4 & x5) ^ (x5 & x6) ^ (x1 & x7) ^ (x6 & x7) ^ (
            x2 & x8) ^ (x4 & x8)
    y4 = x1 ^ (x0 & x3) ^ (x2 & x3) ^ (x0 & x5) ^ (x3 & x5) ^ x6 ^ (x2 & x6) ^ (x4 & x6) ^ (x5 & x6) ^ (x6 & x7) ^ (
            x2 & x8) ^ (x7 & x8)
    y5 = x2 ^ (x0 & x3) ^ (x1 & x4) ^ (x3 & x4) ^ (x1 & x6) ^ (x4 & x6) ^ x7 ^ (x3 & x7) ^ (x5 & x7) ^ (x6 & x7) ^ (
            x0 & x8) ^ (x7 & x8)
    y6 = (x0 & x1) ^ x3 ^ (x1 & x4) ^ (x2 & x5) ^ (x4 & x5) ^ (x2 & x7) ^ (x5 & x7) ^ x8 ^ (x0 & x8) ^ (x4 & x8) ^ (
            x6 & x8) ^ (x7 & x8) ^ 1
    y7 = x1 ^ (x0 & x1) ^ (x1 & x2) ^ (x2 & x3) ^ (x0 & x4) ^ x5 ^ (x1 & x6) ^ (x3 & x6) ^ (x0 & x7) ^ (x4 & x7) ^ (
            x6 & x7) ^ (x1 & x8) ^ 1
    y8 = x0 ^ (x0 & x1) ^ (x1 & x2) ^ x4 ^ (x0 & x5) ^ (x2 & x5) ^ (x3 & x6) ^ (x5 & x6) ^ (x0 & x7) ^ (x0 & x8) ^ (
            x3 & x8) ^ (x6 & x8) ^ 1
    y = (y8 << 8) | (y7 << 7) | (y6 << 6) | (y5 << 5) | (y4 << 4) | (y3 << 3) | (y2 << 2) | (y1 << 1) | (y0 << 0)
    return y


def FI(_input: int, _KI: int) -> int:
    """
    :param _input: 16 bits, split into left(9 bits) and right(7 bits)
    :param _KI: 16 bits, split into left(9 bits) and right(7 bits)
    :return: 16 bits
    """
    _S7 = [27, 50, 51, 90, 59, 16, 23, 84, 91, 26, 114, 115, 107, 44, 102, 73, 31, 36, 19, 108, 55, 46, 63, 74, 93, 15,
           64, 86, 37, 81, 28, 4, 11, 70, 32, 13, 123, 53, 68, 66, 43, 30, 65, 20, 75, 121, 21, 111, 14, 85, 9, 54, 116,
           12, 103, 83, 40, 10, 126, 56, 2, 7, 96, 41, 25, 18, 101, 47, 48, 57, 8, 104, 95, 120, 42, 76, 100, 69, 117,
           61, 89, 72, 3, 87, 124, 79, 98, 60, 29, 33, 94, 39, 106, 112, 77, 58, 1, 109, 110, 99, 24, 119, 35, 5, 38,
           118, 0, 49, 45, 122, 127, 97, 80, 34, 17, 6, 71, 22, 82, 78, 113, 62, 105, 67, 52, 92, 88, 125]
    _S9 = [451, 203, 339, 415, 483, 233, 251, 53, 385, 185, 279, 491, 307, 9, 45, 211, 199, 330, 55, 126, 235, 356, 403,
           472, 163, 286, 85, 44, 29, 418, 355, 280, 331, 338, 466, 15, 43, 48, 314, 229, 273, 312, 398, 99, 227, 200,
           500, 27, 1, 157, 248, 416, 365, 499, 28, 326, 125, 209, 130, 490, 387, 301, 244, 414, 467, 221, 482, 296,
           480, 236, 89, 145, 17, 303, 38, 220, 176, 396, 271, 503, 231, 364, 182, 249, 216, 337, 257, 332, 259, 184,
           340, 299, 430, 23, 113, 12, 71, 88, 127, 420, 308, 297, 132, 349, 413, 434, 419, 72, 124, 81, 458, 35, 317,
           423, 357, 59, 66, 218, 402, 206, 193, 107, 159, 497, 300, 388, 250, 406, 481, 361, 381, 49, 384, 266, 148,
           474, 390, 318, 284, 96, 373, 463, 103, 281, 101, 104, 153, 336, 8, 7, 380, 183, 36, 25, 222, 295, 219, 228,
           425, 82, 265, 144, 412, 449, 40, 435, 309, 362, 374, 223, 485, 392, 197, 366, 478, 433, 195, 479, 54, 238,
           494, 240, 147, 73, 154, 438, 105, 129, 293, 11, 94, 180, 329, 455, 372, 62, 315, 439, 142, 454, 174, 16, 149,
           495, 78, 242, 509, 133, 253, 246, 160, 367, 131, 138, 342, 155, 316, 263, 359, 152, 464, 489, 3, 510, 189,
           290, 137, 210, 399, 18, 51, 106, 322, 237, 368, 283, 226, 335, 344, 305, 327, 93, 275, 461, 121, 353, 421,
           377, 158, 436, 204, 34, 306, 26, 232, 4, 391, 493, 407, 57, 447, 471, 39, 395, 198, 156, 208, 334, 108, 52,
           498, 110, 202, 37, 186, 401, 254, 19, 262, 47, 429, 370, 475, 192, 267, 470, 245, 492, 269, 118, 276, 427,
           117, 268, 484, 345, 84, 287, 75, 196, 446, 247, 41, 164, 14, 496, 119, 77, 378, 134, 139, 179, 369, 191, 270,
           260, 151, 347, 352, 360, 215, 187, 102, 462, 252, 146, 453, 111, 22, 74, 161, 313, 175, 241, 400, 10, 426,
           323, 379, 86, 397, 358, 212, 507, 333, 404, 410, 135, 504, 291, 167, 440, 321, 60, 505, 320, 42, 341, 282,
           417, 408, 213, 294, 431, 97, 302, 343, 476, 114, 394, 170, 150, 277, 239, 69, 123, 141, 325, 83, 95, 376,
           178, 46, 32, 469, 63, 457, 487, 428, 68, 56, 20, 177, 363, 171, 181, 90, 386, 456, 468, 24, 375, 100, 207,
           109, 256, 409, 304, 346, 5, 288, 443, 445, 224, 79, 214, 319, 452, 298, 21, 6, 255, 411, 166, 67, 136, 80,
           351, 488, 289, 115, 382, 188, 194, 201, 371, 393, 501, 116, 460, 486, 424, 405, 31, 65, 13, 442, 50, 61, 465,
           128, 168, 87, 441, 354, 328, 217, 261, 98, 122, 33, 511, 274, 264, 448, 169, 285, 432, 422, 205, 243, 92,
           258, 91, 473, 324, 502, 173, 165, 58, 459, 310, 383, 70, 225, 30, 477, 230, 311, 506, 389, 140, 143, 64, 437,
           190, 120, 0, 172, 272, 350, 292, 2, 444, 162, 234, 112, 508, 278, 348, 76, 450]
    _L, _R = ((_input >> 7) & 0x1FF), (_input & 0x7F)
    # Round 1
    _L, _R = _R, _S9[_L] ^ _R
    # Round 2
    _L = _S7[_L] ^ (_R & 0x7F) ^ ((_KI >> 9) & 0x7F)
    _R = _R ^ (_KI & 0x1FF)
    _L, _R = _R, _L
    # Round 3
    _L, _R = _R, _S9[_L] ^ _R
    _output = (_L << 9) | _R
    return _output


def FO(_input: int, _KO: list, _KI: list) -> int:
    """
    :param _input: 4 bytes (32 bits), split into left(16 bits) and right(16 bits)
    :param _KO: [KO_1, KO_2, KO_3, KO_4], 16 bits each
    :param _KI: [KI_1, KI_2, KI_3], 16 bits each
    :return: 4 bytes (32 bits)
    """
    _L, _R = ((_input >> 16) & 0xFFFF), (_input & 0xFFFF)
    for _round in range(3):
        _L, _R = _R, FI(_L ^ _KO[_round], _KI[_round]) ^ _R
    _L ^= _KO[3]
    _output = (_L << 16) | _R
    return _output


def FL(_input: int, _KL: list) -> int:
    """
    :param _input: 32 bits, split into left(16 bits) and right(16 bits)
    :param _KL: [KL_1, KL_2], 16 bits each
    :return: 4 bytes 32 bits
    """
    _L, _R = ((_input >> 16) & 0xFFFF), (_input & 0xFFFF)
    _R ^= _L & _KL[0]
    _L ^= _R | _KL[1]
    _output = (_L << 16) | _R
    return _output


def FL_inv(_input: int, _KL: list) -> int:
    """
    :param _input: 32 bits, split into left(16 bits) and right(16 bits)
    :param _KL: [KL_1, KL_2], 16 bits each
    :return: 4 bytes 32 bits
    """
    _L, _R = ((_input >> 16) & 0xFFFF), (_input & 0xFFFF)
    _L ^= _R | _KL[1]
    _R ^= _L & _KL[0]
    _output = (_L << 16) | _R
    return _output


def KeyScheduling(_main_key: bytes) -> dict:
    """
    Fit for round=8

    :param _main_key: 16 bytes
    :return: {'KO': _KO, 'KI': _KI, 'KL': _KL}
    """
    _Key: list[int] = [((_main_key[2 * _i] << 8) | _main_key[2 * _i + 1]) for _i in range(8)]
    _SubKey: list[int] = [FI(_Key[_i], _Key[(_i + 1) % 8]) for _i in range(8)]
    _KO: list[list] = [[_Key[_i % 8], _Key[(_i + 2) % 8], _Key[(_i + 7) % 8], _Key[(_i + 4) % 8]]
                       for _i in range(8)]
    _KI: list[list] = [[_SubKey[(_i + 5) % 8], _SubKey[(_i + 1) % 8], _SubKey[(_i + 3) % 8]]
                       for _i in range(8)]
    # CAUTION!!! Matsui defined Ki ranging from 1 to 8 while we indexing all types of Ki from 0 to 7.
    # 注意！！！ Matsui在原始论文中Ki从1到8，但是程序索引从0到7。
    _KL: list[list] = [[_SubKey[_i // 2 + 2 - 1], _Key[(_i // 2 + 4 - 1) % 8]] if _i % 2 == 0 else
                       [_Key[(_i + 1) // 2 - 1], _SubKey[((_i + 1) // 2 + 6 - 1) % 8]]
                       for _i in range(1, 10 + 1)]
    return {'KO': _KO, 'KI': _KI, 'KL': _KL}


def Misty1Encrypt(_plain: int, _key_set: dict) -> int:
    """
    Fit for round=8

    :param _plain:
    :param _key_set:
    :return:
    """
    _KO, _KI, _KL = _key_set['KO'], _key_set['KI'], _key_set['KL']
    _L, _R = (_plain >> 32) & 0xFFFFFFFF, _plain & 0xFFFFFFFF
    for i in range(8 // 2):
        _L, _R = FL(_L, _KL[2 * i]), FL(_R, _KL[2 * i + 1])
        _L, _R = _R ^ FO(_L, _KO[2 * i], _KI[2 * i]), _L
        _L, _R = _R ^ FO(_L, _KO[2 * i + 1], _KI[2 * i + 1]), _L
    _L, _R = FL(_L, _KL[8]), FL(_R, _KL[9])
    _L, _R = _R, _L
    _cipher = (_L << 32) | _R
    return _cipher


def Misty1Decrypt(_cipher: int, _key_set: dict) -> int:
    """
    Fit for round=8

    :param _cipher:
    :param _key_set:
    :return:
    """
    _KO, _KI, _KL = _key_set['KO'], _key_set['KI'], _key_set['KL']
    _L, _R = (_cipher >> 32) & 0xFFFFFFFF, _cipher & 0xFFFFFFFF
    _L, _R = _R, _L
    _L, _R = FL_inv(_L, _KL[8]), FL_inv(_R, _KL[9])
    for i in range(8 // 2 - 1, -1, -1):
        _L, _R = _R, _L ^ FO(_R, _KO[2 * i + 1], _KI[2 * i + 1])
        _L, _R = _R, _L ^ FO(_R, _KO[2 * i], _KI[2 * i])
        _L, _R = FL_inv(_L, _KL[2 * i]), FL_inv(_R, _KL[2 * i + 1])
    _plain = (_L << 32) | _R
    return _plain

# if __name__ == '__main__':
#     plain = 0x0123456789abcdef
#     cipher = 0x8b1da5f56ab3d07c
#     key = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
#     key_set = KeyScheduling(key)
#     print(key_set)
#     print(Misty1Encrypt(plain, key_set))
#     print(Misty1Decrypt(cipher, key_set))

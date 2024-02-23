class MODE:
    ECB: int = 0
    CBC: int = 1
    CFB: int = 2
    OFB: int = 3
    CTR: int = 4


class MISTY:
    """
    Fit for MISTY1 with round=8
    """

    # 类初始化，装载密钥，可选的指定野蛮模式（不进行安全检查）
    def __init__(self, _key: bytes, _aggressive: bool = False):
        from .MistyComponents import KeyScheduling as _KeyScheduling
        if type(_key) is not bytes:
            raise TypeError("key type must be bytes")
        elif len(_key) != 16:
            raise TypeError("key size must be 16 bytes")
        if type(_aggressive) is not bool:
            raise TypeError("aggressive type must be bool")
        self.key: bytes = _key
        self.key_set: dict = _KeyScheduling(self.key)
        self.aggressive = _aggressive  # determine checking params are valid or not

    # 合法性检查
    def __secure_check__(self, _input: bytes, _work_mode: int, _iv: bytes):
        if not self.aggressive:
            if type(_input) is not bytes:
                raise TypeError("data type must be bytes")
            if type(_work_mode) is not int:
                raise TypeError("work_mode type must be MISTY.MODE(int)")
            if len(_input) % 8 != 0:
                raise ValueError("data size must be a multiple of 8 bytes")
            if _work_mode != MODE.ECB:
                if type(_iv) is not bytes:
                    raise TypeError("iv type must be bytes")
                if len(_iv) != 8:
                    raise ValueError("iv size must be 8 bytes")

    # 加密过程封装
    def encrypt(self, _input: bytes, _work_mode: int, _iv: bytes = None) -> bytes:
        self.__secure_check__(_input, _work_mode, _iv)
        from .MistyComponents import Misty1Encrypt as _Misty1Encrypt

        _output: bytes = b''
        # 工作模式选择
        if _work_mode == MODE.ECB:
            for _i in range(len(_input) // 8):
                _plain = int.from_bytes(_input[8 * _i:8 * (_i + 1)], byteorder='big')
                _cipher = _Misty1Encrypt(_plain, self.key_set)
                _output += int.to_bytes(_cipher, length=8, byteorder='big')
            return _output
        elif _work_mode == MODE.CBC:
            _iv: int = int.from_bytes(_iv, byteorder='big')
            for _i in range(len(_input) // 8):
                _plain = int.from_bytes(_input[8 * _i:8 * (_i + 1)], byteorder='big')
                _plain ^= _iv
                _cipher = _Misty1Encrypt(_plain, self.key_set)
                _iv = _cipher
                _output += int.to_bytes(_cipher, length=8, byteorder='big')
            return _output
        return _output

    # 解密过程封装
    def decrypt(self, _input: bytes, _work_mode: int, _iv: bytes = None) -> bytes:
        self.__secure_check__(_input, _work_mode, _iv)
        from .MistyComponents import Misty1Decrypt as _Misty1Decrypt

        _output: bytes = b''
        # 工作模式选择
        if _work_mode == MODE.ECB:
            for _i in range(len(_input) // 8):
                _cipher = int.from_bytes(_input[8 * _i:8 * (_i + 1)], byteorder='big')
                _plain = _Misty1Decrypt(_cipher, self.key_set)
                _output += int.to_bytes(_plain, length=8, byteorder='big')
            return _output
        elif _work_mode == MODE.CBC:
            _iv: int = int.from_bytes(_iv, byteorder='big')
            for _i in range(len(_input) // 8):
                _cipher = int.from_bytes(_input[8 * _i:8 * (_i + 1)], byteorder='big')
                _plain = _Misty1Decrypt(_cipher, self.key_set)
                _plain ^= _iv
                _iv = _cipher
                _output += int.to_bytes(_plain, length=8, byteorder='big')
            return _output
        return _output


def New(_key: bytes) -> MISTY:
    return MISTY(_key)

# # test
# if __name__ == '__main__':
#     a = New(b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff')
#     plain = b'\x01\x23\x45\x67\x89\xab\xcd\xef'
#     iv = b'\xfe\xdc\xba\x98\x76\x54\x32\x10'
#     cipher = a.encrypt(plain, MODE.CBC, iv)
#     plain = a.decrypt(cipher, MODE.CBC, iv)
#     print(plain)

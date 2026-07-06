import typing as _typing

from Crypto.Cipher import DES as _DES  # type: ignore[import-untyped]
from Crypto.Cipher import DES3 as _DES3  # type: ignore[import-untyped]

from psec import tools as _tools

__all__ = [
    "apply_key_variant",
    "adjust_key_parity",
    "generate_kcv",
    "encrypt_tdes_cbc",
    "encrypt_tdes_ecb",
    "decrypt_tdes_cbc",
    "decrypt_tdes_ecb",
]


def apply_key_variant(key: _typing.Union[bytes, bytearray], variant: int) -> bytes:
    r"""Apply variant to the most significant byte of each DES key pair.

    Parameters
    ----------
    key : bytes
        Binary (Triple) DES key. Has to be a valid DES key.
    variant : bytes
        Variant in the range of 0 and 31.

    Returns
    -------
    key_variant : bytes
        Binary key under desired variant.

    Raises
    ------
    ValueError
        Key must be a single, double or triple DES key
        Variant must be in the range of 0 to 31

    Examples
    --------
    >>> import psec
    >>> key = bytes.fromhex("0123456789ABCDEF")
    >>> psec.des.apply_key_variant(key, 1).hex().upper()
    '0923456789ABCDEF'
    """

    if len(key) not in {8, 16, 24}:
        raise ValueError("Key must be a single, double or triple DES key")

    if variant < 0 or variant > 31:
        raise ValueError("Variant must be in the range of 0 to 31")

    mask = ((8 * variant).to_bytes(1, "big") + (b"\x00" * 7)) * (len(key) // 8)
    return _tools.xor(key, mask)


def adjust_key_parity(key: _typing.Union[bytes, bytearray]) -> bytes:
    r"""Adjust DES key parity key

    Parameters
    ----------
    key : bytes, bytearray
        Binary key to adjust for odd parity.

    Returns
    -------
    adjusted_key : bytes
        Binary key adjusted for odd parity.

    Examples
    --------
    >>> import psec
    >>> key = bytes.fromhex("1A2B3C4D5F0A1B2C4D5F6A7B8C9D0F1A")
    >>> psec.des.adjust_key_parity(key).hex().upper()
    '1A2A3D4C5E0B1A2C4C5E6B7A8C9D0E1A'
    """
    adjusted_key = bytearray(key)

    for i, byte in enumerate(adjusted_key):
        if not _tools.odd_parity(byte):
            adjusted_key[i] ^= 1

    return bytes(adjusted_key)


def _encrypt_des_block(key: bytes, block: bytes) -> bytes:
    return _DES.new(key, _DES.MODE_ECB).encrypt(block)


def _decrypt_des_block(key: bytes, block: bytes) -> bytes:
    return _DES.new(key, _DES.MODE_ECB).decrypt(block)


def _encrypt_tdes_block_manual(key: bytes, block: bytes) -> bytes:
    if len(key) == 8:
        return _encrypt_des_block(key, block)

    if len(key) == 16:
        k1, k2, k3 = key[:8], key[8:16], key[:8]
    elif len(key) == 24:
        k1, k2, k3 = key[:8], key[8:16], key[16:24]
    else:
        raise ValueError("Key must be a single, double or triple DES key")

    return _encrypt_des_block(k1, _decrypt_des_block(k2, _encrypt_des_block(k3, block)))


def _decrypt_tdes_block_manual(key: bytes, block: bytes) -> bytes:
    if len(key) == 8:
        return _decrypt_des_block(key, block)

    if len(key) == 16:
        k1, k2, k3 = key[:8], key[8:16], key[:8]
    elif len(key) == 24:
        k1, k2, k3 = key[:8], key[8:16], key[16:24]
    else:
        raise ValueError("Key must be a single, double or triple DES key")

    return _decrypt_des_block(k3, _encrypt_des_block(k2, _decrypt_des_block(k1, block)))


def _encrypt_tdes_ecb(key: bytes, data: bytes) -> bytes:
    if len(key) == 8:
        return _DES.new(key, _DES.MODE_ECB).encrypt(data)

    try:
        return _DES3.new(key, _DES3.MODE_ECB).encrypt(data)
    except ValueError:
        encrypted = bytearray()
        for offset in range(0, len(data), 8):
            encrypted.extend(_encrypt_tdes_block_manual(key, data[offset : offset + 8]))
        return bytes(encrypted)


def _decrypt_tdes_ecb(key: bytes, data: bytes) -> bytes:
    if len(key) == 8:
        return _DES.new(key, _DES.MODE_ECB).decrypt(data)

    try:
        return _DES3.new(key, _DES3.MODE_ECB).decrypt(data)
    except ValueError:
        decrypted = bytearray()
        for offset in range(0, len(data), 8):
            decrypted.extend(_decrypt_tdes_block_manual(key, data[offset : offset + 8]))
        return bytes(decrypted)


def _encrypt_tdes_cbc(key: bytes, iv: bytes, data: bytes) -> bytes:
    if len(key) == 8:
        return _DES.new(key, _DES.MODE_CBC, iv=iv).encrypt(data)

    try:
        return _DES3.new(key, _DES3.MODE_CBC, iv=iv).encrypt(data)
    except ValueError:
        encrypted = bytearray()
        previous = iv

        for offset in range(0, len(data), 8):
            block = _tools.xor(data[offset : offset + 8], previous)
            previous = _encrypt_tdes_block_manual(key, block)
            encrypted.extend(previous)

        return bytes(encrypted)


def _decrypt_tdes_cbc(key: bytes, iv: bytes, data: bytes) -> bytes:
    if len(key) == 8:
        return _DES.new(key, _DES.MODE_CBC, iv=iv).decrypt(data)

    try:
        return _DES3.new(key, _DES3.MODE_CBC, iv=iv).decrypt(data)
    except ValueError:
        decrypted = bytearray()
        previous = iv

        for offset in range(0, len(data), 8):
            block = data[offset : offset + 8]
            decrypted.extend(_tools.xor(_decrypt_tdes_block_manual(key, block), previous))
            previous = block

        return bytes(decrypted)


def generate_kcv(key: bytes, length: int = 2) -> bytes:
    r"""Generate DES key checksum value (KCV).

    Parameters
    ----------
    key : bytes
        Binary key to provide check digits for. Has to be a valid DES key.
    length : int, optional
        Number of KCV bytes returned (default 2).

    Returns
    -------
    kcv : bytes
        Binary KCV (`length` bytes)

    Examples
    --------
    >>> import psec
    >>> key = bytes.fromhex("0123456789ABCDEFFEDCBA9876543210")
    >>> psec.des.generate_kcv(key).hex().upper()
    '08D7'
    """
    return _encrypt_tdes_ecb(key, b"\x00\x00\x00\x00\x00\x00\x00\x00")[:length]


def encrypt_tdes_cbc(key: bytes, iv: bytes, data: bytes) -> bytes:
    r"""Encrypt data using Triple DES CBC algorithm.

    Parameters
    ----------
    key : bytes
        Binary Triple DES key. Has to be a valid DES key.
    iv : bytes
        Binary initial initialization vector for CBC.
        Has to be 8 bytes long.
    data : bytes
        Binary data to be encrypted.
        Has to be multiple of 8 bytes.

    Returns
    -------
    encrypted_data : bytes
        Binary encrypted data.

    Raises
    ------
    ValueError
        Data length must be multiple of DES block size 8.

    Examples
    --------
    >>> import psec
    >>> key = bytes.fromhex("0123456789ABCDEFFEDCBA9876543210")
    >>> iv = bytes.fromhex("0000000000000000")
    >>> psec.des.encrypt_tdes_cbc(key, iv, b"12345678").hex().upper()
    '41D2FFBA3CDC15FE'
    """
    if len(data) < 8 or len(data) % 8 != 0:
        raise ValueError(
            f"Data length ({str(len(data))}) must be multiple of DES block size 8."
        )

    return _encrypt_tdes_cbc(key, iv, data)


def encrypt_tdes_ecb(key: bytes, data: bytes) -> bytes:
    r"""Encrypt data using Triple DES ECB algorithm.

    Parameters
    ----------
    key : bytes
        Binary Triple DES key. Has to be a valid DES key.
    data : bytes
        Binary data to be encrypted.
        Has to be multiple of 8 bytes.

    Returns
    -------
    encrypted_data : bytes
        Binary encrypted data.

    Raises
    ------
    ValueError
        Data length must be multiple of DES block size 8.

    Examples
    --------
    >>> import psec
    >>> key = bytes.fromhex("0123456789ABCDEFFEDCBA9876543210")
    >>> psec.des.encrypt_tdes_ecb(key, b"12345678").hex().upper()
    '41D2FFBA3CDC15FE'
    """
    if len(data) < 8 or len(data) % 8 != 0:
        raise ValueError(
            f"Data length ({str(len(data))}) must be multiple of DES block size 8."
        )

    return _encrypt_tdes_ecb(key, data)


def decrypt_tdes_cbc(key: bytes, iv: bytes, data: bytes) -> bytes:
    r"""Decrypt data using Triple DES CBC algorithm.

    Parameters
    ----------
    key : bytes
        Binary Triple DES key. Has to be a valid DES key.
    iv : bytes
        Binary initial initialization vector for CBC.
        Has to be 8 bytes long.
    data : bytes
        Binary data to be decrypted.
        Has to be multiple of 8 bytes.

    Returns
    -------
    decrypted_data : bytes
        Binary decrypted data.

    Raises
    ------
    ValueError
        Data length must be multiple of DES block size 8.

    Examples
    --------
    >>> import psec
    >>> key = bytes.fromhex("0123456789ABCDEFFEDCBA9876543210")
    >>> iv = bytes.fromhex("0000000000000000")
    >>> psec.des.decrypt_tdes_cbc(key, iv, bytes.fromhex("41D2FFBA3CDC15FE"))
    b'12345678'
    """
    if len(data) < 8 or len(data) % 8 != 0:
        raise ValueError(
            f"Data length ({str(len(data))}) must be multiple of DES block size 8."
        )

    return _decrypt_tdes_cbc(key, iv, data)


def decrypt_tdes_ecb(key: bytes, data: bytes) -> bytes:
    r"""Decrypt data using Triple DES ECB algorithm.

    Parameters
    ----------
    key : bytes
        Binary Triple DES key. Has to be a valid DES key.
    data : bytes
        Binary data to be decrypted.
        Has to be multiple of 8 bytes.

    Returns
    -------
    decrypted_data : bytes
        Binary decrypted data.

    Raises
    ------
    ValueError
        Data length must be multiple of DES block size 8.

    Examples
    --------
    >>> import psec
    >>> key = bytes.fromhex("0123456789ABCDEFFEDCBA9876543210")
    >>> psec.des.decrypt_tdes_ecb(key, bytes.fromhex("41D2FFBA3CDC15FE"))
    b'12345678'
    """
    if len(data) < 8 or len(data) % 8 != 0:
        raise ValueError(
            f"Data length ({str(len(data))}) must be multiple of DES block size 8."
        )

    return _decrypt_tdes_ecb(key, data)

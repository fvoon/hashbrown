#!/usr/bin/env python3
"""
hashbrown - Generate descriptor codes for fund options.

Replicates Java's CardMerchantDescriptorUtils.generateDescriptorCode() algorithm.
"""

import argparse
import hashlib

ALPHANUMERIC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
DESCRIPTOR_CODE_LENGTH = 2


def generate_descriptor_code(user_id: str, fund_option_id: int) -> str:
    """
    Generate a deterministic 2-character alphanumeric code prefix for a fund option.

    Format: 2 characters from A-Z0-9 followed by a dash (36^2 = 1,296 possible codes).

    Algorithm: hash = SHA-256(userId + ":" + fundOptionId), then each character
    is derived from a separate byte of the hash: ALPHANUMERIC[hash[i] % 36].
    """
    input_str = f"{user_id}:{fund_option_id}"
    hash_bytes = hashlib.sha256(input_str.encode("utf-8")).digest()

    code = ""
    for i in range(DESCRIPTOR_CODE_LENGTH):
        byte_val = hash_bytes[i]
        code += ALPHANUMERIC[byte_val % len(ALPHANUMERIC)]

    return code + "-"


def main():
    parser = argparse.ArgumentParser(
        description="Generate descriptor codes for fund options",
        epilog="Example: hashbrown 550e8400-e29b-41d4-a716-446655440000 12345",
    )
    parser.add_argument("user_id", help="User's UUID")
    parser.add_argument("fund_option_id", type=int, help="Fund option's auto-increment ID")

    args = parser.parse_args()
    print(generate_descriptor_code(args.user_id, args.fund_option_id))


if __name__ == "__main__":
    main()

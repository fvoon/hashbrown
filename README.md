# hashbrown

Generate deterministic descriptor codes for fund options.

## Usage

```bash
python3 hashbrown.py <user-id> <fund-option-id>
```

## Examples

```bash
# Basic usage
python3 hashbrown.py "6891b240c027ea1405ec3005" 1
# Output: S5-

# With a UUID
python3 hashbrown.py "550e8400-e29b-41d4-a716-446655440000" 12345
# Output: 9T-

# Different fund options produce different codes
python3 hashbrown.py "6891b240c027ea1405ec3005" 1   # S5-
python3 hashbrown.py "6891b240c027ea1405ec3005" 2   # CX-
python3 hashbrown.py "6891b240c027ea1405ec3005" 3   # U1-
```

## How It Works

1. Concatenates `userId:fundOptionId`
2. Computes SHA-256 hash
3. Maps first 2 bytes to alphanumeric characters (A-Z, 0-9)
4. Appends a dash

This produces 1,296 possible codes (36²), making collisions unlikely for typical users.

## Requirements

Python 3.6+ (uses only stdlib)

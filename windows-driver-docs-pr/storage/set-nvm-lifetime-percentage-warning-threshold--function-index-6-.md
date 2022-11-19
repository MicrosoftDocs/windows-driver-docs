---
title: Set NVM Lifetime Percentage Warning Threshold (Function Index 6)
description: This function sets the warning threshold for remaining non-volatile memory lifetime percentage.
ms.date: 11/18/2022
---

# Set NVM Lifetime Percentage Warning Threshold (Function Index 6)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function sets the warning threshold for remaining non-volatile memory lifetime percentage.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **NVM Lifetime Percentage Warning Threshold** | 1 | 0 | The percentage value of the warning threshold, which must be between 0 and 100. The platform shall write this value to the *NVM_LIFETIME_WARNING_THRESHOLD* (0, 0x98) register. |

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

## Related articles

[Get NVM Thresholds (Function Index 5)](get-nvm-thresholds--function-index-5-.md)

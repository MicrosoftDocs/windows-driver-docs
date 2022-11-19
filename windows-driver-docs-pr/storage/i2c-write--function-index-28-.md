---
title: I2C Write (Function Index 28)
description: This function writes an Inter-Integrated Circuit (I2C) register.
ms.date: 11/18/2022
---

# I2C Write (Function Index 28)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function writes an Inter-Integrated Circuit (I2C) register. This functionality enables scenarios that require the use of vendor-specific registers. It's also used for debugging.

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Page**   | 1 | 0 | The page in which the I2C register is located. |
| **Offset** | 1 | 1 | The register’s offset inside the page. |
| **Data**   | 1 | 2 | The data to be written to the register. |

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | This function can return the following Function-Specific Error Codes: 1. *Invalid page.* 2. *This register cannot be written to.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

## Related articles

[I2C Read (Function Index 27)](i2c-read--function-index-27-.md)

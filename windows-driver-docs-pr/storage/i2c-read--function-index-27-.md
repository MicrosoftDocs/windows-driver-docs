---
title: I2C Read (Function Index 27)
description: This function reads an Inter-Integrated Circuit (I2C) register.
ms.date: 11/18/2022
---

# I2C Read (Function Index 27)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function reads an Inter-Integrated Circuit (I2C) register. This functionality enables scenarios that require the use of vendor-specific registers. It's also used for debugging.

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Page**   | 1 | 0 | The page in which the I2C register is located. |
| **Offset** | 1 | 1 | The register’s offset inside the page. |

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | This function can return the following Function-Specific Error Code: 1: *Invalid page.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Data** | 1 | 4 | | The data in the specified register. |

## Related articles

[I2C Write (Function Index 28)](i2c-write--function-index-28-.md)

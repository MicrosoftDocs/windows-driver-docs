---
title: Read Typed Data (Function Index 29)
description: This function reads a 32-byte block inside a typed block data region.
ms.date: 11/18/2022
---

# Read Typed Data (Function Index 29)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function reads a 32-byte block inside a typed block data region. This functionality enables scenarios that require the use of vendor-specific registers. It's also used for debugging.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Data Type** | 1 | 0 | The type of the data. This field must be one of the values specified in *TYPED_BLOCK_DATA* (3, 0x04). |
| **Region ID** | 2 | 1 | The identification of the region that is being read. |
| **Block ID**  | 1 | 3 | The identification of the block being read inside the region. |

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0  | This function can return the following Function-Specific Error Code: *Invalid data type.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Data**   | 32 | 4 | The data from the specified block. |

## Remarks

The platform shall use Typed Block Data registers to implement this function.

## Related articles

[Write Typed Data (Function Index 30)](write-typed-data--function-index-30-.md)

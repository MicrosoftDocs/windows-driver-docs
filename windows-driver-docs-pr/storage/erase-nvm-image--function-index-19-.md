---
title: Erase NVM Image (Function Index 19)
description: This function erases the backup image saved in the non-volatile memory module.
ms.date: 11/18/2022
---

# Erase NVM Image (Function Index 19)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function erases the backup image saved in the non-volatile memory module.

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status**                   | 4 | 0 | This function can return the following Function-Specific Error Code: 1. *The operation timed out.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

> [!NOTE]
> This is a synchronous function. It returns only when the erase operation has finished or timed out. If the operation takes longer than the timeout defined in *ERASE_TIMEOUT0* (0, 0x1E) and *ERASE_TIMEOUT1* (0, 0x1F), the platform shall abort this function before it returns.
